#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <string>

using namespace std;

#define INF  1000000;

int fuck( int from, int to ) {
    return (from % to == 0) ? (from / to - 1) : (from / to);
}

int main( void ) {
    int TA;
    scanf("%d", &TA);
    int cc = 1;
    
    while( TA-- ) {
        int n;
        scanf("%d", &n);

        vector<int> A(n);
        for( int i = 0; i < n; i++ )
	    	scanf("%d", &A[i]);
       
        sort(A.begin(), A.end()); 

        int ans = A[n-1]; // Beginign Get max as ans
        
        for( int FOO = 1; FOO <= A[n-1]; FOO++ ) {
		    int lo = 0, hi = A[n-1] - FOO, Cur_min = 0;

		    while( lo <= hi ) {
		        int mid = (lo + hi) / 2;
		        int best = INF;
		        int t;

		        if(true) {
		        	t = 0;
				    int req = 0;

				    for( int j = n-1; j >= 0 && (A[j] - t > FOO); j-- ) 
				        req += fuck (A[j]-t, FOO);

				    int tot = req + t;

				    best = min(best, tot);
		        }
		        if(true) {
		        	t = mid;
				    int req = 0;

				    for( int j = n-1; j >= 0 && (A[j]-t > FOO); j-- ) 
				        req += fuck(A[j] - t, FOO);

				    int tot = req + t;

				    best = min(best, tot);
		        }

		        if( best <= mid ) {
			    	Cur_min = mid;
			    	hi = mid - 1;
		        } else
			    lo = mid + 1;
		    }

		    ans = min(ans, FOO + Cur_min);
	}
	printf("Case #%d: %d\n", cc++, ans);
    
    }

    return 0;
}
