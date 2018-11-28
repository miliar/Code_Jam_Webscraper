#include <stdio.h>
#include <vector>
using namespace std;


typedef long long lint;


bool isPalindrome(lint v)
{
	char s[20]; sprintf(s, "%lld", v);
	int l; for(l = 0; s[l]; l++);
	for(int i = 0; i < l / 2; i++)
		if(s[i] != s[l - i - 1]) return false;
	return true;
}

vector<lint> v;

void init()
{
	for(lint i = 1; i <= 20000000; i++)
	{
		if(isPalindrome(i) && isPalindrome(i * i))
			v.push_back(i * i);
	}
}

int main()
{
	init();
	
	int T;
	scanf("%d", &T);
	
	for(int t = 0; t < T; t++)
	{
		lint A, B;
		scanf("%lld %lld", &A, &B);
		
		int cnt = 0;
		for(int i = 0; i < (int)v.size(); i++)
		{
			if(v[i] >= A && v[i] <= B)
				cnt++;
		}
		
		printf("Case #%d: %d\n", t + 1, cnt);
	}
	
	return 0;
}
