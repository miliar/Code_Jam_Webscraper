#include <iostream>
#include <set>
#include <cstdio>

using namespace std;

typedef long long ll ;

const ll MOD = 1000000007;

void solve(int C)
{
	ll N, x, y;
	bool flag = false;
	set<ll> st;

	scanf("%lld", &N);

	ll i = 1, cnt = 0;

	while(true)
	{
		x = N*i;
		cnt++;

		while(x > 0)
		{
			y = x%10;
			st.insert(y);
			x /= 10;
		}

		if(st.size() == 10)
			break;

		if(cnt > 100000)
	    {
	    	flag = true;
	    	break;
	    }
	    i++;
	}
	printf("Case #%d: ",C);
	if(flag)
		printf("INSOMNIA\n");
	else
		printf("%lld\n", N*cnt);
	return ;
}

int main()
{
	int test;
	scanf("%d", &test);
	
	for(int i = 0 ; i < test ; i++)
		solve(i+1);

	return 0;
}