#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>
#define SI(x) scanf("%d" , &x)
#define SL(x) scanf("%lld" , &x)
#define SD(x) scanf("%lf" , &x)
#define SF(x) scanf("%f" , &x)
#define FI(i , s , e) for(i = s ; i < e ; i++)
#define FD(i , s , e) for(i = s ; i >= e ; i--)
#define PI(x) printf("%d\n" , x)
#define PL(x) printf("%lld\n" , x)
#define PD(x) printf("%lf\n" , x)
#define PF(x) printf("%f\n" , x)
#define VI vector<int>
#define VL vector<long long>
#define VVI vector<vector<int> >
#define VVL vector<vector<long long> >
#define priority_queue<int> PQI
#define priority_queue<long long> PQL
#define LL long long
#define N 1000000009
 
using namespace std;

int main()
{
	int t , n , i , j , k , d , o , p;
	SI(t);
	p = 1;
	while(t--) {
		SI(n);
		double arr[n + 1];
		double brr[n + 1];
		arr[0] = 0.0;
		brr[0] = 0.0;
		FI(i , 1 , n + 1)
			SD(arr[i]);
		FI(i , 1 , n + 1)
			SD(brr[i]);
		sort(arr , arr + n + 1);
		sort(brr , brr + n + 1);
		i = 1;
		j = 1;
		o = 0;
		while(i <= n && j <= n) {
			while(j <= n && brr[j] < arr[i])
				j++;
			if(j <= n)
				o++;
			j++;
			i++;
		}
		o = n - o;
		
		i = 0;
		j = n;
		k = n;
		d = 0;
		while(i <= j && j >= 1 && k >= 1) {
			while(j >= i && k >= 1 && arr[j] > brr[k]) {
				j--;
				k--;
			}
			if(j >= 1 && k >= 1) {
				d++;
				k--;
				i++;
			}
		}
		d = n - d;
		printf("Case #%d: %d %d\n" , p , d , o);
		p++;
	}
	return 0;
}