#include<iostream>
#include<iomanip>
#include<vector>
using namespace std;
class cookie
{
public:
	void clean()
	{
		c=0.0;
		f=0.0;
		x=0.0;
		increment=2.0;
		previous=0.0;
		now=0.0;
		farmtotal=0.0;
		farm=0.0;
	}
	void input()
	{
		cin>>c>>f>>x;
	}
	void workflow()
	{
		previous=x/increment;
		while(true)	
		{
			farm=c/increment;
			farmtotal+=farm;
			increment+=f;
			now=farmtotal+(x/increment);
			if(now<previous)
			{
				previous=now;
			}
			else if(now>previous)
			{
				break;
			}
		}
		cout<<setprecision(7)<<fixed<<previous<<"\n";
	}
private:
	double c,f,x,increment,previous,now,farm,farmtotal;	
};
int main()
{
	int testcase;
	cin>>testcase;
	int c=1;
	cookie obj;
	while(testcase!=0)
	{
		testcase--;
		cout<<"Case #"<<c<<": ";
		c++;
		obj.clean();
		obj.input();
		obj.workflow();
	}
	return 0;
}
