#include<iostream> 
#include<string> 
#include<queue> 
#include<algorithm> 
#include<cstdio> 
#include<vector> 
#include<queue> 
#include<climits> 
#include<cstring> 
#include<ctime>
#include<cstdlib>
using namespace std; 
int num[1005];

int main()
{
	freopen("d://output.txt","w",stdout);
	freopen("d://B-large.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		int n;
		int ans=INT_MAX;
		int maxed=-1;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&num[i]);
			if(maxed<num[i]) maxed=num[i];
		}
		for(int i=1;i<=maxed;i++)
		{
			int tem=i;
			for(int j=0;j<n;j++)
			{
				if(num[j]<=i) continue;
				if(num[j]%i!=0)
				{
					tem+=(num[j]/i);
				}
				else tem+=(num[j]/i-1);
			}
			if(tem<ans) ans=tem;
		}

		printf("Case #%d: %d\n",Case,ans);
	}
}

