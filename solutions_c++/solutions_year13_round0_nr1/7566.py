#include "stdafx.h"
#include <iostream>
using namespace std;
char A[4][4];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.in","w",stdout);
	bool hs,hsdot;
	int N,ax,ao;
	int rx,ro,dix,dio,dnx,dno;
	cin>>N;
	for (int ni=1;ni<=N;ni++)
	{
		int cx[4]={0},co[4]={0};
		hsdot=hs=false;
		dix=dio=dnx=dno=0;
		for (int y=0;y<4;y++)
		{
			rx=ro=0;
			for (int x=0;x<4;x++)
			{
				cin>>A[y][x];
				if(A[y][x]=='.')
					hsdot=true;
				ao=(A[y][x]=='O'||A[y][x]=='T')?1:0;
				ax=(A[y][x]=='X'||A[y][x]=='T')?1:0;
				ro+=ao;	rx+=ax;	co[x]+=ao;	cx[x]+=ax;
				if(x==y)
				{
					dio+=ao;
					dix+=ax;
				}
				if(x==3-y)
				{
					dno+=ao;
					dnx+=ax;
				}
			}
			if(ro==4 && !hs)
				cout<<"Case #"<<ni<<": O won"<<std::endl,hs=true;
			if(rx==4&& !hs)
				cout<<"Case #"<<ni<<": X won"<<std::endl,hs=true;
		}
		if(hs)
			continue;
		if(dno==4||dio==4)
			cout<<"Case #"<<ni<<": O won"<<std::endl,hs=true;
		if(dnx==4||dix==4)
			cout<<"Case #"<<ni<<": X won"<<std::endl,hs=true;
		for (int i=0;i<4 && !hs;i++)
		{
			if(co[i]==4)
				cout<<"Case #"<<ni<<": O won"<<std::endl,hs=true;
			if(cx[i]==4)
				cout<<"Case #"<<ni<<": X won"<<std::endl,hs=true;
		}
		if(!hsdot && !hs)
			cout<<"Case #"<<ni<<": Draw"<<std::endl,hs=true;
		if(!hs)
			cout<<"Case #"<<ni<<": Game has not completed"<<std::endl;
	}

	return 0;
}