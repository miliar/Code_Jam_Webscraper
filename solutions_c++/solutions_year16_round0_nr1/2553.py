#include <bits/stdc++.h>

#define i64 long long
#define u64 unsigned long long
#define i32 int
#define u32 unsigned int

#define pii pair<int, int>
#define pll pair<long long, long long>

#define defmod 1000000007
using namespace std;


int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	
	int tests; cin >> tests;
	for(int test = 1; test <= tests; test++){
		i64 n; cin >> n;
		bool d[10] = {0};
		int cc = 1000;
		i64 cur = n;
		bool g = false;
		while(cc--){
			i64 c2 = cur;
			while(c2){
				d[c2%10] = 1;
				c2/=10;
			}
			bool ok = true;
			for(int i = 0; i < 10; i++){
				if(d[i] == 0)
					ok = false;
			}
			if(ok){
				g = true;
				break;
			}


			cur+=n;
		}
		cout << "Case #" << test << ": ";
		if(g)
			cout << cur << endl;
		else
			cout << "INSOMNIA" << endl;
	}
	return 0;
}