/*************************************************************************
    > File Name: codejamB.cpp
    > Author: skt
    > Mail: sktsxy@gmail.com 
    > Created Time: 2014年04月12日 星期六 23时09分44秒
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
template <typename T> inline T Min(T a, T b) {return a<b?a:b;}
int t, Cas = 1, num;
double c, f, x, ans, maxn;
void work()
{
	scanf("%lf %lf %lf", &c, &f, &x);
	maxn = ans = x / 2.0;
	printf("Case #%d: ", Cas ++);
	num = 1;
	double now = 0, tmp;
	while (num) {
		now = now + c / (2.0 + (num - 1) * f);
		tmp = now + x / (2 + num * f);
		if (ans > tmp) {
			ans = tmp;
		}
		if (ans < tmp) 
			break;
		num ++;
	}
	printf("%.7lf\n", ans);
}
int main()
{
	scanf("%d", &t);
	while (t --) {
		work();
	}
	return 0;
}
