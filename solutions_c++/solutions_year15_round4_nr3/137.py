#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cassert>
#include<string>
#include<map>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
map<string,int> mym;
int n;
int ind[21][1001];int ns;
string ts;
bool ise[20001],isf[20001];
void task()
{
	ns=0;
	cin>>n;
	char tc;
	mym.clear();
	memset(ind,0,sizeof ind);
	ns=0;
	rep(i,n)
	{
		while(true)
		{
			cin>>ts;
			if(mym[ts]==0)
			{
				mym[ts]=++ns;
			}
			//cout<<i<<","<<ind[i][0]<<":"<<ts<<","<<mym[ts]<<endl;
			ind[i][++ind[i][0]]=mym[ts];
			scanf("%c",&tc);
			if(tc!=' ')break;
		}
	}
	int nz=1<<n;
	int tot=99999999;
	rep2(iz,0,nz-1)
	{
		if((iz&1<<0)!=1||(iz&1<<1)!=0)continue;
		memset(ise,0,sizeof ise);
		memset(isf,0,sizeof isf);
		rep(i,n)
		{
			rep(j,ind[i][0])
			{
				if(1<<i-1&iz)ise[ind[i][j]]=true;else isf[ind[i][j]]=true;
			}
		}
		int tres=0;
		rep(is,ns)
		{
			if(ise[is]&&isf[is])++tres;
		}
		tot=min(tot,tres);
	}
	printf("%d\n",tot);
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(it,nt){printf("Case #%d: ",it);task();}
}
