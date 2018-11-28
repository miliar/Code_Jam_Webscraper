#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<iomanip>
#include<fstream>
#include<ctime>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair <int,int> ii;
typedef long long LL;
#define pb push_back
const int INF = 2147483647;
const int MOD = 1000002013;
const int M = 2005;

int z,q,i,j,n,m,poww,a[M],b[M],p[M],czas[M],zm,ci,ind,d;
LL add[M],c,minn,akt;
set<int> wyd;
set<int>::iterator it;

LL suma (int a) {
   //cout << "suma " << a << endl;
   return (a*1LL*(a+1))/2;
}

int main() {
scanf("%d",&z);
for (q=1;q<=z;q++) {
    scanf("%d %d",&n,&m);
    for (i=0;i<=2*m;i++) add[i] = 0;
    poww = 0;
    wyd.clear();
    for (i=0;i<m;i++) {
        scanf ("%d %d %d",&a[i],&b[i],&p[i]);
        a[i]--; b[i]--;
        wyd.insert(a[i]);
        wyd.insert(b[i]);
        poww = ((suma(b[i]-a[i]-1) % MOD) * p[i]  + poww) % MOD;
    }
    d = 0;
    for (it = wyd.begin();it!=wyd.end();it++) czas[d++] = *it;
    for (i=0;i<m;i++) for (j=0;j<d;j++) {
        if (a[i]==czas[j]) add[j]+=p[i];
        if (b[i]==czas[j]) add[j]-=p[i];
    }
    //for (i=0;i<d;i++) cout << czas[i] << " " << add[i] << endl;
    akt = 0;
    while (1) {
          zm = 0; c = 0; ci = 0;
          for (i=0;i<d;i++) {
              c += add[i];
              if (c > 0 && ci == 0) {
                 ind = i;
                 ci = 1;
                 minn = c;
              }
              else if (c == 0 && ci == 1) {
                 //cout << c << " " << minn << " " << i << " " << ind << endl;  
                 akt = ((minn % MOD) * (suma(czas[i]-czas[ind]-1) % MOD) + akt) % MOD;
                 ci = 0;
                 add[ind] -= minn;
                 add[i] += minn;
                 //for (j=ind;j<=i;j++) add[j] -= minn;
                 zm = 1;
              }
              else if (ci == 1) minn = min(minn,c);
          }
          if (zm == 0) break;
    }
    cout << "Case #" << q << ": " << (akt + MOD - poww) % MOD << endl;
}
return 0;
}
