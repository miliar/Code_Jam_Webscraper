#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
	int test;
	cin>>test;
	int c=0;
	while(test--)
	{
		c++;
		int a,b;
		cin>>a>>b;
		int count=0;
		if(a<=1 && b>=1)
		{
			count++;
			//cout<<"1\n";
		}
		if(a<=4 && b>=4)
		{
			count++;
			//cout<<"4\n";
		}
		if(a<=9 && b>=9)
		{
			count++;
			//cout<<"9\n";
		}
		if(a<=121 && b>=121)
		{
			count++;
			//cout<<"121\n";
		}
		if(a<=484 && b>=484)
		{
			count++;
		}
		cout<<"Case #"<<c<<": "<<count<<endl;
	}
	return 0;
}

