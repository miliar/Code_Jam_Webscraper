#include <bits/stdc++.h>
using namespace std;

const int N =  101;

void flip(char* s, int & l);

int solve(char *s)
{
	int l = strlen(s)-1,ans = 0;
	int last = l;
	while(l >= 0)
	{
		if(s[last] == '-'){
			if(s[0] == '-'){
				flip(s,last);
				last--;
				l = last;
			}
			else{
				while(s[l] == '-' && l>=0){l--;}
					if(l>=0) flip(s,l);
					
			}
			ans++;
		}
		else{
			last--;
			l--;
		}
	}
	return ans;
}

void flip(char* s, int & l)
{
	char c;
	for (int i = 0; i <= l/2; ++i)
	{
		c = s[l-i];
		s[l-i] = (s[i] == '+')?'-':'+';
		s[i] = (c == '+')?'-':'+';
	}
}

int main()
{
	int t,ans;
	char str[N];
	scanf("%d",&t);
	for (int i = 1; i <= t; ++i)
	{
		scanf("%100s",str);
		ans = solve(str);
		printf("Case #%d: %d\n",i,ans);
	}
}