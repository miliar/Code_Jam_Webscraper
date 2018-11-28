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

int solve(VI a, int p) {
    int cnt = 0;
    int ps = max_element(all(a))-a.begin();
    while (ps>p) { swap(a[ps],a[ps-1]); --ps; ++cnt;}
    while (ps<p) { swap(a[ps],a[ps+1]); ++ps; ++cnt;}
    int n =a.size();

    VI b(a);
    sort(all(b));
    for(int  i = n-2; i>=0; --i) {
        int v = b[i];
        int cur, id; 
        rp(i,n) {
            if(v==a[i]) cur = i;
            if(v<a[i]) id = i;
        }
        int step = (id>cur) ? 1 : -1;
        while(a[cur]>a[cur+step]) {
            swap(a[cur], a[cur+step]);
            cur+=step;
            ++cnt;
        }
    }

    return cnt;
}
int solve2(VI &a) {
    int cnt = 0;
    VI b(a); sort(all(b));
    int n = a.size();
    rp(i, n) {
        int v = b[i];
        int lo = 0; while(a[lo]<v) ++lo;
        int hi =n-1; while (a[hi]<v) --hi;
        int cur = 0; while (a[cur]!=v) ++cur;
        if (hi-cur< cur-lo) {
            while(cur!=hi) { swap(a[cur], a[cur+1]);++cur;++cnt;}
        }else{
            while(cur!=lo) { swap(a[cur], a[cur-1]);--cur;++cnt;}
        }
    }

    return cnt;
}

int main()
{
	freopen( INP_FILE , "r" , stdin );
	freopen( OUT_FILE , "w" , stdout );
	int tstCnt;
	cin>>tstCnt;

	for(int tst=1;tst<=tstCnt;tst++)
	{
        int n; cin>>n;
        VI a;
        rp(i, n) { int t; cin>>t; a.pb(t); }
        int ps = max_element(all(a))-a.begin();
        int cnt = solve(a, ps);
        /*rp(i, n){
            int t = solve(a, i);
            cnt = min(cnt, t);
        }/**/
        int t = solve2(a);
        cnt = min(cnt, t);

        printf("Case #%d: %d\n",tst, cnt);
	}
	
	return 0;
}