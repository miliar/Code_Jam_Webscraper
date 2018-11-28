#include <iostream>

using namespace std;

bool p[1001];
bool f[1001];

bool isP(int x)
{
	int i = 10;
	while(x/i > 0)
		i*=10;
	i/=10;
	if(i == 1)
		return true;
	if(x/i == x%10)
		return isP(x%i/10);
	return false;
	
}

int main()
{
	int i;
	for(i = 1; i <= 1000; i ++)
	{
		if(isP(i))
			p[i] = true;
		else p[i] = false;
		f[i] = false;
	}
	for(i = 1; i*i <= 1000; i ++)
	{
		if(p[i] && p[i*i])
			f[i*i] = true;
	}
	int num[1001];
	num[0] = 0;
	for(i = 1; i <= 1000; i ++)
	{
		if(f[i])
			num[i] = num[i-1]+1;
		else
			num[i] = num[i-1];
	}
	int t;
	cin >> t;
	
	for(int CASE = 1; CASE <= t; CASE++)
	{
		int a, b;
		cin >> a;
		cin >> b;
		printf("Case #%d: %d\n", CASE, num[b]-num[a-1]);
	}
	return 0;
}