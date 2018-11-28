#include<bits/stdc++.h>
#define ll long long
#define MOD 1000000007
#define MAX 2000007

using namespace std;

int a[200][200],cnt[3000];
int main()
{
	int tc,test,n,i,j,maxi;
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>tc;
	maxi = 2600;
	for(test = 1 ; test <= tc;test++)
	{
		cout<<"Case #"<<test<<": ";
		cin>>n;
		for(i=0;i<maxi;i++)
		cnt[i] = 0;
		for(i=0;i<2*n-1;i++)
		{
			for(j=0;j<n;j++)
			{
				cin>>a[i][j];
				cnt[a[i][j]]++;
			}
		}
		for(i=0;i<maxi;i++)
		{
			if(cnt[i] > 0 && cnt[i]%2 == 1)
			cout<<i<<" ";
		}
		cout<<"\n";
		
	}
	return 0;
}
