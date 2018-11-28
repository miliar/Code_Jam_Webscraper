#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

int NFS;
long long FS[100000];

long long D[110];
long long is_palindrome(long long x)
{
	int n=0;
	while(x)
	{
		D[n++] = x%10;
		x/=10;
	}
	for(int i = 0; i < n; i++)
		if(D[i] != D[n-i-1])
			return false;
	return true;
}

int next_palindrome(int x)
{
	int n=0;
	while(x)
	{
		D[n++] = x%10;
		x /= 10;
	}
	int l = n/2;
	int r = (n-1)/2;
	while(l < n && D[l]==9)
	{
		D[l++]=0;
		D[r--]=0;
	}
	int result = 0;
	if(D[n-1]==0)
	{
		D[n-1] = 1;
		result = 1;
	}
	else
	{
		D[l] = D[l]+1;
		D[r] = D[l];
	}
	for(int i = 0; i < n; i++)
		result = result*10ll + D[i];
	return result;
}

int main()
{
	long long x = 1;
	while(x <= 100000000)
	{
		if(is_palindrome(x*x))
			FS[NFS++] = x*x;
		x = next_palindrome(x);
	}
	// for(int i = 0;i < NFS; i++)
		// cout << FS[i] << endl;
	// return 0;
	
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		
		long long A,B;
		cin >> A >> B;
		int result = 0;
		for(int i = 0; i < NFS; i++)
			if(FS[i] >= A && FS[i] <= B)
				result++;
		printf("%d\n", result);
	}
}

