#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <string>
#include <memory.h>
using namespace std;

#include <cctype>
#include <cstdio>
#include <cstdarg>
#include <ctime>
#include <cmath>
#include <cassert>


const int INF = (1 << 30) - 1;
const float PI = (float)acos(-1.0);
const float EPS = 1e-5;
const float BASE2 = 1.0/log(2);

int cases;
string S;
vector<char> ans;
int n;


int deal(int l, int r, int k)
{
	if (l >= n) return -1;
	if (l > r) return -1;
	//cout << l << " " << r << " " << k << endl;
	int z = l;
	int ss = 1;
	int first, last;
    first = last = l;
	for (int i = l+1; i <= r; i++) {
		if (S[z] < S[i]) {
			z = i;
			ss = 1;
			first = i;
			last = i;
		}
		else if (S[z] == S[i]) {
			++ss;
			last = i;
		}
	}
	int j = k;
	ans[k] = S[z];
	for (int i = last+1; i <= r; i++) {
		ans[k+i-l] = S[i];
	}
	deal(l, last-1, k+1);
//	deal(last+1,r, k+last-l+1);
}

int main ()
{
	scanf("%d", &cases);
	for (int k = 1; k <= cases; k++) {
		cin >> S;
		n = S.length();
		ans.resize(n);
		printf("Case #%d: ", k);
		deal(0,n-1,0);
		for (int i = 0; i < n; i++) {
			printf("%c", ans[i]);
		}
		printf("\n");
	}
	return 0;
}


