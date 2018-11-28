// C++ includes used for precompiling -*- C++ -*-

// Copyright (C) 2003-2013 Free Software Foundation, Inc.
//
// This file is part of the GNU ISO C++ Library.  This library is free
// software; you can redistribute it and/or modify it under the
// terms of the GNU General Public License as published by the
// Free Software Foundation; either version 3, or (at your option)
// any later version.

// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// Under Section 7 of GPL version 3, you are granted additional
// permissions described in the GCC Runtime Library Exception, version
// 3.1, as published by the Free Software Foundation.

// You should have received a copy of the GNU General Public License and
// a copy of the GCC Runtime Library Exception along with this program;
// see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see
// <http://www.gnu.org/licenses/>.

/** @file stdc++.h
*  This is an implementation file for a precompiled header.
*/

// 17.4.1.2 Headers

// C
#ifndef _GLIBCXX_NO_ASSERT
#include <cassert>
#endif
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#if __cplusplus >= 201103L
#include <ccomplex>
#include <cfenv>
#include <cinttypes>
#include <cstdalign>
#include <cstdbool>
#include <cstdint>
#include <ctgmath>
#include <cwchar>
#include <cwctype>
#endif

// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>

#if __cplusplus >= 201103L
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#endif
#include <unordered_map>

//#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define sz(v) (int)v.size()
#define all(c) (c).rbegin(),(c).rend()

vector<int> dec (vector<int> v) {
	for (int i = 0; i < sz(v); i++)
		if (v[i]) v[i]--;
	sort(all(v));
						while(sz(v) && !v.back()) v.pop_back();
	return v;
}

bool emp (vector<int> & v) {
	int ans = 0;
	for (int i = 0; i < sz(v); i++)
		ans += v[i];
	return ans;
}

int main ( ) {
	//freopen("1", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tc, t = 0, n;
	scanf("%d", &tc);
	while (tc--) {
		scanf("%d", &n);
		int ans = 0;
		vector<int> org(n);
		for (int i = 0; i < n; i++)
			scanf("%d", &org[i]);
		queue<pair<vector<int>, int>> q;
		q.push(make_pair(org, 0));
		set<vector<int>> vis;
		while (sz(q) && !ans) {
			int d = q.front().second;
			vector<int> v = q.front().first;
			q.pop();
			if (!emp(v)) ans = d;

			for (int i = 0; i < sz(v); i++) {
				for (int k = 0; k <= sz(v); k++) {
					if (i == k) continue;
					for (int j = 1; j < v[i]; j++) {
						if(k < sz(v) && v[i] - j < v[k] + j) break;
						vector<int> cur = v;
						cur[i] -= j;
						if (k < sz(v)) cur[k] += j;
						else cur.push_back(j);
						sort(all(cur));
						while(sz(cur) && !cur.back()) cur.pop_back();
						if (!vis.count(cur)) {
							vis.insert(cur);
							q.push(make_pair(cur, d + 1));
						}
						
					}
				}
			}

			q.push(make_pair(dec(v), 1 + d));
		}
		printf("Case #%d: %d\n", ++t, ans);
	}
}

