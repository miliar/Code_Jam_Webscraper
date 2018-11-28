#include<iostream>
using namespace std;
int main(){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int t,smax,tek,ans,s;
	char c;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		tek=0;
		ans=0;
		cin>>smax;
		for(int j=0;j<=smax;j++)
		{
			cin>>c;
			s=c-'0';
			if(tek>=j||s==0)
			{
				tek+=s;
			}
			else
			{
				ans+=j-tek;
				tek=j;
				tek+=s;
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<"\n";
	}
	return 0;
}
