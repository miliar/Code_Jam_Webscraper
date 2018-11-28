#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>


//#include <unordered_map>

using namespace std;

char s[1000001];
int a[10001];
int get_ans(int x, int lvl) {
	if (x <= lvl)
		return 0;
	return  x / lvl - (x%lvl == 0);
}

int main() {
	freopen("input.txt", "r+", stdin);
	freopen("output.txt", "w+", stdout);
	

	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; i++) {
		
		int n;
		scanf("%d", &n);
		
		int mx = 0;
		for (int i = 0; i < n; i++) {
			int x;
			scanf("%d", &a[i]);
			if (a[i] > mx)
				mx = a[i];
		}

		int left = 1; 
		int right = mx;
		while (left != right) {
			int m = (left + right) >> 1;
			int m1 = (left + m) >> 1;
			int m2 = right - m1 + left;
			int zoom = 5;
			//for (int z = 1, end = mx; z <= end; z++) {
			int al = left, ar = right, am1 = m1, am2 = m2;

			for (int j = 0; j < n; j++) {
				al += get_ans(a[j], left);
				am1 += get_ans(a[j], m1);
				am2 += get_ans(a[j], m2);
				ar += get_ans(a[j], right);
			}

			if (am1 < mx)
				mx = am1;

			if (am2 < mx)
				mx = am2;
			
			if (al <= am1 && am1 <= am2) {
				right = m2 - 1;
			}
			else if (al >= am1 && am2 <= ar) {
				left = m1;
				right = m2 - 1;
			}
			else {
				left = m1;
			}
		}

		printf("Case #%d: %d\n", i, mx);
	}

	return 0;
}