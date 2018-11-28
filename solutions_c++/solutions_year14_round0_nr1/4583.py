#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>

using namespace std;

long long pp,i,j,k,l,m,n,a,b,s,c[55],t,d[2222][2222],e[1111],a1 = 0,a2 = 1;
vector <long long> p,q;
int main() {
  cin >>t;
  while (t --){
    cin >> a;
    a --;
    for (i = 0; i <4; i ++){
      for (j = 0; j < 4; j ++)
        cin >> d[i][j];
    }
    for (i  =0 ;i < 4; i ++)
      c[d[a][i]] = 1;
    cin >> a;
    a --;
    for (i = 0; i <4; i ++){
      for (j = 0; j < 4; j ++)
        cin >> d[i][j];
    }
    l = 0;
    for (i  =0 ;i < 4; i ++){
    	if (c[d[a][i]] == 1){
          l ++;
          b = d[a][i];
        }
    }
    pp ++;
    printf ("Case %lld: ",pp);
    if (l == 1) cout << b;
    if (l == 0) cout << "Volunteer cheated!";
    if (l > 1) cout << "Bad magician!";
    cout << endl;
    for (i = 0; i < 44; i ++)
      c[i] = 0;
  }
  
  return 0;
}
