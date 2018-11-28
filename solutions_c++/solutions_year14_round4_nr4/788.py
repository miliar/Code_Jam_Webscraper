#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#define INP_FILE "input.txt"
#define OUT_FILE "output.txt"

#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define pb push_back
#define L(s) (int)s.size()
#define mp make_pair
#define pii pair<int,int>
#define x first 
#define y second
#define inf 1000000000
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(),(s).end()
#define C(u) memset((u),0,sizeof((u)))
#define ull unsigned ll
#define uint unsigned int

int m_nodes;
int hits;
int n,m;
char a[10][20];
VI len;
vector<VI > com;
vector<VI > s;
int nodes;

void solve(int id) {
    if (id == -1) {
        rp(i, m) if (s[i].empty()) { return; }
        if (nodes > m_nodes) { m_nodes = nodes; hits = 0;}
        if (nodes == m_nodes) { ++hits; }
        return;
    }
    rp(i, m) {
        int c = 0;
        rp(j, s[i].size()) {
            c = max(c, com[s[i][j]][id]);
        }
        int addnodes = len[id] - c;
        s[i].pb(id);nodes+=addnodes;
        solve(id-1);
        s[i].resize(s[i].size()-1);nodes-=addnodes;
    }
}

int main()
{
	freopen( INP_FILE , "r" , stdin );
	freopen( OUT_FILE , "w" , stdout );
	int tstCnt;
	cin>>tstCnt;
    

	for(int tst=1;tst<=tstCnt;tst++)
	{
        com.clear(); len.clear();s.clear();
        cin>>n>>m;
        s.resize(m);
        com.resize(n, VI(n));
        rp(i, n) { scanf("%s", a[i]); len.pb(strlen(a[i]));}
        rp(i, n) rp(j, i) {
            int k = 0; while (a[i][k] && (a[i][k] == a[j][k])) ++k;
            com[i][j]=com[j][i]=k;
        }
        m_nodes = -1; hits =0;

        nodes =0;
        solve(n-1);
        m_nodes+=m;

        printf("Case #%d: %d %d\n",tst, m_nodes, hits);
	}
	
	return 0;
}