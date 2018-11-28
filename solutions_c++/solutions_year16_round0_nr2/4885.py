// MainProject.cpp : Defines the entry point for the console application.
//
 
#pragma comment(linker, "/STACK:66777216")
#define _CRT_SECURE_NO_WARNINGS
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <cctype>
#include <limits>
#include <bitset>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#include <vector>
using namespace std;
 
typedef long long LL;
typedef long double LD;
 
 
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()
#define mset(m,v) memset(m,v,sizeof(m))
 
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
 
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef vector<long long> vl; typedef pair<long long,long long> pll; typedef vector<pair<long long,long long> > vpll;
typedef vector<string> vs; typedef long double ld;
 
 
#define CIA

int main()
{
#ifdef CIA
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
#define TASK "matrix"
	//freopen(task".in", "r", stdin);
	//freopen(task".out", "w", stdout);
#endif

	int c;
	cin >> c;
	
	rer(i,1,c)
	{
		string in;
		cin >> in;
		
		int idx = 0;
		int ret = 0;
		int bf = true;
		
		while(idx < in.length())
		{
			if( in[idx] == '-' )
			{
				while(idx < in.length() && in[idx] == '-')
				{
					++idx;
				}
				
				if(bf)
				{
					++ret;
				}
				else
				{
					ret += 2;
				}
				
				bf = false;
			}
			else
			{
				++idx;
				bf = false;
			}
			
		}
	
		cout << "Case #" << i << ": " << ret << endl;
		
		
	}

	
 
#ifdef CIA
	cerr << fixed << setprecision(3) << "\nExecution time = " << clock() / 1000.0 << "s\n";
#endif
	return 0;
}

