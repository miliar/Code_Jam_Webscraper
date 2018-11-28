#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define INF 0x3f3f3f3f
typedef long long LL;
char A[200];
int L[200][2];
int R[200][2];
int main()
{
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);
	int t,case1=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",A+1);
		int l=strlen(A+1);
		int i,j,k;
		memset(L,0,sizeof L);
		memset(R,0,sizeof R);
		if(A[1]=='+')
			L[1][0]=1;
		else L[1][1]=1;
		for(i=2;i<=l;i++)
		{
			if(A[i]==A[i-1])
			{
				L[i][1]=L[i-1][1];
				L[i][0]=L[i-1][0];
			}
			else
			{
				L[i][1]=L[i-1][0]+1;
				L[i][0]=L[i-1][1]+1;
			}
		}
		while(l)
		{
			if(A[l]=='-')
			break;
			l--;
		}
		if(l==0)
			A[++l]='+';	
		if(A[l]=='+')
			R[l][0]=1;
		else R[l][1]=1;
		for(i=l-1;i>0;i--)
		{
			if(A[i]==A[i+1])
			{
				R[i][1]=R[i+1][1];
			
				R[i][0]=R[i+1][0];
			}
			else 
			{
				R[i][1]=R[i+1][0]+1;
				R[i][0]=R[i+1][1]+1;
			}
		}
		int ans=L[l][1];
//		cout<<ans<<" "<<l<<endl;
		for(i=1;i<=l;i++)
		{
			ans=min(ans,L[i-1][0]+R[i][0]+1);
		}
		printf("Case #%d: %d\n",++case1,ans);
	}
	return 0;
}
