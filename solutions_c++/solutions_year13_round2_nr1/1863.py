#include <iostream>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>
#include <stack>
#include <queue>
#include <list>
#include <limits.h>
#include <time.h>
#include <iterator>

#pragma comment(linker, "/STACK:167772160")

using namespace std;

int main(){
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		int k, n;
		cin >> k >> n;
		long long x[111];
		for(int i=0; i<n; i++) cin >> x[i];

		if(k == 1){
			cout << "Case #" << t << ": ";
			cout << n << "\n";
			continue;
		}
		
		sort(x, x+n);
		long long s = k;
		int in = 0;
		while((in < n) && (s > x[in])) s += x[in], in++;
		if(in == n) cout << "Case #" << t << ": " << "0\n"; else{
			int ans = n - in;
			int c = 0;
			for(int i=in; i<n; i++){
				ans = min(ans, c + n - i);
				int kk = 0;
				while(s <= x[i]) s += s - 1, kk++;
								 s += x[i];
				//if(in == n) ans = min(ans, c + kk);
				ans = min(ans, c + n - i + kk - 1);
				c += kk;
			}
			//int ans = 1010101;
			//int cur = 0;
			//while(in < n){
			//	ans =  cur + n - in; 
			//	//cout << s << endl;
			//	int kk = 0;
			//	long long ss = s;
			//	while(ss <= x[in]) ss += ss-1, kk++;
			//					   ss += x[in];
			//	int inn = in+1;
			//	while(inn < n && ss > x[inn]) ss += x[inn], inn++;

			//	if(kk + n - inn <= n - in){
			//		in = inn;
			//		s = ss;
			//		cur += kk + n - inn;
			//		//cout << cur << endl;
			//		ans = cur;
			//	}else break;
			//	
			//}
			cout << "Case #" << t << ": ";
			cout << ans << "\n";
		}
	}
	return 0;
}

/*srand(time(0));
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);
	for(int i=0; i<400400; i++)
		color[i] = -1;*/
//int n, m;
// 
//	//scanf("%d %d", &n, &m);
//	char c;
//	//scanf("%c", &c);
// 
//	n = 5000;
//	m = 100000;
//	int cnt = 0;
//	long long a[5010];
//	for(int i=0; i<n; i++) a[i] = 0;
//	while(m--){
//		int p = rand() % 12345678;
//		int l = rand() % n;
//		int r = rand() % n;
//		if(l > r) swap(l, r);
//		if(!l) continue;
//		int x = rand() % 1000000000;
//		if(p & 1){
////			cout << "A " << l << " " << r << " " << x << endl;
//			for(int i=l; i<=r; i++)
//				a[i] = x;
//			upd(1, 1, n, l, r, x);
//		}else{
////			cout << "Q " << l << " " << r << endl;
//			long long s = 0;
//			for(int i=l; i<=r; i++)
//				s += a[i];
//			if(s != find(1, 1, n, l, r)) cnt++;//, cout << "#" << endl;
//		}
//	}
//	cout << cnt << endl;