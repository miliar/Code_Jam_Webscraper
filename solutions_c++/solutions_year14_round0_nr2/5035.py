#include <iostream>
#include<cstdio>
using namespace std;
long double sid(long double c,long double f,long double x,long double k)
{
long double t1,t2;
t1=x/k;
t2=c/k;
if(t1<t2+x/(f+k))
return (t1);
return(t2+sid(c,f,x,k+f));
}
int main() {
	int t,p=0;
	long double c,f,x,ans;
	cin>>t;
	while(t--)
	{
	p++;
	cin>>c>>f>>x;
	ans=sid(c,f,x,2);
	printf("Case #%d: %.7Lf\n",p,ans);
	}
	return 0;
}
