#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const char C[3]={'P','R','S'};
int S[4096];
int A[3],B[3];
int N;
bool cmp(int l,int r)
{
	int i,mid,size;
	mid=(l+r)/2; size=(r-l+1)/2;
	for (i=l;i<=mid;i++)
	{
		if (S[i]>S[i+size]) return true;
		if (S[i]<S[i+size]) return false;
	}
	return false;
}
void rearrange(int l,int r)
{
	int i,mid,size;
	if (l==r) return;
	mid=(l+r)/2; size=(r-l+1)/2;
	rearrange(l,mid); rearrange(mid+1,r);
	if (cmp(l,r))
		for (i=l;i<=mid;i++) swap(S[i],S[i+size]);
}
int main()
{
	int i,j,k,T,_T;
	bool flag;
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for (_T=1;_T<=T;_T++)
	{
		printf("Case #%d: ",_T);
		scanf("%d%d%d%d",&N,&A[1],&A[0],&A[2]);
		flag=false;
		for (i=0;i<=2;i++)
		{
			S[0]=i;
			for (j=0;j<=N-1;j++)
				for (k=0;k<=(1<<j)-1;k++) S[k+(1<<j)]=(S[k]+1)%3;
			memset(B,0,sizeof(B));
			for (j=0;j<=(1<<N)-1;j++) B[S[j]]++;
			if ((B[0]==A[0])&&(B[1]==A[1])&&(B[2]==A[2]))
			{
				flag=true;
				rearrange(0,(1<<N)-1);
				for (j=0;j<=(1<<N)-1;j++) printf("%c",C[S[j]]);
			}
		}
		if (!flag) printf("IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}
