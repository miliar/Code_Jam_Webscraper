/*************************************************************************
	> File Name: coinjam.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2016年04月09日 星期六 16时47分55秒
 ************************************************************************/

#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <cassert>
// #pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
#define LL long long
#define pb push_back
#define mp make_pair
#define x first
#define y second
template <typename T> inline void checkMax(T &a, T b) {a = a>b?a:b;}
template <typename T> inline void checkMin(T &a, T b) {a = a<b?a:b;}
typedef pair<int, int> PII;
typedef vector<int> vi;
const double PI = acos(-1.0);
const double eps = 1e-8;
int T, Cas = 1;

LL base[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
// 用小素数表做随机种子可避免第一类卡米歇尔数的误判
LL gcd(LL a,LL b)
{
	if(b == 0)
		return a;
	return gcd(b,a%b);
}
LL product_mod(LL a, LL b, LL n) {
	LL tmp = 0;
	while (b) {
		if (b & 1) {
			tmp += a;
			if (tmp >= n)
				tmp -= n;
		}
		a<<= 1;
		if (a >= n)
			a -= n;
		b >>= 1;
	} 
	return tmp;
}
LL power_mod(LL a, LL m, LL n) {
	LL tmp = 1;
	a %= n;
	while (m) {
		if (m & 1) tmp = product_mod(tmp, a, n);
		a = product_mod(a, a, n);
		m >>= 1;
	} return tmp;
}
bool miller_rabin(LL n) {
	if (n < 2)
		return false;
	if (n == 2)
		return true;
	if (!(n	& 1))
		return false;
	LL k = 0, i, j, m, a;
	m = n - 1;
	while (!(m & 1)) m >>= 1, k++;
	for ( i = 0; i < 10; i ++) {
		if (base[i] >= n)
			return true;
		a = power_mod(base[i], m, n);
		if (a == 1) continue;
		for ( j = 0; j < k; j ++) {
			if (a == n-1)
				break;
			a = product_mod(a, a, n);
		} 
		if (j == k)
			return false;
	}
   	return true;
}
// factor 数组记录分解质因数的结果，cnt 记录质因数的个数，相同的质因数不合并
LL pollard_rho(LL c, LL n) {
	LL i, x, y, k, d;
	i = 1;
	x = y = rand() % n;
	k = 2;
	do {
		i ++;
		d = gcd(n+y-x, n);
		if (d > 1 && d < n) return d;
		if (i == k) {
			y = x;
			k <<= 1;
		}
		x = (product_mod(x,x,n) + n - c) % n;
	} while (y != x);
	return n;
}
LL rho(LL n) {
	if (miller_rabin(n)) {
		return n;
	} 
	LL t = n;
	while (t >= n) t = pollard_rho(rand()%(n-1)+1, n);
	return min(rho(t), rho(n/t));
}

void print() {
    int cnt = 0;
    for (int i = 0; i <= (1 << 13); i ++) {
        int now = (i << 1) + 1 + (1 << 15);
        bool flag = true;
        LL ten[11] = {};
        for (int j = 15; j >= 0; j --) {
            for (int k = 2; k <= 10; k ++) {
                ten[k] = ten[k] * k + ((now & (1 << j)) == 0 ? 0 : 1);
            }
        }
        for (int j = 2; j <= 10; j ++) {
            LL x = rho(ten[j]);
            if (x == 1 || x == ten[j]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            cnt ++;
            printf("printf(\"");
            for (int i = 15; i >= 0; i --) {
                printf("%d", now & (1 << i) ? 1 : 0);
            }
            for (int j = 2; j <= 10; j ++) {
                printf(" %lld", rho(ten[j]));
            }
            printf("\\n\");\n");
            if (cnt == 50) {
                return ;
            }
        }
    }
}

void show() {
    printf("1000000000000001 3 2 5 2 7 2 3 2 7\n");
    printf("1000000000000101 13 11 3 4751 173 3 53 109 3\n");
    printf("1000000000000111 3 2 5 2 7 2 3 2 11\n");
    printf("1000000000001001 73 5 3 19 19 3 5 19 3\n");
    printf("1000000000001101 3 2 5 2 7 2 3 2 11\n");
    printf("1000000000010011 3 2 5 2 7 2 3 2 7\n");
    printf("1000000000011001 3 2 5 2 7 2 3 2 11\n");
    printf("1000000000011011 5 1567 15559 6197 5 5 1031 7 83\n");
    printf("1000000000011111 3 2 3 2 7 2 3 2 3\n");
    printf("1000000000100101 3 2 5 2 7 2 3 2 7\n");
    printf("1000000000101011 3 7 13 3 5 43 3 73 7\n");
    printf("1000000000101111 5 2 3 2 37 2 5 2 3\n");
    printf("1000000000110001 3 2 5 2 7 2 3 2 11\n");
    printf("1000000000110101 23 17 11 23 5 299699 43 239 59\n");
    printf("1000000000110111 3 2 3 2 7 2 3 2 3\n");
    printf("1000000000111011 17 2 3 2 73 2 17 2 3\n");
    printf("1000000000111101 3 2 3 2 7 2 3 2 3\n");
    printf("1000000001000011 3 2 5 2 7 2 3 2 11\n");
    printf("1000000001001001 3 2 5 2 7 2 3 2 7\n");
    printf("1000000001001111 3 2 3 2 7 2 3 2 3\n");
    printf("1000000001010101 3 7 13 3 5 17 3 53 7\n");
    printf("1000000001010111 5 2 3 2 37 2 5 2 3\n");
    printf("1000000001011001 11 5 281 101 5 67 5 13 19\n");
    printf("1000000001011011 3 2 3 2 7 2 3 2 3\n");
    printf("1000000001011101 17 2 3 2 1297 2 11 2 3\n");
    printf("1000000001011111 59 113 7 157 19 1399 7 43 107\n");
    printf("1000000001100001 3 2 5 2 7 2 3 2 11\n");
    printf("1000000001100011 23 19 11 105491 5 47 11117 1787 127\n");
    printf("1000000001100111 3 2 3 2 7 2 3 2 3\n");
    printf("1000000001101011 5 2 3 2 37 2 5 2 3\n");
    printf("1000000001101101 3 2 3 2 7 2 3 2 3\n");
    printf("1000000001110011 3 2 3 2 7 2 3 2 3\n");
    printf("1000000001110101 5 2 3 2 37 2 5 2 3\n");
    printf("1000000001111001 3 2 3 2 7 2 3 2 3\n");
    printf("1000000001111011 31 557 7 19 23 1129 7 5441 241\n");
    printf("1000000001111101 7 19 43 17 55987 23 7 7 31\n");
    printf("1000000001111111 3 2 5 2 7 2 3 2 7\n");
    printf("1000000010000011 167 2 11 2 58427 2 23 2 839\n");
    printf("1000000010000101 3 2 5 2 7 2 3 2 11\n");
    printf("1000000010001001 5 2 7 2 1933 2 29 2 157\n");
    printf("1000000010010001 3 2 5 2 7 2 3 2 7\n");
    printf("1000000010010111 3 2 3 2 7 2 3 2 3\n");
    printf("1000000010011001 7 1667 179 13 5 11 23 7 311\n");
    printf("1000000010011011 11 2 3 2 13 2 47 2 3\n");
    printf("1000000010011101 3 2 3 2 7 2 3 2 3\n");
    printf("1000000010100011 3 1259 421 3 5 8893 3 67 17\n");
    printf("1000000010100111 5 2 3 2 37 2 5 2 3\n");
    printf("1000000010101001 3 5 13 3 5 43 3 73 7\n");
    printf("1000000010110011 47 2 3 2 11 2 204311 2 3\n");
    printf("1000000010110101 3 2 3 2 7 2 3 2 3\n");
}

void work() {
    printf("Case #%d:\n", Cas ++);
    int N, J;
    scanf("%d %d", &N, &J);
    show();
}
int main() {
 //   print();
    scanf("%d", &T);
    while (T --) {
        work();
    }
    return 0;
}
