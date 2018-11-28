#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define FOR(k,a,b) for(typeof(a) k=(a); k <= (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define REPD(k,a) for(int k=(a)-1; k >= 0; --k)
#define PB push_back 
#define MP make_pair

LL rstB[1001];

pair<LL, int> WhoCan(const LL* barbers, LL B, LL N, LL t)
{
	LL cntOfBarbed = 0;
	int iFirst = -1;
	for (int i = 0; i < B; ++i) {
		auto ti = t / barbers[i];
		rstB[i] = t % barbers[i];
		if (rstB[i] != 0) {
			ti++;
		}
		else if (iFirst == -1) {
			iFirst = i;
		}
		cntOfBarbed += ti;
	}
	if (cntOfBarbed < N) {
		for (int i = 0; i < B; ++i) {
			if (rstB[i] == 0) {
				cntOfBarbed++;
				if (cntOfBarbed == N) {
					iFirst = i;
					break;
				}
			} 
		}
	}
	
	return make_pair(cntOfBarbed, iFirst);
}

int problemb() {
	int res = -1;
	LL barbers[1001];
	LL N, B;
	cin >> B >> N;
	for (auto i = 0; i < B; ++i) cin >> barbers[i];
	int maxBarb = 0;
	for (auto i = 1; i < B; ++i) {
		if (barbers[i] > barbers[maxBarb]) maxBarb = i;
	}
	LL r = barbers[maxBarb] * N;
	LL l = 0;

	while (r - l > 1) {
		LL mid = (r + l) / 2;
		auto bb = WhoCan(barbers, B, N, mid);
		//cout << endl << "T: " << mid << " " << bb.first << " " << bb.second;
		if (bb.first >= N) {
			r = mid;
		} else {
			l = mid;
		}
	}
	auto bbl = WhoCan(barbers, B, N, l);
	//cout << endl << "T: " << l << " " << bbl.first << " " << bbl.second;
	auto bbr = WhoCan(barbers, B, N, r);
	//cout << endl << "T: " << r << " " << bbr.first << " " << bbr.second;
	if (bbl.first >= N) {
		return bbl.second;
	}
	return bbr.second;
}

int main()
{
	int T;
	cin >> T;
	for (auto t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": " << (1 + problemb()) << endl;
	}
	
	return 0;
}

