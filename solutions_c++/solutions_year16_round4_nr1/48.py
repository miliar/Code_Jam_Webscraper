#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
char res[16384];
string tdp[13][256];
int n,nz,nr,np,ns;
bool solve(char i1)
{
	memset(res,0,sizeof res);
	strcpy(res+1,tdp[n][i1].c_str());
	//cout<<n<<","<<i1<<":"<<res+1<<endl;
	int tct[256]={};
	for(int i=1;i<=nz;++i)
	{
		tct[res[i]]++;
	}
	if(tct['P']==np&&tct['R']==nr&&tct['S']==ns)
	{
		printf("%s\n",res+1);
		return true;
	}
	return false;
}
void task()
{
	scanf("%d%d%d%d",&n,&nr,&np,&ns);
	nz=1<<n;
	if(!solve('P')&&!solve('R')&&!solve('S'))
	{
		printf("IMPOSSIBLE\n");
	}
}
int main()
{
	tdp[0]['R']="R";
	tdp[0]['S']="S";
	tdp[0]['P']="P";
	for(int i=1;i<=12;++i)
	{
		#define min(a,b) a>b?b:a
		tdp[i]['R']=min(tdp[i-1]['R']+tdp[i-1]['S'],tdp[i-1]['S']+tdp[i-1]['R']);
		tdp[i]['S']=min(tdp[i-1]['P']+tdp[i-1]['S'],tdp[i-1]['S']+tdp[i-1]['P']);
		tdp[i]['P']=min(tdp[i-1]['P']+tdp[i-1]['R'],tdp[i-1]['R']+tdp[i-1]['P']);
	}
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt)
	{
		printf("Case #%d: ",i);
		task();
	}
}
