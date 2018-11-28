#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

bool isPal (long long x){
	long long y = 0, z = x;
	while (z){
		y = y * 10 + z % 10;
		z /= 10;
	}
	if (x == y) return true;
	return false;
}

int main(){
	vector <long long> vec;
	long long i;
	for (i = 1; i * i <= 100000000000000LL; i++)
		if (isPal (i) == true && isPal (i * i) == true) vec.push_back (i * i);
	int t, h = 0;
	freopen ("C.in", "r", stdin);
	freopen ("C.out", "w", stdout);
	scanf ("%d", &t);
	while (h < t){
		printf ("Case #%d: ", ++h);
		long long a, b;
		scanf ("%lld%lld", &a, &b);
		int ans = 0, n = vec.size(), i = 0;
		while (i < n && vec[i] <= b){
			if (vec[i] >= a) ans++;
			i++;
		}
		printf ("%d\n", ans);
	}
}

