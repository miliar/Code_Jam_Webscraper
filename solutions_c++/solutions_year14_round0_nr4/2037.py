#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
using namespace std;
#define TR(i,v) 		for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
#define DEBUG(x) 		cout << #x << " = "; cout << x << endl;
#define SIZE(p) 		(int)(p).size()
#define MP(a, b)		make_pair((a), (b))
#define ALL(p)			(p).begin(), (p).end()
#define rep(i, n)		for(int (i)=0; (i)<(int)(n); ++(i))
#define REP(i, a, n)	for(int (i)=(a); (i)<(int)(n); ++(i))
#define FOR(i, a, b)   	for(int (i)=(int)(a); (i)<=(int)(b); ++(i))
#define FORD(i, b, a)  	for(int (i)=(int)(b); (i)>=(int)(a); --(i)) 
typedef long long LL;
typedef pair<int, int> pii;
const double eps = 1e-6;
int P1[1005], P2[1005];
class Hungary{
public:
    static const int SIZE = 1005; // 最大的单侧点个数
    int cnt,pos[SIZE],neg[SIZE]; // pos[]为左侧点所匹配到的右侧点编号
                                 // neg[]反之，没有匹配到对应的点则为-1
    // 传入左侧点个数n和左侧点至右侧点的边表e[]，返回匹配对的数量cnt
    int gao(int n, const vector<int> e[]){
        memset(pos,-1,sizeof(pos));
        memset(neg,-1,sizeof(neg));
        for(int i=cnt=0;i<n;i++){
            memset(v,0,sizeof(v));
            if(aug(i,e)) cnt++;
        }
        return cnt;
    }
private:
    bool v[SIZE];
    bool aug(int x, const vector<int> e[]){
        int y;
        for(size_t i=0;i<e[x].size();i++) if(!v[y=e[x][i]]){
            v[y]=true;
            if(~neg[y] && !aug(neg[y],e)) continue;
            pos[neg[y]=x]=y;
            return true;
        }
        return false;
    }
}solver;
vector<int> g[1005];
int main(int argc, char const *argv[])
{
	#ifndef ONLINE_JUDGE
    freopen("D.in", "r", stdin);
    freopen("D.out1", "w", stdout);
    #endif
	// ios::sync_with_stdio(false);		cin.tie(0);
    int T;		scanf("%d", &T);
    FOR(cs, 1, T)
    {
    	int n;	scanf("%d", &n);
    	set<int> dic;
    	rep(i, n)
    	{
    		double tmp;		scanf("%lf", &tmp);
    		P1[i] = floor(tmp*1000000+eps);
    	}
    	rep(i, n)
    	{
    		double tmp;		scanf("%lf", &tmp);
    		P2[i] = floor(tmp*1000000+eps);
    		dic.insert(P2[i]);
    	}
    	rep(i, n)			g[i].clear();
    	rep(i, n)
    	rep(j, n)		if(P1[i] > P2[j])
    		g[i].push_back(j);
    	int r1 = solver.gao(n, g);
    	int r2 = 0;
    	// sort(P1, P1+n);
    	// sort(P1, P1+n, greater<int>());
    	// random_shuffle(P1, P1+n);
    	rep(i, n)
    	{
    		set<int>::iterator f = dic.upper_bound(P1[i]);
    		if(f == dic.end())
    		{
    			++r2;
    			dic.erase(*dic.begin());
    		}else
    		{
    			dic.erase(*f);
    		}
    	}
    	printf("Case #%d: %d %d\n", cs, r1, r2);
    }
	return 0;
}