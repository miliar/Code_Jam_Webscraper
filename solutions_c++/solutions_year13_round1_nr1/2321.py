
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(decltype((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))

#define PROB_ID "A"
#define INPUT_SIZE "small" //"large" //  

int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);
		
	freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
  freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);

	int T; 
	scanf("%d\n", &T); // remember to put \n

	rep(i,T) {
		 unsigned ll r, t;

		// input
		scanf("%lld%lld\n", &r, &t); 
    ld r1 = (ld) r;
    ld t1 = (ld) t;
		// processing
    ld num =   ( ( 1.0 - 2.0 * r1 + sqrt( ((2.0 * r1 - 1.0) * (2.0 * r1 - 1.0)) + (8.0 * t1))) / 4.0 );
    //unsigned ll num =  (1 - 2 * r + (unsigned ll)sqrt( (ld)( ((2 * r - 1) * (2 * r - 1)) + (8 * t)))) / 4 ;

		printf("Case #%d: %lld\n", i + 1, (ll)num);

	}


	return 0;
}

