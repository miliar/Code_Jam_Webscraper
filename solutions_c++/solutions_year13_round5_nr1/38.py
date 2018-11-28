#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

const int N = 37;

double ret;
long long B;

double calc(const vector<long long>& x, int i, long long m)
{
	long long s1 = 0, s2 = 0;
	for (int j = 0; j <= i; ++j)
		s1 += m - x[j];
	for (int j = i + 1; j < N; ++j)
		if (x[j] <= m)
			s2 += m + 1 - x[j];
	if (s1 + s2 > B)
		return 0;
	double t = double(s1) / (i + 1) * 36 - s1 - s2;
	if (t > ret)
		ret = t;	
	return t;
}

void work()
{
	int n;	
	cin >> B >> n;
	vector<long long> x;
	while (n--) {
		long long y;
		cin >> y;
		x.push_back(y);
	}
	while (x.size() < N)
		x.push_back(0);
	sort(x.begin(), x.end());	
	ret = 0;
	for (int i = 0; i < N; ++i) {		
		long long lef = x[i], rig = x[i] + B;
		while (lef + 10 < rig) {
			long long m1 = lef + (rig - lef) / 3;
			long long m2 = rig - (rig - lef) / 3;
			if (calc(x, i, m1) < calc(x, i, m2))
				lef = m1;
			else
				rig = m2;
		}
		while (lef <= rig) {
			calc(x, i, lef);
			++lef;
		}		
	}
	cout << fixed;
	cout.precision(15);
	cout << ret;
}

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        work();
        printf("\n");
    }
    
    return 0;
}

