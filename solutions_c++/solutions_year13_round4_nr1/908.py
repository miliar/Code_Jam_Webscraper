#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;

typedef pair<int, int> PII;

typedef vector<int> VI;
typedef vector<vector<int> > VII;
typedef vector<PII> VPII;

typedef vector<double> VD;
typedef vector<string> VS;

typedef long long LL;

int t[102];
int N, M;

LL temp, c;

LL costs(int o, int e){
    temp = 0;
    c = N;
    for(int j=o; j<e; j++){
        temp += c;
        --c;
        if(temp > 1000002013)
	        temp = temp % 1000002013;
    }
    return temp;
}

int main(){ 	
	int cases;
	scanf("%d\n", &cases);
	
	for(int caseNr = 1; caseNr <= cases; caseNr++){
		// go for it!	
		printf("Case #%d: ", caseNr);
		
		// INIT
		memset(t, 0, sizeof(t));
		LL normalCosts = 0L;
		LL cheatedCosts = 0L;
		
		// READ
		scanf("%d %d\n", &N, &M);
		
	    int o, e, p;		
		for(int i=0; i<M; i++){
		    scanf("%d %d %d\n", &o, &e, &p);
		    
		    // calc normal costs		    
		    normalCosts += costs(o, e) * p;
	        if(normalCosts > 1000002013)
		        normalCosts = normalCosts % 1000002013;
		    
		    // memorize for cheated costs
		    for(int j=o; j<e; j++){
		        t[j] += p;
		    } 
		}
		
		// GO
		while(true){
		    // find longest subsequence > 0
		    int start = -1;
		    int len = -1;
		    for(int i=0; i<N; i++){
		        if(t[i] == 0)
		            continue;
	            
	            int tlen = 0;
	            int tstart = i;
	            while(t[i] > 0 && i < N){
	                ++i;
	                ++tlen;
	            }
	            if(tlen > len){
	                len = tlen;
	                start = tstart;
	            }	                
		    }
		    if(len < 0)
		        break;
		    
		    // reduce subsequence
		    for(int i=start; i<start+len; i++){
		        --t[i];
		    }
		    cheatedCosts += costs(start, start+len);
		    if(cheatedCosts > 1000002013)
    		    cheatedCosts = cheatedCosts % 1000002013;
		}
		
		
		LL savings = normalCosts - cheatedCosts;
	    if(savings > 1000002013)
		    savings = savings % 1000002013;
		
		printf("%lld\n", savings);
		
		fflush(stdout);
	}
	
	return 0;
}
