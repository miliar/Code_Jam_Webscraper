#include<bits/stdc++.h>


#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long int
#define MOD 1000000007

using namespace std; 

vector<pair<int,int> > V;
int A[26];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int sum=0;
		for(i=0;i<26;i++)
			A[i]=0;
		int n;
		cin>>n;
		for(i=0;i<n;i++)
		{
			scanf("%d",A+i);
		}
		printf("Case #%d: ",k);
		while(true)
		{
			sum=0;
			for(i=0;i<n;i++)
				sum+=A[i];
			if(sum==3)
			{
				int ans=-1;
				bool flag=true;
				for(i=0;i<n;i++)
				{
					if(A[i]==2)
					{
						printf("%c ",(char)('A'+i));
						A[i]-=1;
						flag=false;
						break;
					}
					if(A[i]==1)
						ans=i;
				}
				if(flag)
				{
					printf("%c ",(char)('A'+ans));
					A[ans]--;
				}
				sum--;
				continue;
			}
			if(sum==2)
			{
				int c=1;
				for(i=0;i<n;i++)
				{
					if(A[i]&&c==2)
					{
						printf("%c",(char)('A'+i));
						A[i]-=1;
						break;
					}
					if(A[i])
					{
						printf("%c",(char)('A'+i));
						A[i]-=1;
						c++;
					}
				}
				sum=0;
				break;
			}
			V.clear();
			for(i=0;i<n;i++)
			{
				V.pb(mp(A[i],i));
			}
			sort(V.begin(),V.end());
			if(V[n-1].f==V[n-2].f)
			{
				printf("%c%c ",(char)('A'+V[n-1].s),(char)('A'+V[n-2].s));
				A[V[n-1].s]--;
				A[V[n-2].s]--;
				sum-=2;
			}
			else
			{
				printf("%c ",(char)('A'+V[n-1].s));
				A[V[n-1].s]--;
				sum--;
			}
		}
		cout<<endl;
	}
	return 0;
}
