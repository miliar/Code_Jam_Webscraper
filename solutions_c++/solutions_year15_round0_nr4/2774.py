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
int tt, x, n, m;
int main(){                 
        freopen("input.txt", "r", stdin);      
        freopen("output.txt", "w", stdout);
        cin >> tt;
        for (int t = 1; t <= tt; ++t) {
        	cin >> x >> n >> m;
        	if (x == 1) {
        		printf("Case #%d: GABRIEL\n", t);
       		}
       		if (x == 2) {
       			if (n * m % 2 == 0)  printf("Case #%d: GABRIEL\n", t); else 
       			printf("Case #%d: RICHARD\n", t);
       		}	
       		if (x == 3) {
       			if (n < 3 && m < 3) {
       				printf("Case #%d: RICHARD\n", t);
       			} else if (n != 3 && m != 3) {
       				printf("Case #%d: RICHARD\n", t);
       			} else {
       				if (n != 3) swap(n, m);
       			        if (m == 1) {
       			        	printf("Case #%d: RICHARD\n", t);
       		                } else {
       	                		printf("Case #%d: GABRIEL\n", t);
       	                        }
       			}
       		}
       		if (x == 4) {
       			if (n * m % 4 != 0) {
       				printf("Case #%d: RICHARD\n", t);
       			} else if (n < 4 && m < 4) {
       				printf("Case #%d: RICHARD\n", t);
       			} else {
       				if (n != 4) swap(n, m);
       			        if (m < 3) printf("Case #%d: RICHARD\n", t);
       			        else printf("Case #%d: GABRIEL\n", t);
       			}
       	
       		}
        
        }
       	return 0;
}
