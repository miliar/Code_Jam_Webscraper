#include <bits/stdc++.h>

using namespace std;

#define ll long long

ll dp_neg[101];
ll dp_pos[101];
char s[101];

void flip(int x)
{
	for(int i=0;i<=x/2;i++)
	{
		if(i!=x-i)
		{
			char temp = s[x-i];
			s[x-i] = (s[i]=='-') ? '+' : '-';
			s[i] = (temp=='-') ? '+' : '-';
		}
		else
			s[i] = (s[i]=='-') ? '+' : '-';
	}
}

int main()
{
	int T;
	scanf("%d\n", &T);
	for(int case_num=1;case_num<=T;case_num++)
	{
		scanf("%s", s);
		dp_pos[0] = dp_neg[0] = 0;
		if(s[0]=='-')
			dp_pos[0] = 1;
		else
			dp_neg[0] = 1;

		for(int i=1;i<strlen(s);i++)
		{
			if(s[i]=='-')
			{
				dp_neg[i] = min(dp_neg[i-1], dp_pos[i-1]+2);
				dp_pos[i] = min(dp_neg[i-1]+1, dp_pos[i-1]+3);
			}
			else
			{
				dp_neg[i] = min(dp_neg[i-1]+3, dp_pos[i-1]+1);
				dp_pos[i] = min(dp_pos[i-1], dp_neg[i-1]+2);
			}
		}
		printf("Case #%d: %lld\n", case_num, dp_pos[strlen(s)-1]);
	}
}
