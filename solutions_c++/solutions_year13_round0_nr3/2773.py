#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;


int issqu(long long n)
{
	double t = n;
	long long s = sqrt(t);
	if (s*s == n) return 1;
	else return 0;
}

int ispre(long long n)
{
	int j,len,temp = n,dig[101];
	for (len = 1; ; len++)
	{
		dig[len] = temp % 10;
		temp = temp / 10;
		if (temp == 0) break;
	}
	for (j = 1 ; j <= len/2 ; j++)
	{
		if (dig[j] != dig[len-j+1]){return 0;} 
	}
	return 1;

}
int solve()
{
	long long a,b,i;
	int num=0;
	scanf("%lld%lld",&a,&b);
	for (i = a ; i <= b ; i++)
	{
		if(issqu(i) && ispre((int) sqrt( (double) i)) && ispre(i)) num++;
	}
	return num;
}

int main()
{
	int T;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf("%d",&T);
	for (int t = 1 ; t <= T ;t++)
		printf("Case #%d: %d\n",t,solve());
return 0;
}