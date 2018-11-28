#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

long long gcd(long long a, long long b){
	//cout << a << b << endl;
	if (a < b){
		long long c = a;
		a = b;
		b = c;
	}
	if (b == 0)
		return a;
	return gcd(b, a % b);
}

int main()
{
	int n,lenb;
	long long a,b,g,ans,ans2;
	char c;
	cin >> n;
	for (int i = 1; i <= n; i++){
		cin >> a;
		cin >> c;
		cin >> b;
		//cout << gcd(a,b) << endl;
		g = gcd(a, b);
		a = a / g;
		b = b / g;

		ans = 0;
		while (((1 << ans) & b) != b && ans <= b) ++ans;
		ans2 = 0;
		while (1 << ans2 <= a) ++ans2;
		lenb = 0;
		while (1 << lenb <= b) ++lenb;

		if (ans > b || a > b || ans2 > 40 || ans > 40 || lenb > 40) {
			cout << "Case #" << i << ": impossible" << endl;
			continue;
		}else{
			cout << "Case #" << i << ": " << ans - ans2 + 1 << endl;
		}
	}
	return 0;
}