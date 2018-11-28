#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		int a;
		cin>>a;
		string b;
		cin>>b;
		int s=0,m=0;
		for(int i=0;i<=a;i++)
		{
			int x = b[i] - '0';
			if(s<i)
			{
				m+=(i-s);
				s+=(i-s);
			}
			s+=x;
		}
		cout<<"Case #"<<j+1<<": "<<m<<endl;
	}
	return 0;
}
