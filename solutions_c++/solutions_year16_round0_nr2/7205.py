#include<iostream>
#include<vector>
#include<string>
using namespace std;


int main()
{
	int t;
	string n;
	cin>>t;
	int case1=0;
	while(t-->0)
	{
		case1++;
		
		cin>>n;
		vector<int> hash(n.length(),0);
		int flag=0;
		/*if(n.find("-")==-1)
		{
				cout<<"Case #"<<case1<<": "<<0<<endl;
				continue;
		}*/
		int i=0;
		for(i=0;i<n.length();i++)
		{
			if(i==0)
			{
				if(n[i]=='-')
					hash[i]=1;
				continue;
			}
			if(n[i]=='+'||n[i]=='-'&&n[i-1]=='-')
			{
				hash[i]=hash[i-1];
				continue;
			}
			if(n[i]=='-'&&n[i-1]=='+')
			{
				hash[i]=hash[i-1]+2;
				continue;
			}

		}
		cout<<"Case #"<<case1<<": "<<hash[i-1]<<endl;
	}
}