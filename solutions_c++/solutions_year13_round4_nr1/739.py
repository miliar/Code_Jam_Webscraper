#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
const int N = 2005;
const int MOD = 1000002013;
typedef long long ll;
struct P
{
	int t,p,x;
}data[N];
bool cmp(int x,int y)
{
	if(data[x].x==data[y].x)return (data[x].t<data[y].t);
	return data[x].x<data[y].x;
}
int n,b[N],q[N],v[N];
int cal(int o,int e,int p)
{
	ll d=e-o-1;
	//printf("o:%d e:%d ret:%lld\n",o,e,(ll)p*(((d+1)*n-d*(d+1)/2)%MOD)%MOD);
	return (ll)p*(((d+1)*n-d*(d+1)/2)%MOD)%MOD;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,i,m,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		//printf("t:%d \n",T);
		int r2=0;
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)
		{
			int o,e,p;
			scanf("%d%d%d",&o,&e,&p);
			//printf("%d %d %d\n",o,e,p);
			r2=(r2+cal(o,e,p))%MOD;
			data[i+i].t=0;
			data[i+i].p=p;
			data[i+i].x=o;
			data[i+i+1].t=1;
			data[i+i+1].p=p;
			data[i+i+1].x=e;
		}
		//puts("what");
		//printf("r2:%d \n",r2);
		for(i=0;i<m+m;i++)b[i]=i;
		sort(b,b+m+m,cmp);
		int k=0;
		int r=0;
		//puts("here");
		for(i=0;i<m+m;i++)
		{
			//printf("i:%d \n",i);
			int h=b[i];
			//printf("t:%d x:%d p:%d \n",data[h].t,data[h].x,data[h].p);
			if(data[h].t==0)
			{
				q[k]=data[h].x;
				v[k]=data[h].p;
				k++;
			}
			else
			{
				int cnt=data[h].p,x=data[h].x;
				while(cnt)
				{
					if(v[k-1]>=cnt)
					{
						r=(r+cal(q[k-1],x,cnt))%MOD;
						v[k-1]-=cnt;
						cnt=0;
					}
					else
					{
						r=(r+cal(q[k-1],x,v[k-1]))%MOD;
						cnt-=v[k-1];
						k--;
						
					}
				}
			}
		}
		r=r2-r;
		if(r<0)r+=MOD;
		printf("Case #%d: ",ca++);
		cout << r << endl;
	}
	return 0;
}