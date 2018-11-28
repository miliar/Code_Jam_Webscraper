#include<iostream>

using namespace std;

int main()

{

int t,j;

double c,f,x,r;

double ans;

scanf("%d",&t);

for(j=1;j<=t;j++)

{

ans=0.0;

scanf("%lf %lf %lf",&c,&f,&x);

r=2.0;

while((c/r)+(x/(r+f))<(x/r))

{

ans+=c/r;

r+=f;

}

ans+=x/r;

printf("Case #%d: %0.7lf\n",j,ans);

}

return 0;

}