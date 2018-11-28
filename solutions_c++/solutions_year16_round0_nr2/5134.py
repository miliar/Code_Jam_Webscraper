#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <map>
#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807LL
#define INF 2000000000
#define PI acos(-1.0)
#define inf INT_MAX
using namespace std;
typedef long long int LL;
string ip;


int main()
{
int test , len , nxt , i;
scanf("%d",&test);
int answer;
for(int o=1;o<=test;o++)
{
	cin >> ip;
	len = ip.length();
	answer = 0;
	while(1)
	{
		nxt = 0;
		while(ip[nxt]==ip[0] && nxt<len)
		{
			nxt++;
		}
		if(ip[0]=='+' && nxt==len)
			break;
		
		for(int j=0;j<nxt;j++)
		{
			if(ip[j]=='+')
				ip[j] = '-';
			else
				ip[j] = '+';
		}
		// cout << ip << nxt << endl;
		// sleep(5);
		answer++;
	}
	printf("Case #%d: %d\n", o , answer);
}
return 0;
}













