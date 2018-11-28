#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <sstream>
#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <LL> VL;

const int MAXN = 110;

int N;
LL P;

LL getHighest(LL key)
{
	LL cnt = (1LL << N) - key;
	for(int i = 0; ; ++ i)
		if((1LL << i) > cnt)
			return (1LL << N - i + 1) - 1;
}

LL getLowest(LL key)
{
	LL cnt = 1 + key;
	for(int i = 0; ; ++ i)
		if((1LL << i) > cnt)
			return (1LL << N) - (1LL << N - i + 1);	
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	
	int T;	cin >> T;
	
	for(int cas = 1; cas <= T; ++ cas)
	{
		cin >> N >> P;
		
		LL low = 0, high = (1LL << N);
		while(low + 1 < high)
		{
			LL mid = (low + high) >> 1;
			if(getLowest(mid) < P)	low = mid;
			else	high = mid;	
		}
		
		cout << "Case #" << cas << ": " << low << " ";
		
		low = 0, high = (1LL << N);
		while(low + 1 < high)
		{
			LL mid = (low + high) >> 1;
			if(getHighest(mid) < P)	low = mid;
			else	high = mid;	
		}
		
		cout << low << endl;
	}
	
	
	return 0;	
}
