#include <cstdio>
#include <cmath>
#include <map>
using namespace std;
int t,n,x,y;
map<int,long double> facto;
long double fact(int k){if(facto[k]!=0) {return facto[k];} long double 
ans=1.;for(int i=1;i<=k;i++)ans*=(long double)i; facto[k]=ans;return ans;}
long double choose(int k, int nn){return fact(nn)/(fact(k)*fact(nn-k));}

int main(){
scanf("%d", &t);

for(int cas=1;cas<=t;cas++){
scanf("%d %d %d", &n, &x,&y);
x=max(x,0-x);
double nn= (double) n;
int largeur =floor((-3.+sqrt(9.+8.*(n-1)))/4);
n=n-(2*largeur+1)*(largeur+1);
if(x+y<=2*largeur or (x+y==2*largeur+2 and n>y+2+2*largeur)) 
printf("Case #%d: 1.0\n",cas);
else if (x+y>2*largeur+2 or y>n or (x==0 and y==2*largeur+2)) printf("Case #%d: 0.0\n",cas);
else { long double ans = 0;
for(int i=0;i<=n-y-1;i++) ans+= choose(i,n);
for(int i=0;i<n;i++) ans/=2.;
printf("Case #%d: %.8Lf\n",cas,ans);}
}
return 0;
}

