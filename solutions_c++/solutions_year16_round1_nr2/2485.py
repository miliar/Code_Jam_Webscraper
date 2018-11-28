#include<bits/stdc++.h>
#define ll long long
#define endl '\n'
#define max 1000000
using namespace std;
int visited[3000],store[3000],ans[3000];
map<int,int> m;
int main()
{
	ios_base::sync_with_stdio(false);
	freopen("B-small-attempt1.in","r",stdin);
    freopen("output.txt","w+",stdout);
	int coun=1,t;
	cin>>t;
	int k;
	while(coun<=t)
	{
		memset(visited,0,sizeof(visited));
		int n;
		cin>>n;
		int c=1;
		for(int i=1;i<=2*n-1;i++)
		{
			for(int j=1;j<=n;j++)
			{
				cin>>k;
				store[c]=k;
				m[k]++;
				c++;
			}
		}
		cout<<"Case #"<<coun<<": ";
		int co=0;
		for(int i=1;i<c;i++)
		{
		if(visited[store[i]]==0)
		{
			if(m[store[i]]%2!=0)
			{
				ans[co]=store[i];
				co++;
				visited[store[i]]=1;
			}
		}	
		}
		sort(ans,ans+co);
		for(int i=0;i<co;i++)
		cout<<ans[i]<<" ";
		cout<<endl;
		coun++;
		m.clear();
	}
}
