#include <stdio.h>
#include <vector>

using namespace std;

vector<long long> v;

bool isPalindrome(long long n)
{
	char num[25];
	int nsize=0;
	
	while(n)
	{
		num[nsize++] = '0' + (char)(n%10);
		n /= 10;
	}
	
	for(int i=0; i<nsize/2; i++)
		if(num[i] != num[nsize-1-i])
			return false;
	
	return true;
}

void preCalc()
{
	for(long long i = 1; i <= 10000000L; i++)
		if(isPalindrome(i) && isPalindrome(i*i))
			v.push_back(i*i);
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	
	preCalc();
	
	int n;
	scanf(" %d", &n);
	for(int k=1; k<=n; k++)
	{
		int a, b;
		scanf(" %d %d", &a, &b);
		
		int ans = 0;
		
		for(int i=0; i<v.size(); i++)
			if(v[i] >= (long long)a && v[i] <= (long long)b)
				ans++;
		
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}
