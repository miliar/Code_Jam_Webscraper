#include<iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		int s,ans=0;
		string S;
		cin>>s>>S;
		int count=(int)(S[0]-'0');
		//cout<<count<<endl;
		for(int j=1;j<=s;j++)
		{
			int t=0,k=(S[j]-'0');
			//cout<<k<<endl;
			if(j>count) 
				t=j-count;
			count+=(k+t);
			ans+=t;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	} 
	return 0;
}
