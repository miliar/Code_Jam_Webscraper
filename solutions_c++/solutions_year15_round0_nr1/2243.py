#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("A-large.in");
	cout.open("A-large-output.txt");
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		long long n,j;
		cin>>n;
		string s;
		long long a[n+5];
		cin>>s;
		for(j=0;j<=n;j++)
		{
			a[j]=s[j]-'0';
		}
		long long ans=0,temp=a[0],x;
		for(j=1;j<=n;j++)
		{
			if(temp<j)
			{
				if(a[j]!=0)
				{
					x=j-temp;
					ans+=x;
					temp+=x;
				}
			}
			temp+=a[j];
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
