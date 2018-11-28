#include<iostream>
#include<cstdio>
#include<memory.h>
#include<string>
#include<vector>
using namespace std;

const int MAXN = 10000005;
vector<long long> vec;

bool chk(long long x)
{
	string tmp = "";
	while(x)
	{
		tmp += x%10+'0';
		x /= 10;
	}
	
	for(int i = 0, j = tmp.length()-1; i < j; i ++, j --)
		if(tmp[i] != tmp[j])
			return false;
	return true;
}

void init()
{
	vec.clear();
	for(int i = 1; i < MAXN; i ++)
	{
		long long tmp = i; tmp *= i;
		if(chk(i) && chk(tmp))
			vec.push_back(tmp);
	}
}

int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	
	init();

	int cas;
	scanf("%d", &cas);
	for(int t = 1; t <= cas; t ++)
	{
		long long a;
		cin >> a;
		long long b;
		cin >> b;
		
		int cnt = 0;
		for(int i = 0; i < vec.size(); i ++)
			if(a<=vec[i] && vec[i]<=b)
				cnt ++;
		
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
