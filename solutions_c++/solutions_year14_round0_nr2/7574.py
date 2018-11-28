#include <iostream>
#include <iomanip>
using namespace std;
void work(double);
double c,f,x,r=2.0;
int main()
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		r = 2.0;
		cin>>c>>f>>x;
		cout<<"Case #"<<i<<": ";
		work(0);
		cout<<endl;
	}
	return 0;
}

void work(double t)
{
	double tx,t1,t2;
	tx = t+(c/r);
	t1 = t+(x/r);
	t2 = t+(c/r)+(x/(r+f));
	if(t1>t2)
	{
		r += f;
		work(tx);
	}
	else
	{
		cout<<setiosflags(ios::fixed)<<setprecision(7)<<t1;
	}
}