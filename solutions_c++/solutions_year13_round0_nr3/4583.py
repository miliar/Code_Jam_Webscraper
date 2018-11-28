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

#define sz 1000
#define mx sqrt(sz)+10

bool is_pal(int n){
	char s[5];
	sprintf(s, "%d", n);
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

bool is_ps(int n){
	int tmp = sqrt(n);
	if (tmp * tmp == n)
	{
		return true;
	}
	return false;
}

int main(){

	int t, a, b, cnt, cas = 1, tb[sz],Cnt = 0,i;

	freopen("i.txt", "r", stdin);
	freopen("o.txt", "w", stdout);


	for (i = 1; i < mx; ++i)
	{
		if (is_pal(i) && is_pal(i*i))
		{
			tb[Cnt++] = i*i;
		}
	}


	scanf("%d", &t);
	while(t--){
		scanf("%d %d", &a, &b);

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
		printf("Case #%d: %d\n", cas++, cnt);
	}




	return 0;
}