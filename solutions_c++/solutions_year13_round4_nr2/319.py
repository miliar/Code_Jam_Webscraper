#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;

long long n, p, tmp, mp;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B_L.out", "w", stdout);
	
	int TextN = 0, TT = 0;
	cin >> TextN;
	while (TextN--) {
		cin >> n >> p;
		cout << "Case #" << ++TT << ": ";
		
		tmp = 1LL << n;
		if (p == tmp) {
			cout << tmp - 1 << " " << tmp - 1 << endl;
		} else {
			int k;
			for (mp = p, k = n; mp > 0; k--) 
				mp -= 1LL << (k - 1);
			cout << (1LL << (n - k)) - 2 << " ";
			
			for (mp = tmp, k = n; mp > p; k--) 
				mp -= 1LL << (k - 1);
			cout << tmp - (1LL << (n - k)) << endl;
		}
	}
	return 0;
}
