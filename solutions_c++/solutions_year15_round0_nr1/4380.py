#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>

#define MAX 1010

using namespace std;

int Tcases, Smax;
char input[MAX];

void getInput()
{
	scanf("%d", &Smax);
	scanf("%s", input);
}

void solve(int c)
{
	int standing, solution = 0;

	standing = input[0] - '0';

	for(int i=1; i<strlen(input); i++)
	{
		int curInt = input[i] - '0';
		if (curInt == 0) continue;

		if (standing < i)
		{
			solution += i - standing;
			standing += i - standing;
		}

		standing += curInt;
	}

	printf("Case #%d: %d\n", c, solution);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("largeout.out", "w", stdout);

	scanf("%d", &Tcases);

	for(int i=0; i<Tcases; i++)
	{
		getInput();
		solve(i + 1);
	}

	return 0; 
}