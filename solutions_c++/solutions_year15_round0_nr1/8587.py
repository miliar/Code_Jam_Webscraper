#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
int main()
{
	freopen("A-large.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int t,tt=0;
	cin>>t;
	while(t--)
	{
		tt++;
		int n,req=0;
		cin>>n;
		//char ch;
		//cin>>ch;
		char s[1009];
		cin>>s;
		//cout<<s<<endl;
		int sum=s[0]-48;
		for(int i=1;i<=n;i++)
		{
			if(sum < i)
				{
					req+=i-sum;
					sum+=i-sum;
				}
			sum+=s[i]-48;
		}

		cout<<"Case #"<<tt<<": "<<req<<endl;
	}
}

