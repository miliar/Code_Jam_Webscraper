#include <bits/stdc++.h>
using namespace std;
#define pb(y) push_back(y)
typedef long long ll ;

void solve()
{

	int n , m ,map[10],check[10],max_t,tot;
	string A[10];
	int size[100];
	memset(size , 0 , sizeof size);
	scanf("%d%d",&m,&n);
	for(int =0;i<m;i++)
		cin >> A[i];
	for(int i = 0 ; i < 1<<16 ;i++ )
	{
		int curr = i;
		for(int j = 0 ;j<8;j++)
		{
			map[j]=curr%4;
			curr>>2;
		}
		int flag =1;
		for(int j= 0;j<m;j++)
		{
			if(map[j]>=n)
			{
				flag =0;
				break;
			}
		}
		memset(check , 0 , sizeof check);
		for(int j =0;j<m;j++)
		{
			if(check[map[j]]++);
		}
		for(int j =0;j<n;j++)
		{
			if(check[j]<=0)
			{
				falg=0;
				break;
			}
		}
		if(!flag)continue;
		set <string> S;
		for(int j=0;j<m;j++)
		{
			for(int k = 0 ;k<A[j].size();k++)
			{
				 S.insert(A[j]);
			}
		}
		size[S.size()]++;
	}
	max_t = 0;
	for(int i=0;i<100;i++)
	{
		if(size[i])
		{
			max_t=i;
		}
	}
	printf("%d %d",max_t,size[max_t];)
}
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}