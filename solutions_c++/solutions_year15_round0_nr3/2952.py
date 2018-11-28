#include <cstdlib>
#include <string>
#include <vector>
#include <iostream>
#include <assert.h>
#include <sstream>
using namespace std;

typedef pair<int, char> qq;

qq mul(qq q1, qq q2) {
	qq res;
	res.first = 1;
	if (q1.second == '1') {
		res.second = q2.second;
	}
	if (q2.second == '1') {
		res.second = q1.second;
	}

	if (q1.second == q2.second && q1.second != '1') {
		res.first = -1;
		res.second = '1';
	}
	if (q1.second == 'i' && q2.second == 'j') {
		res.first = 1;
		res.second = 'k';
	}
	if (q1.second == 'i' && q2.second == 'k') {
		res.first = -1;
		res.second = 'j';
	}
	if (q1.second == 'j' && q2.second == 'i') {
		res.first = -1;
		res.second = 'k';
	}
	if (q1.second == 'j' && q2.second == 'k') {
		res.first = 1;
		res.second = 'i';
	}
	if (q1.second == 'k' && q2.second == 'i') {
		res.first = 1;
		res.second = 'j';
	}
	if (q1.second == 'k' && q2.second == 'j') {
		res.first = -1;
		res.second = 'i';
	}
	res.first *= q1.first * q2.first;
	return res;
}

qq qqpow(qq q, int k) {
	qq res = {1, '1'};
	for (int i = 0; i < k; ++i) {
		res = mul(res, q);
	}
	return res;
}
string qqstr(qq q) {
	stringstream ss;
	if (q.first == -1) {
		ss << "-";
	} else if (q.first == 1) {
	} else assert(false);
	ss << q.second;
	return ss.str();
}

qq qqrdiv(qq q1, qq q2) {
	qq res;
	string ss = "1ijk";
	for(int s = -1; s <= 1; ++s) {
		if (s == 0) continue;
		qq x; x.first = s;
		for(char c : ss) {
			x.second = c;
			if (mul(q2, x) == q1) {
				return x;
			}
		}
	}
	cout << qqstr(q1) << " / " << qqstr(q2) << endl;
	assert(false);
}
qq div_cache[3]['z'][3]['z'];
qq pow_cache[3]['z'][4];

inline qq qqdiv_cache(qq q1, qq q2) {
	return div_cache[q1.first + 1][q1.second][q2.first + 1][q2.second];
}
inline qq qqpow_cache(qq q1, int k) {
	assert(k < 4);
	return pow_cache[q1.first + 1][q1.second][k];
}

int main(int argc, char** argv) {
	int T;
#if 1
//	T = 0;
	vector<qq> qqs;
	qqs.push_back({1, '1'});
	qqs.push_back({1, 'i'});
	qqs.push_back({1, 'j'});
	qqs.push_back({1, 'k'});
	qqs.push_back({-1, '1'});
	qqs.push_back({-1, 'i'});
	qqs.push_back({-1, 'j'});
	qqs.push_back({-1, 'k'});

	
	for (int i = 0; i < qqs.size(); ++i) {
		for (int j = 0; j < qqs.size(); ++j) {
			div_cache[qqs[i].first + 1][qqs[i].second][qqs[j].first + 1][qqs[j].second] = qqrdiv(qqs[i], qqs[j]);
		}
		for(int k = 0; k < 4; ++k) {
			pow_cache[qqs[i].first+1][qqs[i].second][k] = qqpow(qqs[i], k);
		}
	}
//	return 0;
#endif

	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int L, X;
		string S;
		cin >> L >> X >> S;
		vector<qq> partials(L + 1);
		partials[0] = qq(1, '1');
		for (int i = 1; i <= L; ++i) {
			partials[i] = mul(partials[i - 1],qq(1, S[i - 1]));
			assert(partials[i].first == 1 || partials[i].first == -1);
		}
		for (int full1 = 0; full1 < 4 && full1 < X; ++full1)
			for (int use1 = 0; use1 < L; ++use1) {
				for (int full2 = 0; full2 < 4 && full2 + full1 < X; ++full2)
					for (int use2 = 0; use2 < L; ++use2) {
						if (full1 + full2 + (use1+use2)/L > X) {
							continue;
						}
						//if (use1 != 1 || use2 != 1) continue;
						//cout << "here "<<use1 << " " << use2 << endl;
						qq q1 = mul(qqpow_cache(partials[L], full1), partials[use1]);
						//cout << "q1 = " << qqstr(q1) << endl;
						if (q1.first != 1 ||  q1.second != 'i') continue;
						
						int full12 = (full1 * L + full2 * L + use1 + use2);
						qq q2 = mul(qqpow_cache(partials[L], (full12 / L) % 4), partials[full12 % L]);
						q2 = qqdiv_cache(q2, q1);
						if (q2.first != 1 ||  q2.second != 'j') continue;
						
						qq q3 = qqdiv_cache(qqpow_cache(partials[L], X % 4), mul(q1, q2));
						if (q3.first != 1 ||  q3.second != 'k') continue;
						
						cout << "Case #" << t << ": " << "YES" << endl;
						goto next;
					}
			}
		cout << "Case #" << t << ": " << "NO" << endl;
		next:
		continue;
	}

	return 0;
}

