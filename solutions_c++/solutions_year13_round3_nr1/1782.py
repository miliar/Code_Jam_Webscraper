#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define Maxsize 100+5
char sname[Maxsize];

bool IsConsonant(char x)
{
	if (x=='a' || x=='e' || x=='i' || x=='o' || x=='u')
		return false;

	return true;
}

//check the substring, sname[ begin, end), whether statisify n consequtive consanonts or not
bool Check(int begin, int end, int n)
{
	int i, j;
	int max, cnt;

	max = 0;

	for (i=begin; i<end; i=j+1)
	{
		cnt = 0;
		j=i;
		while( IsConsonant(sname[j]) && j<end)
		{
			cnt++;
			j++;
		}
		if (cnt>max) max = cnt;
	}

	if (max >= n) return true;
	return false;
}

int Cal(char *sname, int n)
{
	int begin, end;
	int ans=0;
	int L = strlen(sname);

	for (begin=0; begin+n<=L; begin++)
	{
		end = begin + n;
		while (end<=L)
		{
			if ( Check(begin, end, n) ) //if sname[ begin, end) statisify n consequtive consanonts
				break;
			end++;
		}
		//if it don't have anyone, then end will be L+1

		ans += L- end + 1;
	}

	return ans;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	//=========code segment
	int T;
	scanf("%d", &T);

	int i, j;
	int n;
	int ans;
	for (i=1; i<=T; i++)
	{
		scanf("%s%d", sname, &n);
		ans = Cal(sname, n);
		printf("Case #%d: %d\n", i, ans);
	}

	//============================
	fclose(stdin);
	fclose(stdout);
	return 0;
}