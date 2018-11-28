// A.cpp : Defines the entry point for the console application.
//

#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <unordered_set>

using namespace std;
#define ll long long
const ll MOD = 1000000007;


double calc(vector<double>& in, double end){
	ll totalTime = accumulate(in.begin(), in.end(), 0);
	double total = 0;
	for (int i = 0; i < in.size(); ++i){
		total += in[i] * in[i]/(double)2;
	}
	ll rep = end / totalTime;
	double result = total*rep;
	end -= rep*totalTime;
	for (ll i = 0; i < in.size(); ++i){
		ll rem = min(end, in[i]);
		result += rem *rem/ (double)2;
		if (rem == end)break;
		end -= rem;
	}
	return result;
}

inline string to_bin_str(ll n) {
	string str;
	while (n > 0) {
		str.push_back('0' + (n & 1));
		n >>= 1;
	}
	std::reverse(str.begin(), str.end());
	return str;
}

int main()
{
#if 0
	int T;
	cin>>T;
	for(int _t=1;_t<=T;++_t){
		double N, A, B;
		cin >> N >> A >> B;
		vector<double> C;
		C.resize(N);
		for (int i = 0; i < N; ++i)cin >> C[i];

		double a = calc(C, A);
		double b = calc(C, B);
		double result = (b - a) / (double)(B - A);
			cout << "Case #" << _t << ": " << fixed<<result << setprecision(8)<<endl;;
		cerr<< "Case #" << _t << ": " << result << endl;;

	}
#endif
	ll N = 16;
	ll lower = (1 << (N-1)) | 1;
	ll upper = (1 << N) - 1;
	int count = 0;
	int J = 50;
	unordered_set<ll> taken;
	cout << "Case #1:" << endl;
	while (count < J){
		ll val = rand() % (upper - lower) + lower;
		if ((val&1)==0||taken.find(val) != taken.end())continue;

		taken.insert(val);
		//cout << to_bin_str(val) << endl;
		vector<ll> result;
		for (int i = 2; i <= 10; ++i){
			ll tmp = val;
			ll inter = 0;
			ll add = 1;
			while (tmp){
				if (tmp & 1){
					inter += add;
				}
				add *= i;
				tmp >>= 1;
			}
			//cout << to_bin_str(val) << ";"<<i << "; " << inter << endl;

			ll div = -1;
			for (ll d = 2; d*d <= inter; ++d){
				if ((inter%d) == 0){
					div = d;
					break;
				}
			}
			if (div == -1){
				break;
			}
			result.push_back(div);
		}
		//cout << result.size() << endl;
		if (result.size() == 9){
			cout<<to_bin_str(val);
			for (int i = 0; i < result.size(); ++i){
				cout << " " << result[i];
			}
			cout << endl;
			++count;
			cerr << count << endl;
		}
	}
}



