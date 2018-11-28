#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#define REP(i, a, b) for ( int i = int(a); i <= int(b); i++ )
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(a) (a).begin(), (a).end()
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define DFS_WHITE -1
#define DFS_BLACK 1
#define MAXN 10010
using namespace std;

struct node {
	string org, cmp;
	vector< pair< char, int> > pat;
};

int T, N;
char buff[MAXN];
vector<node> IN;

void compressStr() {
	REP(i, 0, N-1) {
		int k = IN[i].org.size();
		char c = IN[i].org[0];
		IN[i].cmp = "";
		IN[i].cmp += c;
		IN[i].pat.pb(mp(c, 1));
		int idx = 0;
		REP(j, 1, k-1) {
			if(IN[i].org[j] == 13) continue;
			if(IN[i].org[j] != c) {
				c = IN[i].org[j];
				IN[i].cmp += c;
				IN[i].pat.pb(mp(c, 1));
				idx++;
			} else {
				IN[i].pat[idx].ss++;
			}
		}		
	}
}

bool allCompressedStrEqual() {
	string str = IN[0].cmp;	
	REP(i, 1, N-1) {		
		if(IN[i].cmp != str) {			
			return false;
		}
	}
	return true;
}

pair<int, vector< pair<char, int> > > changesReq(int a, int b) {
	int k = IN[a].pat.size();
	int c = 0;
	vector< pair<char, int> > pat;
	REP(i, 0, k-1) {
		c += abs(IN[a].pat[i].ss - IN[b].pat[i].ss);
		pat.pb(mp(IN[a].pat[i].ff, min(IN[a].pat[i].ss, IN[b].pat[i].ss)));
	}
	return mp(c, pat);
}

int changesReq2(int a, vector< pair<char, int> >& pat) {
	int k = IN[a].pat.size();
	int c = 0;	
	REP(i, 0, k-1) {
		c += abs(IN[a].pat[i].ss - pat[i].ss);		
	}
	return c;
}

int main()
{
    sscanf(gets(buff), "%d", &T);
    REP(tt, 1, T) {
    	sscanf(gets(buff), "%d", &N);
    	IN.clear(); IN.resize(N);
    	REP(i, 0, N-1) {
    		gets(buff);
    		IN[i].org = string(buff);
    	}
    	compressStr();
    	printf("Case #%d: ", tt);
    	if(allCompressedStrEqual()) {
    		//putchar('\n');
    		int minv = (1 << 30), v;
    		pair<int, vector< pair<char, int> > > ret;
    		REP(i, 0, N-1) {
    			REP(j, 0, N-1) {
    				if(i != j) {
    					ret = changesReq(i, j);
    					v = ret.ff;
    					REP(k, 0, N-1) {
    						if(k != i && k != j) {
    							v += changesReq2(k, ret.ss);
    						}
    					}
    					minv = min(minv, v);
    				}
    			}
    		}
    		printf("%d\n", minv);
    	} else {
    		printf("Fegla Won\n");
    	}
    }
    return 0;
}
