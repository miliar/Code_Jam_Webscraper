#include <iostream>
#include<string>
using namespace std;

int main() 
{
	int t;
	cin>>t;
	int j=1;
	for(j=1;j<=t;j++)
	{
		int n,f=0;
		//cin>>n;
		int s=0;
		int k=0;
		char s1[10000];
		cin>>n>>s1;
	//	cout<<s1<<endl;
	if(s1[0]-48>=n)
	{
		cout<<"Case #"<<j<<": 0"<<endl;
		continue;
	}
	s=s1[0]-48;
		for(int i=1;i<=n;i++)
		{
			if(s<i)
			{
				int x=i-s;
				k+=(i-s);
				s+=x;
			}
			s+=s1[i]-48;
		}
		
		cout<<"Case #"<<j<<": "<<k<<endl;
	
		
	}
	return 0;
}
