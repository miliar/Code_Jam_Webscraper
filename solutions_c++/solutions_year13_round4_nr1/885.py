#include <stdio.h>
#include <algorithm>
using namespace std;
const long long int MOD=1000002013LL;
const int MAXM=1010;
int n,m;
struct bra
{
	int ver;
	int val,q;
};
bra pos[2*MAXM];
int p;
bool comp(bra a,bra b)
{
	if(a.val!=b.val) return a.val<b.val;
	return a.ver<b.ver;
}
bra pil[2*MAXM];
int f;
long long int faz(int a,int b)
{
	long long int i=b-a;
	long long int r=((n+n-i+1)*i)/2;
	return r;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int w=1;w<=t;w++)
	{
		scanf("%d %d",&n,&m);
		p=0;
		long long int res1=0;
		for(int i=1;i<=m;i++)
		{
			p++;
			pos[p].ver=0;
			pos[p+1].ver=1;
			scanf("%d %d %d",&pos[p].val,&pos[p+1].val,&pos[p].q);
			res1+=(pos[p].q*faz(pos[p].val,pos[p+1].val))%MOD;
			if(res1>=MOD) res1-=MOD;
			pos[p+1].q=pos[p].q;
			p++;
		}
		sort(&pos[1],&pos[p+1],comp);
		f=0;
		long long int res2=0;
		for(int i=1;i<=p;i++)
		{
			if(pos[i].ver==0)
			{
				f++;
				pil[f]=pos[i];
			}
			else
			{
				while(pos[i].q>0)
				{
					if(pos[i].q>=pil[f].q)
					{
						res2+=(faz(pil[f].val,pos[i].val)*pil[f].q)%MOD;
						if(res2>=MOD) res2-=MOD;
						pos[i].q-=pil[f].q;
						f--;
					}
					else
					{
						res2+=(faz(pil[f].val,pos[i].val)*pos[i].q)%MOD;
						if(res2>=MOD) res2-=MOD;
						pil[f].q-=pos[i].q;
						pos[i].q=0;
					}
				}
			}
		}
		printf("Case #%d: %lld\n",w,(res1-res2+2*MOD)%MOD);
	}
	return 0;
}
