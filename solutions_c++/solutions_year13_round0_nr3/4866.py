#include <iostream>
#include <cstdio>
using namespace std;

int l,r;
bool check(int x)
{
	int y = x;
	int z = x%10;
	while(y>10)y/=10;
	return y==z && l<=x && x<=r;
}
int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int T;cin >> T;
	for(int cases = 1;cases <= T; ++cases)
	{
		cin >> l >> r;
		int ans = 0;
		for(int i = 1;i < 10; ++i)
			if(check(i*i))++ans;
		if(check(11*11))++ans;
		if(check(22*22))++ans;
		printf("Case #%d: %d\n",cases,ans);
	}
}
