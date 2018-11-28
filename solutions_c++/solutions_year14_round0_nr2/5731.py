#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

double solve(double x,double c,double f)
{
double cur=x/2,next,r=2.0,temp=0.0;
temp=c/r;
next=x/(r+f)+temp;
r+=f;
while(cur-next>1e-7)
{
 cur=next;
 temp+=c/r;
 next=x/(r+f)+temp;
 r+=f;
}
return cur;

}

int main()
{
freopen("in2.txt","r",stdin);
freopen("out2.txt","w",stdout);

double x,c,f,ans;
int t,test;
cin>>t;
for(test=1;test<=t;test++)
{
cin>>c>>f>>x;
ans=solve(x,c,f);
cout<<"Case #"<<test<<": ";
printf("%.7lf\n",ans);

}
return 0;
}

