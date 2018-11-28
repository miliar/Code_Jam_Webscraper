#include<iostream>
#include<cstring>
#include<cstdlib>
#include<set>
#include<cstdio>
using namespace std;


int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A1.out","w",stdout);
	int t;
	cin>>t;
	
	int q=0;
	while(t--)
	{
		
		q++;
		string s;
		int n;
		cin>>s>>n;
		int sum=0;
		int l=s.length();
		for(int i=0;i<=l-n+1;i++)
		{
			for(int j=n;j<=(l-i);j++)
			{
			string s2=s.substr(i,j);
			//cout<<s2<<endl;
			int flag;
			for(int k=0;k<=(s2.length()-n);k++)
			{
			string s3=s2.substr(k,n);
			//cout<<s3<<endl;
			unsigned found=s3.find_first_of("aeiou");
			flag=0;
			if(found!=std::string::npos)
			{
				continue;
			}
			else
			{
				flag=1;
				break;
			}
			}
		//	cout<<"kdjdkjdkjd"<<endl;
			if(flag==1)
			{
			//cout<<s2<<endl;
			sum++;
		}
		   }
		}
		cout<<"Case #"<<q<<": "<<sum<<endl;
		
		
	}
}
