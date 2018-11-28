#include<algorithm>
#include<functional>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<bitset>
#include<climits>

#define all(c) (c).begin(), (c).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

typedef unsigned long long ull;
typedef long long ll;

const int INF=100000000;
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

using namespace std;

typedef pair<int ,int > P;

string mat[4];

string solve()
{
	rep(i,4) cin>>mat[i];

	int count=0;
	int Tcount=0;

	rep(i,4)
	{
		count=0;
		Tcount=0;
		rep(j,4)
		{
			if(mat[i][j]=='X')
				count++;
			if(mat[i][j]=='T')
				Tcount++;
		}
		if(count==4)
			return "X won";
		if(count==3&&Tcount==1)
			return "X won";
	}
	rep(i,4)
	{
		count=0;
		Tcount=0;
		rep(j,4)
		{
			if(mat[j][i]=='X')
				count++;
			if(mat[j][i]=='T')
				Tcount++;
		}
		if(count==4)
			return "X won";
		if(count==3&&Tcount==1)
			return "X won";
	}
	
	
	rep(i,4)
	{
		count=0;
		Tcount=0;
		rep(j,4)
		{
			if(mat[i][j]=='O')
				count++;
			if(mat[i][j]=='T')
				Tcount++;
		}
		if(count==4)
			return "O won";
		if(count==3&&Tcount==1)
			return "O won";
	}
	rep(i,4)
	{
		count=0;
		Tcount=0;
		rep(j,4)
		{
			if(mat[j][i]=='O')
				count++;
			if(mat[j][i]=='T')
				Tcount++;
		}
		if(count==4)
			return "O won";
		if(count==3&&Tcount==1)
			return "O won";
	}

	count=0;
	Tcount=0;
	rep(i,4)
	{
		if(mat[i][i]=='X')
			count++;
		if(mat[i][i]=='T')
			Tcount++;
	}
	if(count==4)
		return "X won";
	if(count==3&&Tcount==1)
		return "X won";


	count=0;
	Tcount=0;
	rep(i,4)
	{
		if(mat[i][i]=='O')
			count++;
		if(mat[i][i]=='T')
			Tcount++;
	}
	if(count==4)
		return "O won";
	if(count==3&&Tcount==1)
		return "O won";
	count=0;
	Tcount=0;
	rep(i,4)
	{
		if(mat[i][3-i]=='X')
			count++;
		if(mat[i][3-i]=='T')
			Tcount++;
	}
	if(count==4)
		return "X won";
	if(count==3&&Tcount==1)
		return "X won";


	count=0;
	Tcount=0;
	rep(i,4)
	{
		if(mat[i][3-i]=='O')
			count++;
		if(mat[i][3-i]=='T')
			Tcount++;
	}
	if(count==4)
		return "O won";
	if(count==3&&Tcount==1)
		return "O won";

	rep(i,4) rep(j,4) if(mat[i][j]=='.') return "Game has not completed";


	return "Draw";

}

int main()
{

	int t=0;
	cin>>t;
	FILE*fp=fopen("C:/Users/odan/Documents/app/vim/GCJ/ans.txt","w");
	rep(i,t)
	{
		//Case #1: X won
		fprintf(fp,"Case #%d: %s\n",i+1,solve().c_str());

	}
	fclose(fp);


	return 0;
}


