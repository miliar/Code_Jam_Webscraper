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

LL w[MAXN];
LL B;
int N;

double calc(LL mid)
{
	if(mid <= 0)	return -10.0;
	
	LL sum = (37 - N) * mid;
	int idx = 0;
	while(idx < N && w[idx] <= mid)
	{
		sum += mid - w[idx ++];	
	}	
	
	if(sum <= B && sum > 0)
	{
		double ret = - 10.0;
		for(int k = idx; sum <= B && k >= 0; -- k)
		{
			double tmp = mid * (37.0 - N) / (37.0 - N + k) * 36;
			for(int i = 0; i < k; ++ i)
			{
				tmp += (mid - w[i]) / (37.0 - N + k) * 36;	
			}
			ret = max(ret, tmp - sum);
			++ sum;
		}
//		cout << "mid  " << mid << " " << idx << " " << ret << endl;
		return ret;	
	}
	
	return -10.0;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int T;	cin >> T;
	
	for(int cas = 1; cas <= T; ++ cas)
	{
		cin >> B >> N;
		for(int i = 0; i < N; ++ i)
		{
			cin >> w[i];	
		}
		
		sort(w, w + N);
		
		if(N == 37)
		{
			int idx = 0;
			while(++ idx < N && w[idx] == w[idx - 1]);
			for(int i = idx; i < N; ++ i)
			{
				w[i - idx] = w[i];	
			}
			N -= idx;
		}
		
		printf("Case #%d: ", cas);
		
		if(N == 1)	
		{
			puts("0");
			continue;	
		}
		
		double ans = 0.0;
		LL low = 0, high = min(B + 1, w[N - 1] + 1);
		while(low + 1 < high)
		{
			LL mid = (low + high) / 2;
			double tmp = calc(mid);
			if(tmp > -1)
			{
				ans = max(ans, tmp);
				low = mid;
				ans = max(ans, calc(mid - 1));	
			}
			else	high = mid;
		}
		
		for(int i = 0; i < N; ++ i)
		{
			ans = max(ans, calc(w[i]));
			ans = max(ans, calc(w[i] - 1));	
		}
		
		printf("%.12f\n", ans);
	}
	
	
	return 0;	
}
