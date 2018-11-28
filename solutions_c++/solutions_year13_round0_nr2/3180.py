#include <cstdio>
#include <algorithm>
//soit tu es le + gd sur ta ligne; soit sur ta colonne
using namespace std;

int t,m,n;
int main(){
scanf("%d",&t);
for(int i=0;i<t;i++){
scanf("%d %d", &n, &m);
int tab[n][m];
int mn[n];
int mm[m];

for(int j=0;j<n;j++)for(int k=0;k<m;k++)scanf("%d",&(tab[j][k]));


for(int j=0;j<n;j++){mn[j]=0;
for(int k=0;k<m;k++)mn[j]=max(mn[j],tab[j][k]);
}

for(int j=0;j<m;j++){mm[j]=0;
for(int k=0;k<n;k++)mm[j]=max(mm[j],tab[k][j]);
}
bool yes=true;
for(int j=0;j<n;j++){for(int k=0;k<m;k++)yes=yes && (tab[j][k]==mn[j] || tab[j][k]==mm[k] );}

printf("Case #%d: %s\n",i+1,yes?"YES":"NO");
}
return 0;
}

