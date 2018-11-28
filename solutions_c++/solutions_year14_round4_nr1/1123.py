#include <bits/stdc++.h>
using namespace std;
#define msg(x) cout<<#x<<" = "<<x<<endl;
#define N 100000
typedef long long int LL;
int v[N];
int main() {
    //ios_base::sync_with_stdio(0);
   	int T, ans, fin, tam, n;
   	scanf("%d", &T);
   	for(int caso=1 ; caso<=T ; caso++) {
   		scanf("%d %d", &n, &tam);
   		for(int i=0 ; i<n ; i++) scanf("%d", &v[i]);
   		sort(v, v+n);
   		ans = fin = 0;
   		for(int i=n-1 ; i>=fin ; i--) {
   			if( i == fin ) ans++;
   			else {
   				if( v[i] + v[fin] <= tam ) {
   					ans++;
   					fin++;
   				} else ans++;
   			}
   		}
   		printf("Case #%d: %d\n", caso, ans);
   	}
    return 0;
}