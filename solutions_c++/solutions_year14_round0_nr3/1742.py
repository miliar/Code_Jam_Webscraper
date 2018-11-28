#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include<set>
#include <map>
#include <time.h>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, 1, -1, 0};

int dx2[8] = {1, 1, 1, 0, 0, -1, -1, -1};
int dy2[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

vector<vector<int> > v;
int cas;
bool mask[30];
int a,b,c;
int n;
bool isans = false;
void ans()
{
	isans = true;
	printf("Case #%d:\n",cas);
	for(int i=0; i<a; ++i)
	{
		for(int j=0; j<b; ++j)
		{
			if(v[i][j] == -1)
				cout<<'*';
			else
			if(v[i][j] == -2)
				cout<<'c';
			else
				cout<<'.';
		}
		cout<<'\n';
	}
	return;
}
void check()
{
	int stx=-1, sty=-1;
	int ex =-1, ey = -1;
	int cnt = 0;
	for(int i=0; i<a; ++i)
	{
		for(int j=0; j<b; ++j)
		{
			if(v[i][j] == 0)
			{
				stx=i;
				sty = j;
			}
			if(v[i][j]>=0)
			{
				cnt++;
				ex=i;
				ey=j;
			}
		}
	}
	if(stx == -1 && cnt > 1)
		return;
	if(stx == -1 && cnt == 1)
	{
		v[ex][ey]=-2;
		ans();
		return;
	}
	vector<vector<int> > used(a,vector<int> (b,0));
	queue<pair<int , int> > q;
	q.push(make_pair(stx, sty));
	used[stx][sty]=1;
	cnt--;
	while(!q.empty())
	{
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for(int i=0; i<8; ++i)
		{
			int tox = x+dx2[i];
			int toy = y+dy2[i];
			if(tox>=0 && tox <a && toy>=0 && toy<b && used[tox][toy] == 0 && v[tox][toy]>=0)
			{
				cnt--;
				used[tox][toy]=1;
				if(v[tox][toy] == 0)
					q.push(make_pair(tox,toy));
			}
		}
	}
	if(cnt == 0)
	{
		v[stx][sty]=-2;
		ans();
		return;
	}

}

void rec(int i, int k)
{ 
	if(isans)
		return;
	if(i==n)
	{
		for(i=0; i<n; ++i)
		{
			if(mask[i])
			{
				v[i/b][i%b]=-1;
				int ptr1 = i/b;
				int ptr2 = i%b;
				for(int j=0; j<8; ++j)
				{
					int tox = ptr1+dx2[j];
					int toy = ptr2+dy2[j];
					if(tox>=0 && tox<a && toy >=0 && toy<b && v[tox][toy]!=-1)
						v[tox][toy]++;
				}
			}
		}
		check();
		v.assign(a, vector<int> (b,0));
		return;
	}
	if(i+k<n)
	{
		mask[i]=0;
		rec(i+1,k);
	}
	if(k>0)
	{
		mask[i]=1;
		rec(i+1,k-1);
	}
}

int main()
{
	freopen("C-small-attempt4.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(cas = 1; cas<=t; ++cas)
	{
		isans = false;
		cin>>a>>b>>c;
		n = a*b;
		v.assign(a, vector<int> (b,0));
		rec(1,c);
		if(!isans)
			printf("Case #%d:\nImpossible\n",cas);
		
	}
	return 0;
}