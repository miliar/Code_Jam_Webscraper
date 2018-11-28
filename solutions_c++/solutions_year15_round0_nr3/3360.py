#include<bits/stdc++.h>

using namespace std;

/* Number system being used is:
        -k  -j  -i  -1  1   i   j   k
        -4  -3  -2  -1  1   2   3   4
*/
const int ds[5][5] = {{1,1,1,1,1},
                      {1,1,2,3,4},
                      {1,1,-1,4,-3},
                      {1,3,-4,-1,2},
                      {1,4,3,-2,-1}};

int proc (char x) {
  switch(x) {
    case 'i': return 2;
    case 'j': return 3;
    case 'k': return 4;
  }
}

int pro (int a, int b) {
  if(a<0 && b>0) return - ds[abs(a)][b];
  else if(a<0 && b<0) return ds[abs(a)][abs(b)];
  else if(a>0 && b<0) return - ds[a][abs(b)];
  else return ds[a][b];
}

int main() {
  int t;
  string lx; // my string

  scanf("%d", &t);

  for (int i = 0; i < t; ++i) {
    int l;
    long long x;
    bool fi = false, fj = false, fk = false; // flags for i,j,k
    int temp=1;

    scanf("%d %lld", &l, &x);
    cin >> lx;

    printf("Case #%d: ", i+1);

    for(int j=0; j<x; j++) {
      for (int k=0; k<l; k++) {
        temp = pro(temp, proc(lx[k])); // temp = temp (*) lx[k]

        if(temp == 2 && !fi) {         // temp = i and fi = false
          fi = true; temp = 1;
        }

        if(temp == 3 && fi && !fj) {   // temp = j and fi = true and fj = false
          fj = true; temp = 1;
        }

        if(temp == 4 && fi && fj && !fk && (j==x-1 && k==l-1)) { // temp = k and fi,fj = true and fk = false
          fk = true; temp = 1;                                   // and last char of input string
        }
      }
    }

    lx.clear();

    if(fi && fj && fk) printf("YES\n");
    else printf("NO\n");
  }

  return 0;
}