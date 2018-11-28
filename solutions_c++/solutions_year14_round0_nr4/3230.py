#include <iostream>
#include <cstdio>
#include <algorithm>
#include <deque>
using namespace std;

int t, n, ans, ans2;
double l[1005], g[1005];
deque<double> one, two;

int main(){
	cin >> t;
	for(int k = 1; k <= t; ++k){
		ans = ans2 = 0;
		cin >> n;
		for(int a = 0; a < n; ++a) cin >> l[a];
		for(int a = 0; a < n; ++a) cin >> g[a];
		sort(l, l+n);
		sort(g, g+n);
		for(int a = 0; a < n; ++a) one.push_back(l[a]);
		for(int a = 0; a < n; ++a) two.push_back(g[a]);
		for(int a = 0; a < n; ++a){
			if(one.front() > two.front()){
				++ans;
				one.pop_front();
				two.pop_front();
			}
			else{
				one.pop_front();
				two.pop_back();
			}
		}
		int a = 0;
		/*
		for(int a = 0; a < n; ++a) cout << l[a] << " ";
		cout << endl;
		for(int a = 0; a < n; ++a) cout << g[a] << " ";
		cout << endl;
		*/
		while(n){
			int pos = upper_bound(g, g+n, l[a++])-g;
			if(pos >= n){
				++ans2;
				g[0] = 10000;
			}
			else{
				g[pos] = 10000;
			}
			sort(g, g+n);
			//cout << a << ": " << pos << " " << ans2 << endl;
			--n;
		}
		//--ans2;
		cout << "Case #" << k << ": " << ans << " " << ans2 << endl;
	}
	return 0;
}
