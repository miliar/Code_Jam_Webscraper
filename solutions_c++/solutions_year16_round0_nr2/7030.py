#include <iostream>
#include <cstdio>
#include <climits>
#include <cstring>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <list>
#include <cmath>
#include <numeric>
#include <utility>
#include <algorithm>
using namespace std;

#define BUF 1001
#define LEN 400
#define MOD 1000000007
#define PI 3.1415926535
#define lu unsigned long long int
#define ll long long int
#define pp pair<long long int, long long int>
#define vp vector< pp >
#define vl vector< ll >
#define vi vector< long int >
#define vvi vector< vi >
#define qi queue< int >
#define st stack< long int >
#define bt bitset<100>
#define pb(n) push_back(n)
#define setl set<long int>

bool sortfunc(long long int i, long long int j)
{
	return (fabs(i)<fabs(j));
}

typedef struct
{
	int x,y;
}loc;

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int c = 0; c < t; ++c)
	{
		char s[BUF],red[BUF];
		scanf("%s",s);
		int len = strlen(s),k=0, ans = 0;

		red[k++] = s[0];
		for (int i = 1; i < len; ++i)
			if(s[i] != s[i-1])
				red[k++] = s[i];

		red[k] == '\0';
		// printf("%s\n", red);

		for (int i = 0; i < k-1; ++i)
		{
			if(red[i] == '+' && red[i+1]=='-')
				ans+=1;
			else if(red[i] == '-' && red[i+1]=='+')
				ans+=1;
		}
		if(red[0] == '+' && red[k-1] == '-')
			ans += 1;
		else if(red[0] == '-' && red[k-1] == '-')
			ans += 1;
		printf("Case #%d: %d\n", c+1, ans);
	}
	return 0;
}