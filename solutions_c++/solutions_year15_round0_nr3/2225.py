#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define fore(i, l, r) for(int i = l; i < r; i++)
#define forn(i, n) fore(i, 0, n)

typedef vector<int> vi;

int evaluate(int a, int b, int table[5][5]){
  // a * b
  int sgn = (a * b) / abs(a * b);
  int v = table[abs(a)][abs(b)] * sgn;
  return v;
}

int fs(int a, int b, int table[5][5]){
  // a * x = b, x = ?
  if (a == 1 || a == -1){
    return b * a;
  }
  else return evaluate(-a, b, table);
}

int ff(int a, int b, int table[5][5]){
  // x * a = b, x = ?
  if (a == 1 || a == -1){
    return b * a;
  }
  else return evaluate(b, -a, table);  
}

int powr(int a, int n){
  if (n == 0) return 1;
  else if (n == 1) return a;
  else if (n == 2) {
    if (a == 1 || a == -1) return 1;
    return -1;
  }
  else if (n == 3){
    if (a == 1 || a == -1) return a;
    return -a;
  }
}

int main(){
  int t;
  scanf("%d", &t);
  fore(cs, 1, t + 1){
    int l;
    long long c;
    scanf("%d %lld", &l, &c);
    char arr[10005];
    scanf("%s", arr); 
    // if (cs == 22){
    //    cout<<l<<" "<<c<<" "<<arr<<endl;
    // }
    vi inp(l, 1);
    int table[5][5] = {{1, 1, 1, 1, 1},
		       {1, 1, 2, 3, 4}, 
		       {1, 2, -1, 4, -3}, 
		       {1, 3, -4, -1, 2}, 
		       {1, 4, 3, -2, -1}};
    
    forn(i, l){
      inp[i] += arr[i] - 'i' + 1;
    }
    
    vi dpf(l + 1, 0);
    dpf[0] = 1;
    forn(i, l){
      int sgn = dpf[i] / abs(dpf[i]);
      dpf[i + 1] = table[abs(dpf[i])][inp[i]] * sgn;
    }
    
    vi dpb(l + 1, 0);
    dpb[l] = 1;
    for(int i = l - 1; i >= 0; i--){
      int sgn = dpb[i + 1] / abs(dpb[i + 1]);
      dpb[i] = table[inp[i]][abs(dpb[i + 1])] * sgn;
    }    
    
    int ind = 0;
    int tot = dpf[l];
    int rem = ((c - 1) % 4);

    // case 1 , when same block splits twice
    forn(n1, 4){
      forn(n2, 4){
	if ((n1 + n2) <= (c - 1) && (n1 + n2) % 4 == rem){
	  // valid case
	  //	  cout<<n1<<" - "<<n2<<endl;
	  int v1 = powr(tot, n1), v2 = powr(tot, n2);// cout<<v1<<" power "<<v2<<endl;
	  v1 = fs(v1, 2, table);
	  v2 = ff(v2, 4, table);// cout<<v1<<" after f "<<v2<<endl;
	  int pos1 = l, pos2 = 0;
	  forn(i, l + 1){
	    if (dpf[i] == v1){
	      pos1 = i;
	      break;
	    }
	  }
	  for(int i = l; i >= 0; i--){
	    if (dpb[i] == v2){
	      pos2 = i;
	      break;
	    }
	  }
	  
	  if (pos1 < pos2){
	    // valid chance
	    int y = ff(v2, tot, table);
	    y = fs(v1, y, table);
	    if (y == 3){
	      //	      cout<<rem<<" rem "<<endl;
	      //  cout<<"output case 1 "<<n1<<" "<<n2<<" "<<" "<<pos1<<" "<<pos2<<endl;
	      ind = 1;
	      break;
	    }
	  }
	}
      }
      if (ind) break;
    }
    
    if (!ind && c >= 2){
      // when diff block splits
      rem = ((c - 2) % 4);
      forn(n1, 4){
	forn(n2, 4){
	  forn(n3, 4){
	    if ((n1 + n2 + n3) <= c - 2 && (n1 + n2 + n3) % 4 == rem){
	      // valid n's
	      //cout<<n1<<" - "<<n2<<" - "<<n3<<endl;
	      int v1 = powr(tot, n1);
	      int v2 = powr(tot, n2);
	      int v3 = powr(tot, n3);
	      v1 = fs(v1, 2, table);
	      v3 = ff(v3, 4, table);
	      int pos1 = -1, pos2 = -1;
	      forn(i, l + 1){
		if (dpf[i] == v1){
		  pos1 = i; break;
		}
	      }
	      forn(i, l + 1){
		if (dpb[i] == v3){
		  pos2 = i; break;
		}
	      }
	      if (pos1 > -1 && pos2 > -1){
		v1 = fs(v1, tot, table);
		v3 = ff(v3, tot, table);
		
		if (evaluate(v1, evaluate(v2, v3, table), table) == 3){
		  ind = 1;
		  break;
		}
	      }
	    }
	  }
	  if (ind) break;
	}
	if (ind) break;
      }
    }

    if (ind){
      printf("Case #%d: YES\n", cs);
    }
    else printf("Case #%d: NO\n", cs);
  }
}
