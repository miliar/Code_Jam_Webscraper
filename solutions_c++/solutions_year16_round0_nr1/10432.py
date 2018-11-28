#include <iostream>
#include <set>
using namespace std;

int dyn_prog(int val,set<int> &s,int i)
{
	int r;
	int val1=val*i;
	int val2=val1;
	if(val1==0)
	{
		return -1;
	}
	else
	{	
		while(val1!=0)
		{
			r=val1%10;
			s.insert(r);
			val1/=10;
		}
		if(s.size()==10)
		{
			return val2;	
		}
		else
		{
			return dyn_prog(val,s,i+1);
		}
	}
	 
}

int main()
{
	int test,val,res;
	cin>>test;
	int i=0;
	set<int> s;
	while(i<test)
	{
		cin>>val;
		res=dyn_prog(val,s,1);
		if(res==-1)
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		else
			cout<<"Case #"<<i+1<<": "<<res<<endl;
		s.clear();
		i++;
	}
}


