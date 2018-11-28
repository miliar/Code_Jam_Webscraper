#include<climits>
#include<cstdio>
#include<cstring>
typedef long long ll;

const int NMAX=10000;

int E,R,N; 
struct {int v,l,r;} CT[1+NMAX];

static inline ll max(ll a,ll b) {return a<b?b:a;}
static inline ll min(ll a,ll b) {return a<b?a:b;}

ll solve(int m,int l,int r,ll exh,ll ext)
{
	const ll pre=exh+(ll)(m-l)*R;
	const ll pst=(ll)(r-m+1)*R;
	const ll the=min(pre,E)-max(ext-pst,0);
//fprintf(stderr,"solve %d:[%d,%d] ext=%lld the=%lld pre=%lld pst=%lld\n",m,l,r,ext,the,pre,pst);
	ll ret=the*CT[m].v;
	if(CT[m].l>=0)ret+=solve(CT[m].l,l,m-1,exh,the+max(ext-pst,0));
	if(CT[m].r>=0)ret+=solve(CT[m].r,m+1,r,min(min(pre,E)-the+R,E),ext);
	return ret;
}

ll A,rec[2+10][1+5];int use[1+10];
void dfs(int Enow,int dep,ll Gnow)
{
	if(dep>N)
	{
		if(Gnow>A)
		{
			A=Gnow;
			for(int i=1;i<=N;i++)printf("[%d] ",use[i]);
			putchar('\n');
		}
		return;
	}
	if(Gnow<=rec[dep][Enow])return;
	rec[dep][Enow]=Gnow;
	for(int i=0;i<=Enow;i++)
	{
		use[dep]=i;
		dfs(min(Enow-i+R,E),dep+1,Gnow+i*(ll)CT[dep].v);
	}
}

ll solve()
{
//#define SMALL
#ifdef SMALL
	A=0;
	memset(rec,0xFF,sizeof(rec));
	dfs(E,1,0);
	return A;
#else
	return solve(CT[0].r,1,N,E,0);
#endif
}

void input()
{
	static int s[1+NMAX];
	int sp=0;
	scanf("%d%d%d",&E,&R,&N);
	CT[0].v=INT_MAX;
	CT[0].l=-1;
	CT[0].r=-1;
	s[sp++]=0;
	for(int i=1;i<=N;i++)
	{
		scanf("%d",&CT[i].v);
		while(CT[s[sp-1]].v<CT[i].v)sp--;
		const int j=s[sp-1];
		CT[i].l=CT[j].r;
		CT[j].r=i;
		CT[i].r=-1;
		s[sp++]=i;
	}
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		input();
		printf("Case #%d: %lld\n",i,solve());
	}
	return 0;
}
