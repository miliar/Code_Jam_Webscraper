#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <stack>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define INF (1e9)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf =(int) 1e9;

const double eps = 1e-3;
const int ss=(int)1e6+3;
const int base=inf;

bool pred (const pair<int,int>& i, const pair<int,int>& j) 
{
    if (i.first==j.first)
        return i.second>j.second;
    else
        return i.first>j.first;
}

int main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	cin>>t;
	vector<vector<char> > table(4,vector<char>(4,0));
	FOR(ppp,t)
	{
		table.assign(4,vector<char>(4,0));
		string s  ="";
		bool x = false,o = false,empty = false;
		FOR(i,4) FOR(j,4)
		{
			cin>>table[i][j];
			if(table[i][j] =='.') empty = true;
		}

		FOR(i,4)
		{
			int xsumrow = 0;
			int xsumcol = 0;
			FOR(j,4){
				if(table[i][j] == 'X' || table[i][j] =='T') xsumrow++;
				if(table[j][i] == 'X' || table[j][i] =='T') xsumcol++;
			}
			if(xsumrow == 4 || xsumcol == 4) x = true;


			int ysumrow = 0;
			int ysumcol = 0;
			FOR(j,4){
				if(table[i][j] == 'O' || table[i][j] =='T') ysumrow++;
				if(table[j][i] == 'O' || table[j][i] =='T') ysumcol++;
			}
			if(ysumrow == 4 || ysumcol == 4) o = true;

		}
		int xsumrow = 0;
		int ysumrow = 0;
		int xsumcol = 0;
		int ysumcol = 0;
		FOR(i,4)
		{
			if(table[i][i] == 'O' || table[i][i] =='T') ysumrow++;
			if(table[3-i][i] == 'O' || table[3-i][i] =='T') ysumcol++;
			if(table[i][i] == 'X' || table[i][i] =='T') xsumrow++;
			if(table[3-i][i] == 'X' || table[3-i][i] =='T') xsumcol++;
		}
		if(ysumrow == 4 || ysumcol == 4) o = true;
		if(xsumrow == 4 || xsumcol == 4) x = true;
		if(o == true && x == true)
		{
			s = "Draw";
		}
		if(o == false && x == false && empty == false)
		{
			s = "Draw";
		}
		if(o == false && x == false && empty == true)
		{
			s = "Game has not completed";
		}
		if(o == true && x== false)
		{
			s = "O won";
		}
		if(x == true && o == false)
		{
			s = "X won";
		}

		cout<<"Case #"<<ppp+1<<": "<<s<<endl;
	}
	return 0;
}
