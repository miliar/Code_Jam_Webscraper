//#define NDEBUG

#include <iostream>
#include <fstream>
#include <bitset>
#include <vector>
#include <queue>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <sstream>
#include <string>
#include <numeric>

using namespace std;

#define all(c) c.begin(),c.end()
#define nl '\n'
#define printv(v) for (long long i=0 ; i<v.size() ; i++) cout<<v[i]<<" "; cout<<nl;
#define printpv(v) for (long long i=0 ; i<v.size() ; i++) cout<<v[i].first<<","<<v[i].second<<" "; cout<<nl;
#define maxnum 50005
#define inf 1000000000

ifstream fin ("cj.in");
ofstream fout ("cj.out");

int t;

int main()
{
	fin>>t;
	for (int k=0 ; k<t ; k++)
	{
		char grid[4][4];
		for (int i=0 ; i<4 ; i++)
			for (int j=0 ; j<4 ; j++)
				fin>>grid[i][j];

		bool over=false;

		//row
		for (int i=0 ; i<4 ; i++)
		{
			int xrc=0, orc=0;
			bool t=false;
			for (int j=0 ; j<4 ; j++)
			{
				if (grid[i][j]=='X') xrc++;
				if (grid[i][j]=='O') orc++;
				if (grid[i][j]=='T') t=true;
			}
			if (xrc==4 || (xrc==3 && t)) 
			{
				fout<<"Case #"<<k+1<<": "<<"X won"<<nl;
				over=true;
				break;
			}
			if (orc==4 || (orc==3 && t))
			{
				fout<<"Case #"<<k+1<<": "<<"O won"<<nl;
				over=true;
				break;
			}
		}
		if (over) continue;

		//column
		for (int i=0 ; i<4 ; i++)
		{
			int xcc=0, occ=0;
			bool t=false;
			for (int j=0 ; j<4 ; j++)
			{
				if (grid[j][i]=='X') xcc++;
				if (grid[j][i]=='O') occ++;
				if (grid[j][i]=='T') t=true;
			}
			if (xcc==4 || (xcc==3 && t)) 
			{
				fout<<"Case #"<<k+1<<": "<<"X won"<<nl;
				over=true;
				break;
			}
			if (occ==4 || (occ==3 && t))
			{
				fout<<"Case #"<<k+1<<": "<<"O won"<<nl;
				over=true;
				break;
			}
		}
		if (over) continue;

		//diagonals
		int xc=0, oc=0;
		bool t=false;
		for (int i=0 ; i<4 ; i++)
		{
			if (grid[i][i]=='X') xc++;
			if (grid[i][i]=='O') oc++;
			if (grid[i][i]=='T') t=true;
		}
		
		if (xc==4 || (xc==3 && t)) 
			{
				fout<<"Case #"<<k+1<<": "<<"X won"<<nl;
				over=true;
			}
		else if (oc==4 || (oc==3 && t))
			{
				fout<<"Case #"<<k+1<<": "<<"O won"<<nl;
				over=true;
			}
		if (over) continue;

		xc=0, oc=0;
		t=false;
		for (int i=0 ; i<4 ; i++)
		{
			if (grid[i][3-i]=='X') xc++;
			if (grid[i][3-i]=='O') oc++;
			if (grid[i][3-i]=='T') t=true;
		}
		if (xc==4 || (xc==3 && t)) 
			{
				fout<<"Case #"<<k+1<<": "<<"X won"<<nl;
				over=true;
			}
		else if (oc==4 || (oc==3 && t))
			{
				fout<<"Case #"<<k+1<<": "<<"O won"<<nl;
				over=true;
			}
		if (over) continue;
		
		for (int i=0 ; i<4 ; i++)
		{
			for (int j=0 ; j<4 ; j++)
			{
				if (grid[i][j]=='.')
				{fout<<"Case #"<<k+1<<": "<<"Game has not completed"<<nl; over=true; break;}
			}
			if (over) break;
		}
		if (over) continue;

		fout<<"Case #"<<k+1<<": "<<"Draw"<<nl;
	}
}
		
