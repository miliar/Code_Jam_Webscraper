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

double res[(1<<20) + 5];
set<int> zb;
string s;
char t[25];
int n,q,z,r,i;

double jedz (int r) {
       if (zb.find(r) != zb.end()) return res[r];
       zb.insert(r);
       if (r == ((1<<n) - 1)) {
          res[r] = 0.0;
          return res[r];
       }
       int i,j,d,tab[20];
       res[r] = 0.0;
       for (i=0;i<n;i++) if ((1<<i) & r) {
           tab[i]=1; 
       }
       else {
            tab[i] = 0;
       }
       if (r == 0) {
          res[r] = n + jedz(1);
          return res[r];
       }
       i=0;
       while (tab[i]==1) i++;
       while (tab[i]==0) i = (i+1) % n;
       j = i;
       //printf("%d %d\n",r,n);
       while (1) {
             d = 1;
             while (tab[j]==1) {
                   d++;
                   j=(j+1)%n;
             }
             //printf(" %d %d\n",r,j);
             //printf(" %d %d\n",r,d);
             res[r] += (d*1.0/n) * ((2.0*n - d+1)/2 + jedz(r+(1<<j)));
             j=(j+1)%n;
             if (j==i) break;
       }
       //printf("%d %.3lf\n",r,res[r]);
       return res[r];
}

int main() {
scanf("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%s",t);
    s=t; n=s.size();
    r=0;
    for (i=0;i<n;i++) if (s[i]=='X') r+=(1<<i);
    zb.clear();
    printf("Case #%d: %.11lf\n",q,jedz(r));
}
return 0;
}
