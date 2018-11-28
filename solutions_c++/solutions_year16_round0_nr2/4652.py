// Google Code Jam 2016
// Qualifying Round
// Problem B - Revenge of the Pancakes

#include <cstdio>
#include <string>
#include <iostream>

#define INPUT_FILE "B-large.in"
#define OUTPUT_FILE "B-large.out"

using namespace std;

int N, T;
string S;

void Flip(string& s, int first)
{
	for (int i = 0; i < first; ++i)
	{
		s[i] = '+' + '-' - s[i];
	}
}

void Solve()
{
	cin >> S;
	int flips = 0;

	// can be improved, not needed for the limits
	for (int i = S.size() - 1; i >= 0; --i)
	{
		if (S[i] == '-')
		{
			Flip(S, i);
			++flips;
		}
	}

	printf("%d\n", flips);
}

int main()
{
    freopen(INPUT_FILE, "rt", stdin);
    freopen(OUTPUT_FILE, "wt", stdout);
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        Solve();
    }
   
   return 0;
}

