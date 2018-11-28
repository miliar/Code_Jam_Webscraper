#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

#define LL __int64
#define sz 10000000
#define mx 10000001
LL tb[10000];

bool is_pal(LL n){
	char s[20];
	sprintf(s, "%I64d", n);
	int len = strlen(s);
	for (int i = 0, int j = len-1; i < j; ++i,--j)
	{
		if (s[i] != s[j])
		{
			return false;	
		}
	}
	return true;
}

int main(){

	LL t, a, b, cnt, cas = 1,Cnt = 0,i;

	freopen("iii.txt", "r", stdin);
	freopen("o.txt", "w", stdout);

	for (i = 1; i < mx; ++i)
	{
		if (is_pal(i) && is_pal(i*i))
		{
			tb[Cnt++] = i*i;
			//printf("%I64d > %I64d\n",i,i*i);
		}
	}

	scanf("%I64d", &t);
	while(t--){
		scanf("%I64d %I64d", &a, &b);

		cnt = 0;
		for (i = 0; i < Cnt; ++i)
		{			
			if(tb[i] > b)
				break;
			else if (tb[i] >= a)
			{
				cnt++;
			}
		}
		printf("Case #%I64d: %I64d\n", cas++, cnt);
	}




	return 0;
}