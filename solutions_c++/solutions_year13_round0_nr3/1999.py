#include<stdio.h>
#include<iostream>
#include<cstring>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;++i)
#define FORS(i,s,n) for(int i=s;i<n;++i)
#define MAX 1000

bool is_palindrome(int x)
{
	int reverse = 0, original = x;
	
	while(x>0)
	{
		reverse = reverse*10 +x%10; 
		x/=10;
	}

	return reverse==original;
}

int main()
{
	int t,a,b, hash[MAX+1];
	scanf("%d",&t);
	memset(hash, 0, sizeof(hash));
	
	int i=0;
	
	while(i*i < MAX+1)
	{
		hash[i*i]=i;
		++i;
	}

	FOR(T,t)
	{
		scanf("%d%d", &a, &b);
	
		int cnt = 0;

		FORS(i,a,b+1)
		{
			if(is_palindrome(i) && hash[i]!=0 && 
			   is_palindrome(hash[i]))
			 {
			 	++cnt;
			 }
		}

		printf("Case #%d: %d\n", T+1, cnt);
	}

	return 0;
}
