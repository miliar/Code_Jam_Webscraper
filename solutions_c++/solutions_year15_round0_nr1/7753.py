#include<iostream>
using namespace std;
int main()
{
	int test;
	cin>>test;
	int p = 1;
	while(test--)
	{
		int size;
		cin>>size;
		string a;
		cin>>a;
		int count=0,ans=0;
		count=count+a.at(0)-48;
		for(int i=1;i<a.length();i++)
		{
			if(count < i)
			{
				int hu = i - count;
				ans = ans + hu;
				count = count + hu;	
			}	
			count += a.at(i) - 48;
		}
		cout<<"Case #"<<p<<": "<<ans<<endl;
		p++;
	}
	return 0;
}
