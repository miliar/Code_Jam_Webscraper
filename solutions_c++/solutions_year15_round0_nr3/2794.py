#include<cstdio>
#include<cstring>
#include<algorithm>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;

const int maxn=10010;

int L,K,a[maxn],b[maxn],q1[maxn],q2[maxn],g[6][6],w[6][6];
char s[maxn];

void init()
{
	scanf("%d%d",&L,&K);
	scanf("%s",s+1);
}

void solve()
{
	int now,len,tail1,tail2;
	now=0;
	fou(i,1,L){
		if (s[i]=='i') a[i]=2;
		if (s[i]=='j') a[i]=3;
		if (s[i]=='k') a[i]=4;
	}
	fou(j,1,K-1){
		now+=L;
		fou(i,now+1,now+L) a[i]=a[i-now];
	}
	
	len=L*K;
	
	b[1]=a[1];
	fou(i,2,len)
		if (b[i-1]>0) b[i]=g[b[i-1]][a[i]];
		else b[i]=-g[-b[i-1]][a[i]];
	
	tail1=tail2=0;
	
	if (a[1]==2) q1[++tail1]=1;
	now=a[1];
	fou(i,2,len){
		if (now>0) now=g[now][a[i]];
		else now=-g[-now][a[i]];
		if (now==2) q1[++tail1]=i;
	}
	
	if (a[len]==4) q2[++tail2]=len;
	now=a[len];
	fod(i,len-1,1){
		if (now>0) now=g[a[i]][now];
		else now=-g[a[i]][-now];
		if (now==4) q2[++tail2]=i;
	}
	
	fou(i,1,tail1)
		fou(j,1,tail2){
			if (q1[i]+1>q2[j]-1) break;
			if (b[q1[i]]>0){
				if (b[q2[j]-1]>0) now=w[b[q2[j]-1]][b[q1[i]]];
				else now=-w[-b[q2[j]-1]][b[q1[i]]];
			}else
			{
				if (b[q2[j]-1]>0) now=-w[b[q2[j]-1]][-b[q1[i]]];
				else now=w[-b[q2[j]-1]][-b[q1[i]]];
			}
			if (now==3){
				printf("YES\n");
				return;
			}
		}
	printf("NO\n");
}

int main()
{
	fou(i,1,4) g[i][1]=g[1][i]=i;
	fou(i,2,4) g[i][i]=-1;
	g[2][3]=4;g[3][2]=-4;
	g[2][4]=-3;g[4][2]=3;
	g[3][4]=2;g[4][3]=-2;
	
	fou(i,1,4) w[i][1]=i;
	fou(i,2,4) w[1][i]=-i;
	fou(i,1,4) w[i][i]=1;
	w[2][3]=4;w[3][2]=-4;
	w[2][4]=-3;w[4][2]=3;
	w[3][4]=2;w[4][3]=-2;
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
