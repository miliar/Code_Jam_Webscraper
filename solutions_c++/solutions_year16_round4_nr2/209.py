#include <cmath>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include "gmpxx.h"
using namespace std;
typedef long long ll;

//typedef mpz_class Int;
typedef mpf_class Float;
//typedef double Float;

#define ALL(c) (c).begin(),(c).end()
#define SORT(a) sort(a.begin(), a.end())
#define UNIQ(a) a.resize(unique(a.begin(), a.end()) - a.begin())

Float calc_tie(vector<Float> &p)
{
	int k=p.size();
	vector<Float> pp(k+2, 0);
	pp[0] = 1.0;
	for(int i=0; i<p.size(); ++i)
	{
		vector<Float> pp2(k+2, 0);
		for(int j=0; j<=k; ++j)
		{
			pp2[j+1] += pp[j]*p[i];
			pp2[j]   += pp[j]*(1.0-p[i]);
		}
		swap(pp, pp2);
	}
	return pp[k/2];
}


int main() {
	int t;
	
	cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		int n, k;
		cin >> n >> k;
		vector<Float> p(n);
		for(int i=0; i<n; ++i)
		{
			double x;
			cin >> x;
			p[i] = x;
		}
		SORT(p);
		//printv(p);
		
		Float bestp = 0.0;
		for(int l=0; l<=k; ++l)
		{
			vector<Float> p2;
			for(int i=0; i<l; ++i)
				p2.push_back(p[i]);
			for(int i=n-1; n-(k-l)<=i; --i)
				p2.push_back(p[i]);
			ASSERT(p2.size() == k);

			Float v = calc_tie(p2);
			if(bestp < v)
				bestp = v;
		}

		double ans = bestp.get_d();
		
		//cout << "Case #" << tt << ": " << ans << "\n";
		printf("Case #%d: %.10lf\n", tt, ans);
		cout.flush();
	}

	return 0;
}
