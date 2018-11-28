#include <iostream>
using namespace std;
double finc(double c,double f,double x,double k)
{
double t1,t2;
t1=x/k;
t2=c/k;
if(t1<t2+x/(f+k))
return (t1);
return(t2+finc(c,f,x,k+f));
}
int main() {
	int t,p=0;
	double c,f,x,ans;
	cin>>t;
	while(t--)
	{
	p++;
	cin>>c>>f>>x;
	ans=finc(c,f,x,2);
	printf("Case #%d: %.7lf\n",p,ans);
	}
	return 0;
}