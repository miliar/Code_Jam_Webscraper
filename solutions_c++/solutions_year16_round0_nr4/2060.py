#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int BASE = 1000;
int N, k, c, s;

vector<int> add(const vector<int> &a, const vector<int> &b) {
	int l1 = a.size(), l2 = b.size(), l = l1 > l2 ? l1:l2;
	vector<int> c(l);
	for (int i = 0; i < l; ++i) {
		if (i >= l1) c[i] = b[i];
		else if (i >= l2) c[i] = a[i];
		else c[i] = a[i] + b[i];
	}
	--l;
	for (int i = 0; i < l; ++i) {
		c[i+1] += c[i] / BASE;
		c[i] %= BASE;
	}
	for (; c[l] >= BASE; ++l) {
		c.push_back(c[l] / BASE);
		c[l] %= BASE;
	}
	return c;
}

vector<int> mult(const vector<int> &a, int b) {
	if (b == 0) {
		vector<int> zero(1, 0);
		return zero;
	}
	
	int l = a.size();
	vector<int> c(l);
	for (int i = 0; i < l; ++i) {
		c[i] = a[i] * b;
	}
	--l;
	for (int i = 0; i < l; ++i) {
		c[i+1] += c[i] / BASE;
		c[i] %= BASE;
	}
	for (; c[l] >= BASE; ++l) {
		c.push_back(c[l] / BASE);
		c[l] %= BASE;
	}
	return c;
}

vector<int>  newNum(int num) {
	vector<int> c(1, num);
	int l = 0;
	for (; c[l] >= BASE; ++l) {
		c.push_back(c[l] / BASE);
		c[l] %= BASE;
	}
	return c;
}

void print(const vector<int> &a) {
	int l = a.size();
	printf("%d", a[l-1]);
	for (int i = l-2; i >= 0; --i) {
		if (a[i] < 10) printf("00");
		else if (a[i] < 100) printf("0");
		printf("%d", a[i]);
	}
}

int main(int argc, char** argv) {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	scanf("%d", &N);
	for (int times = 1; times <= N; ++times) {
		printf("Case #%d: ", times);
		scanf("%d%d%d", &k, &c, &s);
		if (s * c < k) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		
		int n = (k + c - 1) / c;
		vector<int> base = newNum(1);
		vector<vector<int> > nums(n);
		for (int i = 0; i < n; ++i) nums[i] = newNum(1 + i * c);
		
		if (k < c) c = k;
		
		for (int i = 1; i < c; ++i) {
			base = mult(base, k);
			nums[0] = add(nums[0], mult(base, i));
			for (int j = 1; j < n; ++j) 
				if (j == n-1 && n * c - k >= c - i)
					nums[j] = add(nums[j], mult(base, c * (j - 1) + i + 1));
				else nums[j] = add(nums[j], mult(base, c * j + i));
		}
		for (int i = 0; i < n; ++i) {
			if (i) printf(" ");
			print(nums[i]);
		}
		printf("\n");
	}
	
	return 0;
}

