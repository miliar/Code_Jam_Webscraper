#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

const int ONE = 1;
const int I = 2;
const int J = 3;
const int K = 4;

int multi[5][5] = {{},
                   {0, ONE,    I,    J,    K},
                   {0,   I, -ONE,    K,   -J},
                   {0,   J,   -K, -ONE,    I},
                   {0,   K,    J,   -I, -ONE}};


int f(int a, int b){
  int sig = 1;

  if(a < 0){
    sig *= -1;
  }

  if(b < 0){
    sig *= -1;
  }

  int c = sig * multi[abs(a)][abs(b)];
  return c;
}

pair<int,int> next(int l, pair<int, int> p){
  p.second++;
  if(p.second == l){
    p.second = 0;
    p.first++;
  }
  return p;
}

bool ismiddle(int l, long long x, pair<int,int> &a, pair<int,int> &b, vector<int> &left, vector<int> &right, vector<vector<int> > &mid){
  int value;
  if(a.first == x - 1 - b.first){
    value = mid[a.second][l - 1 - b.second];
  }else{
    int m = x - (a.first + b.first + 2);
    m = m % 4;

    value = right[a.second];
    for(int k = 0; k < m; ++k){
      value = f(value, left[l - 1]);
    }
    value = f(value, left[l - 1 - b.second]);
  }
  
  return value == J;
}

int main(){ IO;
  int t;
  cin >> t;

  for(int ncase = 1; ncase <= t; ++ncase){
    int l;
    long long x;
    string s;
    cin >> l >> x >> s;

    vector<int> left;
    vector<pair<int,int> > vI;
    int value = ONE;
    for(int k = 0; k < 4; ++k){
      for(int i = 0; i < s.size(); ++i){
	value = f(value, s[i] - 'i' + I);
	if(k == 0){
	  left.push_back(value);
	}
	if(value == I){
	  vI.push_back(make_pair(k, i));
	}
      }
    }

    vector<vector<int> > mid(l, vector<int>(l));
    vector<int> right;
    vector<pair<int,int> > vK;

    for(int k = 0; k < 4; ++k){
      for(int i = 0; i < l; ++i){
	int value = ONE;
	for(int k2 = k; k2 < 4; ++k2){
	  for(int i2 = 0; i2 < l; ++i2){
	    if(k2 > k or i2 >= i){
	      value = f(value, s[i2] - 'i' + I);
	      if(k == 3){
		mid[i][i2] = value;
	      }
	    }
	  }
	}
	if(k == 3){
	  right.push_back(value);
	}
	if(value == K){
	  vK.push_back(make_pair(3 - k, l - 1 - i));
	}
      }
    }

    string ans = "NO";
    for(int i = 0; i < vI.size(); ++i){
      for(int j = 0; j < vK.size(); ++j){
        long long int len = l * (vI[i].first + vK[j].first);
        len += vI[i].second + vK[j].second + 2;

        pair<int,int> a = next(l, vI[i]);
        pair<int,int> b = next(l, vK[j]);

        if(len < x * l and ismiddle(l, x, a, b, left, right, mid)){
          ans = "YES";
        }
      }
    }

    cout << "Case #" << ncase << ": " << ans << endl;
  }

  return 0;
}
