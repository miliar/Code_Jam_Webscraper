#pragma comment(linker, "/STACK:64000000")
#include <ctime>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <deque>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;
#define forn(i,n) for (LL i=0;i<n;i++)
#define rforn(i,n) for (LL i=n-1;i>=0;i--)
#define mp make_pair
#define __int64 long long
#define LL long long
const int dx[]={-1,-1,-1,0,0,0,1,1,1};
const int dy[]={-1,0,1,-1,0,1,-1,0,1};

clock_t start;

bool check(vector <vector <int> > &a, int x, int y, int xx, int yy, int m){
	if (a[xx][yy]==1)
		return false;

	clock_t finish=clock();
	if (((double) (finish-start))/CLOCKS_PER_SEC > 10)
		return false;

	deque <pair <int, int> > dq;
	vector <vector <bool> > fl(x, vector <bool> (y,0));
	dq.push_back(mp(xx,yy));
	int l=0, dd;
	while (l<dq.size())
	{
		xx=dq[l].first;
		yy=dq[l].second;
		fl[xx][yy]=1;
		l++;

		dd=0;
		forn(i,9)
		{
			if (xx+dx[i]>=0 && yy+dy[i]>=0 && xx+dx[i]<x && yy+dy[i]<y && a[xx+dx[i]][yy+dy[i]]==1){
				dd++;
			}
		}

		if (dd==0)
		{
			forn(i,9)
			{
				if (xx+dx[i]>=0 && yy+dy[i]>=0 && xx+dx[i]<x && yy+dy[i]<y && fl[xx+dx[i]][yy+dy[i]]==0){
					fl[xx+dx[i]][yy+dy[i]]=1;
					dq.push_back(mp(xx+dx[i],yy+dy[i]));
				}
			}
		}
	}

	return x*y==m+dq.size();
}

bool solve(int pos, int x, int y, int m, vector <vector <int> > &a){
	clock_t finish=clock();
	if (((double) (finish-start))/CLOCKS_PER_SEC > 10)
		return false;

	if (pos==x*y)
	{
		if (m!=0)
			return false;

		int mm=0;
		forn(i,x)
			forn(j,y)
			if (a[i][j]==1)
				mm++;

		forn(xx,x)
			forn(yy,y)
			if(check(a,x,y,xx,yy,mm))
			{
				forn(i,x)
				{
					forn(j,y)
					{
						if (i==xx && j==yy)
							cout<<'c';
						else
						if (a[i][j]==0)
							cout<<".";
						else
							cout<<"*";
					}
					cout<<"\n";
				}
				return true;
			}
		return false;
	}
	int xx, yy;
	xx=pos/y;
	yy=pos%y;

	if (y-yy+(x-1-xx)*y<m)
		return false;

	if (m>0)
	{
		a[xx][yy]=1;
		if (solve(pos+1,x,y,m-1,a))
			return true;
	}

	a[xx][yy]=0;
	if (solve(pos+1,x,y,m,a))
		return true;

	return false;
}

int main()
{
	ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	//freopen("answers.txt","w",stdout);
	#endif
	
	/*
	for (int x=1;x<=5;x++)
		for (int y=1;y<=5;y++)
			for (int m=0;m<x*y;m++)
			{				
				cout<<x<<" "<<y<<" "<<m<<" ";
				vector <vector <int> > a(x, vector <int> (y, 0));
				if (solve(0,x,y,m,a))
					cout<<1;
				else
					cout<<0;
				cout<<"\n";
			}
	*/
	int T;
	cin>>T;
	forn(t,T)
	{
		start=clock();
		cout<<"Case #"<<(t+1)<<":\n";
		int x,y,m;
		cin>>x>>y>>m;
		vector <vector <int> > a(x, vector <int> (y, 0));
		if (!solve(0,x,y,m,a)){
			cout<<"Impossible\n";
		}
	}
}