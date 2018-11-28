/* Google Code Jam */

#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int tot_num_fair_sqr[1004];

bool isFair(int input)
{
	char input_str[5];
	int cnt=0;

	for(int i=input; i>0; i/=10)
		input_str[cnt++] = i%10;

	for(int i=0; i<cnt; i++)
		if(input_str[i] != input_str[cnt-i-1]) return false;

	return true;
}
int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	for(int i=0; i<1004; i++)
		tot_num_fair_sqr[i] = 0;

	int T;

	scanf("%d", &T);

	for(int i=1; i*i<1002; i++)
		if(isFair(i) == true && isFair(i*i) == true)
			tot_num_fair_sqr[i*i]++;
/*
	for(int i=1; i<=1000; i++)
		if(tot_num_fair_sqr[i]>0) printf(" %d", i);
*/
	for(int tc=1; tc<=T; tc++)
	{
		int left, right, ans=0;

		cin >> left >> right;

		for(int i=left; i<=right; i++)
			if(tot_num_fair_sqr[i]>0) ans++;

		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}