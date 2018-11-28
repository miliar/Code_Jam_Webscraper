#include <bits/stdc++.h>
using namespace std;
#define INF 1000000007;
const int N = 1001;
int h[N];
void solve(int test)
{
	int D, res = 0, val;
	cin >> D;
	memset(h, 0, sizeof(h));

	for (int i = 0; i<D; i++){
		cin >> val;
		h[val]++;
		res = max(res, val);
	}

	for (int minutes = 1; minutes<N; minutes++){
		int total = 0;
		for (int pancakes = minutes+1; pancakes<N; pancakes++){
			if (h[pancakes] == 0) continue;
			int shifts = 0;
			if (pancakes % minutes == 0)
				shifts = pancakes / minutes - 1;
			else 
				shifts = pancakes/ minutes;
			total += shifts * h[pancakes];
			//cout << minutes <<" " << pancakes <<" " << shifts << endl;
		}
		res = min(res, minutes + total);
	}
	printf("Case #%d: %d\n", test, res);
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i<=t; i++)
		solve(i);
	return 0;
}