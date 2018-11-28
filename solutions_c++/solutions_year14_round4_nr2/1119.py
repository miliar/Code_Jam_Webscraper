#include <bits/stdc++.h>
using namespace std;
#define msg(x) cout<<#x<<" = "<<x<<endl;
typedef long long int LL;
int main() {
    //ios_base::sync_with_stdio(0);
    int T, n, vv[50], v[50], tmp[50];
    scanf("%d", &T);
    for(int caso=1 ; caso<=T ; caso++) {
    	scanf("%d", &n);
    	int maximo = -(1<<20);
    	for(int i=0 ; i<n ; i++) {
    		scanf("%d", &v[i]);
    		tmp[i] = v[i];
    		vv[i] = v[i];
    		maximo = max(v[i], maximo);
    	}
    	sort(tmp, tmp+n);
    	int ans = (1<<20);
    	do{
    		bool flag = true;
    		for(int i=0 ; flag && i<n ; i++) {
    			if( tmp[i] == maximo ) {
    				for(int k=0 ; k<i ; k++) {
    					if( tmp[k] > tmp[k + 1] ) {
    						flag = false;
    						break;
    					}
    				}
    				for(int k=i ; flag && k<n-1 ; k++) {
    					if( tmp[k] < tmp[k + 1] ) {
    						flag = false;
    						break;
    					}
    				}
    			}
    			vv[i] = v[i];
    		}

    		if( flag ) {
    			int cnt = 0;
    			for(int i=0 ; i<n ; i++) {
    				for(int k=i ; k<n ; k++) {
    					if( tmp[i] == vv[k] ) {
    						for(int j=k ; j>i ; j--) {
    							cnt++;
    							swap(vv[j], vv[j - 1]);
    						}
    					}
    				}
    			}
    			if( cnt < ans ) ans = cnt;
    		}
    	}while(next_permutation(tmp, tmp + n));
    	printf("Case #%d: %d\n", caso, ans);
    }
    return 0;
}