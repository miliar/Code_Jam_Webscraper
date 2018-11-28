#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
using namespace std;
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )
typedef long long LL;
typedef pair<int, int> pii;

int N;
vector<int> R;

int main(){
    int caseNumber;
    //scanf("%d", &caseNumber);
    cin>>caseNumber;
    REP(caseN, caseNumber) {
    	cin>>N; 
    	// int l = -1, pos = -1;
    	R.clear();
    	REP(i, N) {
    		int x; cin>>x;R.pb(x);
    	}
    	int small = 10000000;
    	REP(F, N) {
    		int res = 0;
    		vector<int> X = R;
    		vector<int> G(N, false);
    			int left = 0, right = 0;
    		REP(i, N) {
    			int big = 2000000000, pos = -1;
    			REP(j, N) {
    				if (!G[j] && X[j] < big) {
    					big = X[j]; pos = j;
    				}
    			}
    			// cout<<"big"<<big<<' '<<pos<<' '<<pos - left<<' '<<N - 1 - pos - right<<' '<<left<<' '<<right<<endl;
    			if (pos - left < N - 1 - pos - right) {
    				while (pos != left) {
    					swap(X[pos], X[pos - 1]);
    					pos--;res++;
    				}
    				left++;
    				// cout<<"left"<<endl;
    			} else  {
    				while (pos != N - 1 - right) {
    					swap(X[pos], X[pos + 1]);
    					pos++;res++;
    				}
    				right++;
    			}
    			G[pos] = true;
    		}
    		small = min(small, res);
    		// cout<<res<<' '<<F<<endl;
    	}
    	printf("Case #%d: %d\n", caseN + 1, small);
    }
    return 0;
}