#include<bits/stdc++.h>
#define ll long long 
#define pb push_back
#define mp make_pair
#define si(i) scanf("%d",&i)
#define fs first
#define sc second
#define pii pair<int,int>
#define psi pair<string,int>
#define FOR(i,j,k) for(int i=j;i<k;i++)
#define REP(i,k) for(int i=0;i<k;i++)
#define FORR(i,j,k) for(int i=n;i>=k;i--)
#define MOD 1000000007
#define sll(i) scanf("%lld",&i)
using namespace std;
int main()
{

	int t;
	scanf("%d",&t);
	int t1=0;
	while(t--)
	{t1++;
		int n;
		scanf("%d",&n);
		int arr[100];
		int vis[30];
		for(int i=0;i<27;i++)vis[i] = 0;int c=0;
		for(int i=0;i<n;i++) { scanf("%d",&arr[i]); c+=arr[i];}
			printf("Case #%d: ",t1);
		while(1)
		{	if(c<=0)break;
			int ma = 0,ma2=0,id;int x=0,id2=0,f3=0;
			for(int i=0;i<n;i++)
			{
				if(arr[i]>ma)
				{
					ma = arr[i];
					id = i;f3=-1;
				}
				else if(arr[i]==ma && f3==-1){id2=i;f3=1;}
				if(arr[i]) x+=arr[i];

			}
			
			if(x==2 )
				 {
				int p=2;int x3=0;
				for(int i=0;i<n;i++)
				{
					if(arr[i]>0){ printf("%c",65+i);arr[i]--;x3++;}
					if(x3==2)
						break;
				}
				printf(" ");c-=2;
			}
			else if(f3==1 && x!=3)
			{
				printf("%c%c ",65+id,65+id2);
				arr[id]--;arr[id2]--;c-=2;
			}
			else 
			{
				printf("%c ",65+id);
				arr[id]--;c--;
			}
			
	}
	
	printf("\n");
}
	return 0;
}