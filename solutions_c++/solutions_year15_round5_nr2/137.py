#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
		int N, K;
    cin >> N >> K;

		vector<int> v(N), d(K), s(K);
		int M = N-K+1;
		for (int i=0;i<M;i++) {
			cin >> v[i];
		}

		int diff = 0, off = 0;
		for (int i=0;i<K;i++) {
			int c = 0, lo = 0, hi = 0;
			for (int j=i;j<M-1;j+=K) {
				c += v[j+1]-v[j];
				lo = min(lo, c);
				hi = max(hi, c);
			}
			d[i] = hi-lo;
			off += s[i] = -lo;
			diff = max(diff, hi-lo);
		}
		int slack = 0;
		for (int i=0;i<K;i++) slack += diff - d[i];

		int base = off;
		base += ((v[0] - (base+slack))/K)*K;
		while (true) {
			if (base + slack < v[0] && base + K <= v[0]) base+=K;
			else if (base > v[0]) base-=K;
			else break;
		}
		int add = 0;
		if (v[0]>base+slack) add++;
		printf("Case #%d: %d\n",t,diff + add);
//		base -= off;
////printf("%d %d %d %d %d\n",diff,add,base,off,slack);
//		//cout << base << endl;
//		vector<int> a(N);
//		int num = 0;
//		for (int i=0;i<K;i++) {
//			a[i] = base/K + s[i];
//			if (base+off+num<v[0]) {
//				int inc = min(v[0]-base-num-off,diff-d[i]+add);
//				num+=inc;
//				a[i]+=inc;
//			}
//		}
//		for (int i=1;i<M;i++) {
//			a[K+i-1] = a[i-1]+(v[i]-v[i-1]);
//		}
//		//for (int i=0;i<N;i++) cout << a[i] << " ";
//		//cout << endl;
//
//		int lo2=100000, hi2=-100000;
//		for (int i=0;i<N;i++) {
//			lo2 = min(lo2,a[i]);
//			hi2 = max(hi2,a[i]);
//		}
//		int w = 0;
//		for (int i=0;i<K;i++) w+=a[i];
//		if (w != v[0]) cout << w << "!=" << v[0] << endl;
//		//cout << hi2-lo2 << endl;
//		if (hi2-lo2 != diff+add) cout << hi2-lo2 << "!=" << diff+add << endl;
//		for (int i=K;i<N;i++) {
//			w+=a[i]-a[i-K];
//			if (w != v[i-K+1]) cout << w << "!=" << v[i-K+1] << endl;
//		}
//		
  }

}
