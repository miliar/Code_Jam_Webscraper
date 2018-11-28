#include<iostream>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<cstring>
#include<cctype>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<utility>
#include<string>
#include<ctime>
#include<numeric>
#include<functional>
using namespace std;

#define eps 1e-8
#define PI 3.1415926
#define LL long long
#define ULL unsigned long long
#define MP make_pair
#define wait system( "pause" );

#define _FIO_

void swap(int& a, int& b) {
	a = a ^ b;
	b = a ^ b;
	a = a ^ b;
}

int main() {
#ifdef _FIO_
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _FIO_
	int t;
	scanf("%d", &t);
	for (int ca = 1; ca <= t; ++ca) {
		int x, r, c;
		scanf("%d%d%d", &x, &r, &c);
		if (r > c)
			swap(r, c);
		bool ans = false;
		switch (x) {
		case 1:
			ans = true;
			break;
		case 2:
			ans = !((r * c) & 1);
			break;
		case 3:
			switch (r) {
			case 1:
				ans = false;
				break;
			case 2:
				ans = c == 3;
				break;
			case 3:
				ans = true;
				break;
			case 4:
				ans = false;
				break;
			default:
				break;
			}
			break;
		case 4:
			switch (r) {
			case 1:
			case 2:
				ans = false;
				break;
			case 3:
				ans = c == 4;
				break;
			case 4:
				ans = true;
				break;
			default:
				break;
			}
			break;
		default:
			break;
		}
		printf("Case #%d: %s\n", ca, ans ? "GABRIEL" : "RICHARD");
	}
#ifdef _FIO_
	fclose(stdin);
	fclose(stdout);
#endif // _FIO_
	return 0;
}
