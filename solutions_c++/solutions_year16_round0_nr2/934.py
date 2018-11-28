#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <set>

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define FORC(it,cont) for(__typeof(cont.begin()) it=(cont).begin(); it!=(cont).end();++(it))
#define VI vector<int>
#define VS vector<string>

using namespace std;

int main()
	{
	int T,N;
	ifstream fcin("in.txt",ios::in);
	FILE* fout;
	fout = fopen("out.txt","w");
	fcin >> T;
	FOR(tc,0,T)
		{
		int res = 0;
		string s;
		fcin >> s;
		N = s.size();
		reverse(s.begin(),s.end());
		int mult = 0;
		
		for( int i =0; i < N; ++ i)
			{
			if ( mult == (s[i] == '-'))
				{
				continue;
				}
			else 
				{
				++res;
				mult = 1 - mult;
				}
			}
		
		fprintf(fout,"Case #%d: %d\n",tc+1,res);
		}
	fcin.close();
	return 0;
	}
