#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1 << 30;

int f( int from, int to ) {
	int ret = from / to;

    return (from % to == 0) ? ret - 1 : ret;
}

int main( void ) {
    int T;
    scanf("%i", &T);
    
    int nC = 1;
    
    while( T-- ) {
        int N;
        scanf("%i", &N);

        vector<int> A(N);
        for( int i = 0; i < N; i++ )
	    scanf("%i", &A[i]);
        sort(A.begin(), A.end());
        
        int ans = A[N-1];
        for( int MAX = 1; MAX <= A[N-1]; MAX++ ) { // iterate over all maximums
        	
	    // TOTCOST = MAX + minReq

	    int lo = 0, hi = A[N-1] - MAX, minReq;
	    while( lo <= hi ) {
	        int mid = (lo + hi) / 2;

	        
	        int best = INF;
	        for( int t = 0; t <= mid; t+=mid ) { // iterate over all normal minutes
			
			    int req = 0;
			    for( int j = N-1; j >= 0 && (A[j]-t > MAX); j-- ) 
			        req += f(A[j]-t, MAX);

			    int tot = req + t;

			    best = min(best, tot);
			    if(mid == 0) break;
	        }

	        if( best <= mid ) {
		    minReq = mid;
		    hi = mid - 1;
	        } else {
		    lo = mid + 1;
	        }
	    }
	    
	    ans = min(ans, MAX + minReq);
	}

	printf("Case #%i: %i\n", nC++, ans);
    
    }

    return 0;
}
