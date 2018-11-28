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


int main()
{
	freopen( INP_FILE , "r" , stdin );
	freopen( OUT_FILE , "w" , stdout );
	int tstCnt;
	cin>>tstCnt;

	for(int tst=1;tst<=tstCnt;tst++)
	{
        int x, n; cin>>n>>x;
        int cnt = 0; multiset<int> a;
        rp(i, n) { int t; cin>>t; a.insert(t);}
        while(!a.empty()) {
            multiset<int>::iterator it = a.end();--it;
            int v = *it; a.erase(it);
            ++cnt;
            if (!a.empty()) {
                multiset<int>::iterator it2 = a.upper_bound(x-v);
                if(it2 != a.begin()){
                    --it2;
                    if (*it2 <= v) {
                        a.erase(it2);
                    }
                }
            }
        }
        printf("Case #%d: %d\n", tst, cnt);

	}
	
	return 0;
}