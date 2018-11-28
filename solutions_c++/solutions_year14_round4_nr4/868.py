#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <ctime>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef long long LL;
#define tr(container, it)for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

int m, n;
vector<string> inp;
set<vector<vector<string>>> cand;
void gen(int sm, vector<vector<string>> div) {
    //cout<<sm<<endl;
    if (sm == m) {
        bool ok = true;
        REP(i, 0, n) if (div[i].size() == 0) ok = false;
        if (ok) {
            cand.insert(div);
        }
        return;
    }
    REP(i, 0, n) {
        auto ndiv = div;
        ndiv[i].PB(inp[sm]);
        gen(sm+1, ndiv);
    }
}

struct tN {
    tN *l[256];
}*root;
int cnt;

void init(void)
{
	root=new tN();
	cnt=0;
}

void addString(string s)
{
	tN *p=root;int flag=1;
	for(int k = 0; k < (int)s.size(); k++)
	{
		if(!p->l[s[k]])
		{
			p->l[s[k]] = new tN();
			cnt++;
		}
		p = p->l[s[k]];
	}
}

void free(tN *p)
{
	for(int i=0;i<256;i++)
		if(p->l[i])
			free(p->l[i]);
	delete p;
}

int getCnt(vector<string> tr) {
    init();
    REP(i, 0, tr.size()) {
        //cout<<"Add "<<tr[i]<<endl;
        addString(tr[i]);
    }
    int ret = cnt;
    free(root);
    return ret;
}

int main() {
    clock_t startTime = clock();
    ios_base::sync_with_stdio(true);

    int testCases; cin>>testCases;
    REP(tests, 1, testCases+1) {
        inp.clear();
        cand.clear();
        cout<<"Case #"<<tests<<": ";
        cin>>m>>n;
        REP(i, 0, m) {
            string s; cin>>s;
            inp.PB(s);
        }
        vector<vector<string>> tmp;
        tmp.resize(n);
        gen(0, tmp);
        //cout<<cand.size()<<"\n";
        int mx = -1, cmx = 0;
        for (auto it = cand.begin(); it != cand.end(); it++) {
            int tt = 0;
            vector<vector<string>> cur = (*it);
            REP(i, 0, cur.size()) {
                tt += getCnt(cur[i]) + 1;
            }
//            cout<<tt<<"::\n";
//                REP(i, 0, cur.size()) {
//                    REP(j, 0, cur[i].size())
//                        cout<<cur[i][j]<<" ";
//                    cout<<"\n";
//                }
            if (mx < tt) {
                mx = tt;
                cmx = 0;
            }
            if (mx == tt) cmx++;
        }
        cout<<mx<<" "<<cmx<<"\n";
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}


