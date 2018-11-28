#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

const double eps = 1e-9;
const int inf = 1e9 + 23;

const int size = 1000 * 1000 * 1;

int num[20];

vector <long long> ans;

bool is_polyndrome(long long x){
	vector <int> num;
	while (x > 0){
		num.push_back(x % 10);
		x /= 10;
	}
	int len = num.size();
	for (int i = 0; i < len / 2; i++)
		if (num[i] != num[len - 1 - i])
			return false;
	return true;
}

bool is_ok(long long x){
	if (is_polyndrome(x) && is_polyndrome(x * x))
		return true;
	else
		return false;
}

void generate_all (int n){
	int t = 1;
	for (int i = 0; i < (n + 1) / 2 - 1; i++)
		t *= 10;
	for (int i = t; i < t * 10; i++){
		int k = i;
		for (int j = 0; j < (n + 1) / 2; j++){
			num[j] = k % 10;
			k /= 10;
		}
		reverse(num, num + (n + 1) / 2);
		for (int j = 0; j < (n + 1) / 2; j++)
			num[n - 1 - j] = num[j];
		long long x = 0;
		for (int j = 0; j < n; j++){
			x *= 10;
			x += num[j];
		}
		assert(is_polyndrome(x));
		if (is_polyndrome(x * x))
			//cout << x << endl;
			ans.push_back(x);
	}
}

int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	for (int i = 1; i < 9; i++)
		generate_all(i);
	/*for (int i = 1; i < 1000 * 100; i++)
		if (is_ok(i))
			cout << i << endl;*/
	int n, len = ans.size();
	cin >> n;
	for (int it = 1; it <= n; it++){
		cout << "Case #" << it << ": ";
		long long a, b, c = 0;
		cin >> a >> b;
		for (int i = 0; i < len; i++)
			if (ans[i] * ans[i] >= a && ans[i] * ans[i] <= b)
				c++;
		cout << c << endl;
	}

	return 0;
}