#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <fstream>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <deque>
using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)

int main()
{
	ifstream in("in.in");
	ofstream out("output.txt");
	int t, n, l;
	string s;
	in>>t;
	REP(q,t)
	{
		set<pii> rez;
		in>>s>>n;
		vector<int> gl;
		gl.push_back(-1);
		REP(i,s.size())
		{
			if ((s[i] == 'a') || (s[i] == 'e') || (s[i] == 'i') || (s[i] == 'o') || (s[i] == 'u')) 
			{
				s[i] = '?';
				gl.push_back(i);
			}
		}
		gl.push_back(s.size());
		int pred = 0;
		int k = 0;
		REP(i,gl.size())
		{
			if (gl[i] - pred >= n)
			{
				for(int z = pred+1; z <= gl[i] - n; z++)
				{
					for(int w = 0; w <= z; w++)
						for (int e = z+n; e<= s.size(); e++)
							rez.insert(mp(w,e));
				}
			}
			pred = gl[i];
		}
		out<<"Case #"<<q+1<<": "<<rez.size()<<'\n';
	}
	in.close();
	out.close();
	return 0;
}