#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long
#define lim 10000
#define N 32
#define M 500
bool isprime[lim+10];
ll List[lim+10];
int pcnt;
map<vector<int>,int> mapp;

vector<int> ans[1000];
vector<int> divs[1000];
void primegen()
{
	int i,j;
	pcnt=0;
	for(i=0;i<=lim;++i)
		isprime[i]=1;
	for(i=2;i<=lim;++i)
	{
		if(isprime[i])
		{
			List[pcnt++]=i;
			for(j=i;((long long)i)*j<=lim;++j)
				isprime[i*j]=0;
		}
	}

}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	ll pos,i,j,k;
	int n;
	sd(n);sd(n);sd(n);
	printf("Case #1:\n");
	primegen();
	for(pos=1;pos<=M;++pos)
	{
		while(true)
		{
			vector<int> v,d;
			v.clear();d.clear();
			v.PB(1);
			for(i=1;i<N-1;++i)
			{
				int num=rand()%2;
				v.PB(num);
			}
			v.PB(1);
			if(mapp[v])
				continue;
			mapp.erase(v);
			reverse(v.begin(),v.end());
			for(i=2;i<=10;++i)
			{
				for(j=0;j<pcnt;++j)
				{
					ll prod=1,s=0;
					for(k=0;k<N;++k)
					{
						if(v[k])
							s=(s+prod)%List[j];
						prod=(prod*i)%List[j];
					}
					if(s==0)
					{
						d.PB(List[j]);
						break;
					}
				}
				if(j==pcnt)
					break;
			}
			reverse(v.begin(),v.end());
			if(i<=10)
				continue;
			mapp[v]=pos;
			ans[pos]=v;
			for(i=0;i<9;++i)
				divs[pos].PB(d[i]);
			break;
		}
		//cerr<<pos<<'\n';
	}
	for(i=1;i<=M;++i)
	{
		for(j=0;j<N;++j)
			cout<<ans[i][j];
		for(j=0;j<9;++j)
			cout<<' '<<divs[i][j];
		cout<<'\n';
	}
}