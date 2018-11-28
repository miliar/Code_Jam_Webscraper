#include <iostream>

using namespace std;

void solve(int test){
	//char b[4][4];
	unsigned long long r = 0;
	unsigned long long t = 0;

	cin >> r >> t;

	unsigned long long x = 1;
	while(1){
		unsigned long long used = 2 * x * x + (2*r-1) * x;
		if(used > t) break;
		else x++;
	}

		cout << "Case #" << test << ": " << x - 1 << endl;
	
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests = 0;
	scanf("%d", &tests);
	for(int i=1; i <= tests; ++i){
		solve(i);
	}
}