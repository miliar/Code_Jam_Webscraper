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
	int n , i , j , k , t , l , l1 , ca , cb , x;
	string a , b  , s;
	SI(t);
	x = 1;
	while(t--) {
		SI(n);
	/*	string arr[n];
		l = 0;
		FI(i , 0 , n) {
			cin >> arr[i];
			if(arr[i].length() > l) {
				s = arr[i];
				l = s.length();
				k = i;
			}
		}
		FI(i , 0 , n) {
			if(i != k) {
				a = arr[i];
				l1 = a.length();
				while()
			}
		}
		*/
		cin >> a;
		cin >> b;
		i = 0;
		j = 0;
		ca = 0;
		cb = 0;
		k = 0;
		char c;
		while(i < a.length() && j < b.length()) {
			ca = 0;
			cb = 0;
			if(a[i] == b[j]) {
				c = a[i];
				while(i < a.length() && a[i] == c) {
					ca++;
					i++;
				}
				while(j < b.length() && b[j] == c) {
					cb++;
					j++;
				}
				k += abs(ca - cb);
			}
			else {
				break;
			}
		}
		if(i == a.length() && j == b.length()) {
			printf("Case #%d: %d\n" , x , k);
		} else {
			printf("Case #%d: Fegla Won\n" , x);
		}
		x++;
	}
	return 0;
}











