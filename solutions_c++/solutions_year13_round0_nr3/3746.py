#include<iostream>
#include<string>
#include<cstdio>
#include<cmath>

using namespace std;

bool check(unsigned long long x)
{
	char t[1000];
	int l = 0;
	while(x)
	{
		t[l++] = x%10;
		x/=10;
	}
	for(int i=0; i<l; ++i)
		if(t[i] != t[l-1-i])
			return false;
	return true;
}

int main()
{
	int T;
	freopen("32.in", "r", stdin);
	freopen("32.out","w", stdout);
	cin >> T;
	for(int cases = 1; cases <= T; ++ cases) {
		unsigned long long a, b;
		cin >> a >> b;
		unsigned long long ans = 0;
		for(unsigned long long x = 0; x*x <=b&&x<=b; ++x) {
			if(x*x <a) continue;
			if(!check(x)) continue;
			if(!check(x*x)) continue;
			++ans;
		}
		printf("Case #%d: %llu\n", cases, ans);
	}
	return 0;
}
