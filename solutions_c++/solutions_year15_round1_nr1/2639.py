#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())


int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ": ";
        int N;
        cin >> N;
        vector<long> v(N);
        for(int i=0; i<N; i++) {
            cin >> v[i];
        }
        long M = 0;
        fu(i,1,N) M =max(M, v[i-1]-v[i]);
        long a=0, b=0;
        fu(i,1,N) a += max(0L, v[i-1]-v[i]);
        fu(i,0,N-1) {
            b += min(M,v[i]);
        }
        cout << a << " " << b << endl;
	}
}
