﻿#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#define _SCL_SECURE_NO_WARNINGS

//#define _CRT_RAND_S

//#include <windows.h>
//#include <tchar.h>
//#include <atlbase.h>
//#include <winerror.h>

//#define BOOST_FILESYSTEM_NO_DEPRECATED
//#include <boost/filesystem.hpp>
//#include <boost/filesystem/fstream.hpp>
//#include <boost/regex.hpp>
//#include <boost/algorithm/string.hpp>

#include <type_traits>
#include <stdint.h>
#include <climits>
#include <ctime>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <vector>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <algorithm>

#include <thread>
#include <mutex>
#include <atomic>
#include <condition_variable>
#include <ppl.h>

#include <unordered_set>
#include <unordered_map>

#include "gmp_helpers.h"

#include "concurrency/concurrency.h"
#include "algorithm/collections/collections.h"
#include "algorithm/hash/std_tuple_hash.h"
#include "algorithm/math/base.h"
#include "algorithm/math/combinatorics.h"
#include "algorithm/math/comb_primes.h"
#include "algorithm/math/modulos.h"
#include "algorithm/math/polynoms.h"
#include "algorithm/math/primes.h"
#include "algorithm/math/recurrence.h"
#include "algorithm/math/reduce.h"
#include "algorithm/math/sums.h"
#include "structure/math/complex.h"
#include "structure/math/fraction.h"
#include "structure/math/matrix.h"
#include "structure/math/modulo.h"
#include "structure/math/polynom.h"
#include "structure/math/prime_holder.h"
#include "structure/math/quadratic.h"
#include "structure/math/vector3d.h"
#include "structure/math/vectorNd.h"
#include "structure/math/fenwick_tree.h"
#include "structure/graph/disjoint_set.h"

using namespace std;
using namespace tr1;
using namespace concurrency;

using namespace altruct::math;
using namespace altruct::collections;
using namespace altruct::concurrency;
using namespace altruct::graph;

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<ll, ll> pll;
typedef long double ld;

typedef fraction<ll> frac;
typedef moduloX<int> modx;
typedef modulo<int, 1000000123> mod;
typedef polynom<mod> poly;
typedef moduloX<poly> polymod;
typedef vector3d<double> vect3d;
typedef altruct::math::complex<int> gaussian;

// uses my own open source library: https://github.com/plamenko/altruct

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int n; cin >> n;
		set<pii, std::greater<pii>> s;
		int tot = 0;
		for (int i = 0; i < n; i++) {
			int c; cin >> c;
			s.insert({c, i});
			tot += c;
		}
		cout << "Case #" << t << ": ";
		while (!s.empty()) {
			auto z1 = *s.begin(); s.erase(s.begin());
			cout << char('A' + z1.second);
			tot--; --z1.first;
			if (!s.empty() && (2 * s.begin()->first > tot)) {
				auto z2 = *s.begin(); s.erase(s.begin());
				cout << char('A' + z2.second);
				tot--; --z2.first;
				
				if (!s.empty() && (2 * s.begin()->first > tot)) printf("ERROR1\n");
				if ((2 * z1.first > tot)) printf("ERROR2\n");
				if ((2 * z2.first > tot)) printf("ERROR3\n");
				
				if (z2.first > 0) s.insert(z2);
			}
			if (z1.first > 0) s.insert(z1);
			cout << " ";
		}
		cout << endl;
	}
	return 0;
}
