#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

//global variables
bool isPalindrome(int x) {
        if (x < 0) return false;
        int d = 1;
        while (x / d >= 10) d *= 10;
        while (x != 0) {
            int l = x / d; //highest digit
            int r = x % 10; //lowest digit
            if (l != r) return false;
            x = (x % d) / 10; //delete the highest and loweset digit
            d /= 100; 
        }
        return true;
    }
int sqrt(int x) {
        if(x < 2) return x;
        long long l = 0;
        long long u = 1 + (x / 2);
        while(l +1 < u) {
            long long m = l + (u - l) / 2;
            long long p = m * m;
            if(p > x)
                u = m;
            else if(p < x)
                l = m;
            else
                return m;
        }
        return (int)l;
    }
int main() {
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	scanf("%d", &t);  //case num
	int a, b;
	FOR(test, 1, t) {
		scanf("%d%d", &a, &b);  //range
	
		int total=0;

		FOR(n, a, b){
			if (isPalindrome(n)==true) {
				int temp=sqrt(n);
				//printf("%d\n ", temp);

				 if (isPalindrome(temp)==true && temp*temp==n){
					total++;
			}
		  }
		}
		
		
		
		printf("Case #%d: ", test); //test cases

				printf("%d ", total); //results

			printf("\n");
		
	}

	exit(0);
}
