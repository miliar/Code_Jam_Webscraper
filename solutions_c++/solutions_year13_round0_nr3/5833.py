#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <cstring>
#include <stack>
using namespace std;

#define x first
#define y second
#define pb push_back
#define mp make_pair

int n,t;
char field[10][10];

bool check_pal(long long k)
{
	vector<int> dig;

	while(k != 0)
	{
		dig.pb(k%10);
		k /= 10 ;
	}
	for(int i = 0,j = dig.size()-1;i++,j--;i < j)
	{
		if (dig[i] != dig[j])
			return(false);
	}
	return(true);
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&t);
	for(int test = 0; test < t; test++)
	{
		long long a;
		long long b;
		int c = 0;
		cin >> a >> b;
		for(long long i = (long long)ceil(sqrt(a)); i <= (long long)floor(sqrt(b)); i++)
		{
			if (check_pal(i)&&check_pal(i*i))
				c++;
		}
		printf("Case #%d: %d\n",test+1,c);
	}
	return(0);
}