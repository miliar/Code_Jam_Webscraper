#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

vector<long long> pool;

bool pal(long long x){
	vector<int> z;
	while(x){
		z.push_back(x%10);
		x/=10;
	}

	int len = z.size();

	for(int i = 0; i < (len + 1) / 2; i++){
		if(z[i] != z[len-1-i]) return false;
	}

	return true;
}

void pool_up(){
	for(int i = 1; i <= 10000000; i++){
		if(!pal(i)) continue;

		if(pal(i * i)){
			pool.push_back(i*i);
		}
	}
}

int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	pool_up();
	int T; cin >> T;
	for(int t = 1; t <= T; t++){
		long long x, y;
		cin >> x >> y;
		cout << "Case #" << t << ": ";
		cout << upper_bound(pool.begin(), pool.end(), y) - lower_bound(pool.begin(), pool.end(), x) << endl;
	}
	return 0;
}
