#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int inf = 1 << 25;

int getCount( int x, int y )
{
    int ans = x / y;
    return ((x % y == 0) ? ans - 1 : ans);
}

int main( void )
{
    int t;
    scanf("%d", &t);
    
    int tt = 1;
    
    while( t-- )
    {
        int n;
        scanf("%d", &n);
        vector<int> a(N);
        for( int i = 0; i < n; i++ )
	    scanf("%d", &a[i]);
        sort(a.begin(), a.end());
        
        int ans = a[n-1];
        for( int mx = 1; mx <= a[n-1]; mx++ ) {

	    int lo = 0, hi = a[N-1] - mx, minReq;
	    while( lo <= hi )
	    {
	        int m = (lo + hi) / 2;

	        int best = inf;
	        vector<int> vv = {0, m};
	        for( int kk = 0; kk < vv.size(); kk++ ) {
                int t = vv[kk];
		        int req = 0;
		        for( int j = n-1; j >= 0 && (a[j]-t > mx); j-- ) 
		        {   req += getCount(a[j]-t, mx);
		        }
		        best = min(best, req + t);
	        }

	        if( best <= mid ) {
		        minReq = m;
		        hi = m - 1;
	        } else {
		        lo = m + 1;
	        }
	    }
	    
	    ans = min(ans, mx + minReq);
	}

	printf("Case #%d: %d\n", tt++, ans);
    
    }

    return 0;
}
