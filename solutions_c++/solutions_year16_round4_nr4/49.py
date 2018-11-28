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
int n;
int ind[26][26];
bool visitx[26],visity[26];
bool visit[26][26];
int tcx,tcy,tcc;
void dfs(int ix,int iy)
{
	if(!visitx[ix])
	{
		visitx[ix]=true;
		++tcx;
	}
	if(!visity[iy])
	{
		visity[iy]=true;
		++tcy;
	}
	visit[ix][iy]=true;
	++tcc;
	rep(ty,n)
	{
		if(visit[ix][ty])continue;
		if(ind[ix][ty]==1)
		{
			dfs(ix,ty);
		}
	}
	rep(tx,n)
	{
		if(visit[tx][iy])continue;
		if(ind[tx][iy]==1)
		{
			dfs(tx,iy);
		}
	}
}
int ibx[17],iby[17];int nb;
int ibc[17];
int tax,tay;
int tdp[1<<16][26][26];
int res;
void pushblock(int ix,int iy,int ic)
{
	//cout<<"Push:"<<ix<<","<<iy<<","<<ic<<endl;
	if(ix==1&&iy==1&&ic==1)
	{
		++tax;++tay;
		return;
	}
	++nb;
	ibx[nb]=ix;
	iby[nb]=iy;
	ibc[nb]=ic;
	tax+=ix;tay+=iy;
}
void task()
{
	memset(visitx,0,sizeof visitx);
	memset(visity,0,sizeof visity);
	memset(visit,0,sizeof visit);
	scanf("%d",&n);
	rep(i,n)
	rep(j,n)
	{
		scanf("%1d",&ind[i][j]);
	}
	nb=0;
	tax=0,tay=0;
	rep(ix,n)
	rep(iy,n)
	{
		if(ind[ix][iy]==1&&!visitx[ix])
		{
			tcx=tcy=0;
			tcc=0;
			dfs(ix,iy);
			pushblock(tcx,tcy,tcc);
		}
	}
	//cout<<tax<<","<<tay<<"!"<<endl;
	
	memset(tdp,38,sizeof tdp);
	res=0;
	int nz=1<<nb;
	assert(nb<=16);
	int oo=tdp[0][0][0];
	tdp[0][n-tax][n-tay]=0;
	for(int iz=0;iz<nz;++iz)
	{
		for ( int tz=iz; ; tz=(tz-1)&iz ) 
		{
			for(int rx=n-tax;rx>=0;--rx)
			{
				for(int ry=n-tay;ry>=0;--ry)
				{
					if(tdp[iz^tz][rx][ry]!=oo)
					{
						if(tz==0)
						{
							if(rx&&ry)
							{
								tdp[iz][rx-1][ry-1]=min(tdp[iz][rx-1][ry-1],tdp[iz^tz][rx][ry]+1);
							}
							continue;
						}
						int tlx=0,tly=0,tlc=0;
						rep(i,nb)
						{
							if(tz&1<<i-1)
							{
								tlx+=ibx[i];
								tly+=iby[i];
								tlc+=ibc[i];
							}
						}
						if(tlx>=tly)
						{
							if(tlx-tly<=ry)
							{
								tdp[iz][rx][ry-(tlx-tly)]=
									min(tdp[iz][rx][ry-(tlx-tly)],tdp[iz^tz][rx][ry]+tlx*tlx-tlc);
							}
						}
						else
						{
							if(tly-tlx<=rx)
							{
								tdp[iz][rx-(tly-tlx)][ry]=
									min(tdp[iz][rx-(tly-tlx)][ry],tdp[iz^tz][rx][ry]+tly*tly-tlc);
							}
						}
							
					}
				}
			}
			if(tz==0)break;
        } 
	}
	printf("%d\n",tdp[nz-1][0][0]);
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt)
	{
		printf("Case #%d: ",i);
		task();
	}
}
