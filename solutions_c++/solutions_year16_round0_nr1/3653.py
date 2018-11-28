#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int NMAX = 100000 + 7;
const int INF = 1000000000;



int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	int n;
	cin >> t;
	for (int testNumber = 1; testNumber <= t; testNumber++) {
		cin >> n;
		cout << "Case #" << testNumber << ": ";
		if (0==n) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		int digits[10];
		int cnt = 10;
		for (int i=0;i<=9;i++) {
			digits[i]=1;
		}
		int base = n;
		n=0;
		do {
			n+=base;
			int x = n;
			while (x) {
				int digit = x%10;
				if (digits[digit]) {
					digits[digit] = 0;
					cnt--;
				}
				x/=10;
			}
		} while (cnt);
		cout << n << endl;
	}
	return 0;
}