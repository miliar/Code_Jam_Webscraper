#include<iostream>

using namespace std;

int main()
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int smax;
		cin>>smax;
		char s[smax+2];
		cin>>s;
		int it,sum=s[0]-'0',count=0;
		//cout<<count<<" "<<sum<<endl;
		for(it=1;it<smax+1;it++)
		{
			if(sum<it&&s[it]!='0')
			{
				count+=it-sum;
				
				sum+=it-sum;
			}
			sum+=s[it]-'0';
			//cout<<count<<" "<<sum<<endl;
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
