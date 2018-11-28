//This code was writen by Aliaksandr Driapko (sdryapko)
#include<sstream>
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<map>                             	
#include<set>               
#include<string>
#include<string.h>  
#include<deque>
#include<ctime>
#define gcd(a,b) __gcd((a), (b))
#define sqr(a) ((a) * (a))
#define odd(a) ((a) & 1)
#define pw2(x) (1ll << (x))
#define bits(x) __builtin_popcountll(1ll * (x))
#define F first
#define S second
const int maxi = 2000000000;              
const int maxq = 1000000000;
const double eps = 1e-10;       
const double pi = 3.1415926535897932;
const double inf = 1e+18;
const int mo = 1000000007;
const int maxn = 500000;
using namespace std;
int t, k;
string s;
int main(){                 
        freopen("input.txt", "r", stdin);      
        freopen("output.txt", "w", stdout);
        cin >> t;
        for (int tt = 1; tt <= t; ++tt) {
        	cin >> k >> s;
        	int sum = 0, ans = 0;
        	for (int i = 0; i <= k; ++i) if (sum >= i && s[i] >= '1') {
        		sum += s[i] - '0';
        	}  else {
        		if (s[i] != '0') {
        			ans += (i - sum);
        			sum += (i - sum);
        			sum += s[i] - '0'; 
        	        }
        	}
        	printf("Case #%d: %d\n",tt,ans);
        }
       	return 0;
}
