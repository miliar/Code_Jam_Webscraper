#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for (int i=a;i>=b;i--)
#define eps 1e-9
#define MOD 1000000007

int main(){
	#ifndef ONLINE_JUDGE
		freopen("A-large.in", "r", stdin);
		freopen("a.out","w", stdout);
	#endif
    ios_base::sync_with_stdio(false);
    int test;
    cin >> test;
    int n;
    int a[100010];
    FOR(i, 1, test){
    	cin >> n;
    	FOR(j, 0, n-1) cin >> a[j];
    	
    	int t, t1, t0;
    	t = t1 = t0 = 0;
    	//t1 += a[0];
    	
    	t0 = 0;
    	for(int j = 1; j < n; j++) {
    		if (a[j] < a[j-1]) t += (a[j-1]-a[j]);
    		t0 = max(t0, (a[j-1]- a[j]));
    	}
    	for(int j = 0; j < n - 1;j++){
    		if (a[j] < t0)  t1 += abs(a[j]);
    		else t1 += t0;
    		//cout << j << " " << a[j] << endl;
    	}
    	//t1 -= a[n-1];
    	
    	cout << "Case #" << i << ": "<< t << " " << t1 << endl;
    
    }
	return 0;
}

