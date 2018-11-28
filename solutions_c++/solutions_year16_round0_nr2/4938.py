#include <bits/stdc++.h>

using namespace std;

char s[110], temp[110];
int n, ans;

void Flip(int pos)
{
	for(int i=0;i<=pos;i++)
	{
		temp[i] = s[pos-i];
	}
	for(int i=0;i<=pos;i++)
	{
		s[i] = temp[i];
	}
}
void Reverse(int pos)
{
	for(int i=0;i<=pos;i++)
	{
		if(s[i] == '+')	s[i] = '-';
		else	s[i] = '+';
	}
}
int maxPos(int pos)
{
	int ind=-1, cnt=0, maxi=0;
	for(int i=0;i<pos;i++)
	{
		cnt=0;
		while(i<pos && s[i] == '+')
		{	
			i++;
			cnt++;
		}
		if(cnt>0)	i--;
		if(maxi<cnt)
		{
			ind = i;
			maxi = cnt;
		}
	}
	return ind;
}
void solve(int pos, int tot)
{
	if(tot>2 * n || tot>=ans || pos<0)	return;
	if(pos == 0)
	{
		if(s[pos] == '-')
		{
			ans = min(ans, tot+1);
		} else	ans = min(ans, tot);
	}
	if(s[pos] == '+')
	{
		solve(pos-1, tot);
	} else {
		if(s[0] == '-')
		{
			Flip(pos);
			Reverse(pos);
			solve(pos-1, tot+1);
			Flip(pos);
			Reverse(pos);
		}
		int ind = maxPos(pos);
		if(ind>=0)
		{
			Flip(ind);
			Reverse(ind);
			Flip(pos);
			Reverse(pos);

			solve(pos-1, tot+2);

			Reverse(pos);
			Flip(pos);
			Flip(ind);
			Reverse(ind);
		}
	}
}
int main()
{
	int t, ind=0;
	scanf("%d",&t);
	while(t--)
	{
		ind++;
		ans = 10000;
		scanf("%s",&s);
		n = strlen(s);
		solve(n-1, 0);
		printf("Case #%d: %d\n", ind, ans);
	}
	return 0;
}