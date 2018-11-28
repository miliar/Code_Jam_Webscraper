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

int main()
{
int N , test , T;
cin >> test;
int freq[12] , counter = 10;
int i;

for(int o=1;o<=test;o++)
{
	cin >> N;
	if(N!=0)
	{
	for(int i=0;i<12;i++)
		freq[i] = 0;
	counter = 10;
	for(i=1;counter>0;i++)
	{
		T = (N*i);
		while(T!=0)
		{
			if(freq[(T%10)]==0)
				counter--;
				freq[(T%10)]++;
				T = (T/10);
		}
		if(counter==0)
			break;
	}	
	printf("Case #%d: %d\n",o, (N*i));
	}
	else
		printf("Case #%d: INSOMNIA\n",o);
}
return 0;
}










