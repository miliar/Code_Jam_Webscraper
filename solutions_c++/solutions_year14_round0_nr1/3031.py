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
#define FI(i , s , e) for(i = s ; i < e ; i++)
#define FD(i , s , e) for(i = s ; i >= e ; i--)
#define PI(x) printf("%d\n" , x)
#define PL(x) printf("%lld\n" , x)
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
	int t , i , j , k , n , a , b , p;
	SI(t);
	p = 1;
	int arr[5][5];
	while(t--) {
		SI(a);
		int crr[20];
		FI(i , 1 , 5)
			FI(j , 1 , 5)
				SI(arr[i][j]);
		FI(i , 1 , 5)
			crr[arr[a][i]] = 1;
		
		SI(b);
		FI(i , 1 , 5)
			FI(j , 1 , 5)
				SI(arr[i][j]);
		j = 0;
		FI(i , 1 , 5)
			if(crr[arr[b][i]] == 1) {
				k = arr[b][i];
				j++;
			}
		
		printf("Case #%d: " , p);
		p++;
		if(j == 1)
			PI(k);
		else if (j > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}