#include<iostream>
#include<algorithm>
#define mul 100000
using namespace std;

int main()
{
	//freopen("D-large.in","r",stdin);
	//freopen("game.txt","w",stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;++tt)
	{
		int n;
		cin>>n;
		int naomi[n+1],ken[n+1],check[n+1];
		double d;
		for(int i=0;i<n;++i)
		{
			cin>>d;
			naomi[i]=d*mul;
		}
		for(int i=0;i<n;++i)
		{
			cin>>d;
			ken[i]=d*mul;
		}
		int count=0;
		sort(ken,ken+n);
		sort(naomi,naomi+n);
		for(int i=0;i<n;++i)
			check[i]=0;
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<n;++j)
			{
				if(check[j]==0 && naomi[j]>ken[i])
				{
					check[j]=1;
					++count;
					break;
				}
			}
		}
		cout<<"Case #"<<tt<<": "<<count<<" ";
		count=0;
		for(int i=0;i<n;++i)
			check[i]=0;
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<n;++j)
			{
				if(check[j]==0 && naomi[i]<ken[j])
				{
					check[j]=1;
					++count;
					break;
				}
			}
		}
		cout<<n-count<<endl;
	}
}
