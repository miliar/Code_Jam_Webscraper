//Nakul Krishna
//Computer Science Engineering
//Amrita Vishwa Vidyapeetham

#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<sstream>
#include<queue>
#include<stack>

#include<ctype.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

#define pb push_back
#define mp make_pair

using namespace std;

unsigned long long mod=1000000007;

int dp[1010];

int is_palindrome(int a)
{
	int rev=0,temp=a;
	while(a)
	{
		rev=rev*10+(a%10);
		a/=10;
	}
	if(rev==temp)
		return 1;
	return 0;
}

void func()
{
	int cnt=0;
	for(int i=0;i<=1000;i++)
	{
		if(is_palindrome(i) and (int)sqrt(i)*(int)sqrt(i)==i and is_palindrome((int)sqrt(i)))
			cnt++;
		dp[i]=cnt;
	}
}

int main()
{
	int t=1,tc;
	memset(dp,0,sizeof dp);
	scanf("%d",&tc);
	func();
	while(t<=tc)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		printf("Case #%d: %d\n",t,dp[b]-dp[a-1]);
		t++;
	}
    scanf("\n");
    return 0;
}

//Nakul © Copyright 2012 - All Rights Reserved

