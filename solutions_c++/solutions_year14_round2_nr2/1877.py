// Ilya Shakirov

#pragma comment(linker, "/STACK:836777216")

#define INF (long long)1e18
#define EPS 1e-15
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#include <memory.h>

using namespace std;

const int MAX_N = 100;

int T;
int A, B, K;



int main()
{
#ifndef ONLINE_JUDGE
 freopen("input.txt", "r", stdin);
 freopen("output.txt", "w", stdout);
#endif
 cin >> T;
 for (int test = 0; test < T; test++) {
	 cin >> A >> B >> K;
	 int ans = 0;
	 for (int i = 0; i < A; i++)
		 for (int j = 0; j < B; j++)
			 if ((i & j) < K)
				 ans++;
  	  cout << "Case #" << test + 1 << ": " << ans << '\n';	
 }

 
 return 0;
}