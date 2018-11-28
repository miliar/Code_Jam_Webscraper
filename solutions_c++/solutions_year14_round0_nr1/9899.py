#include <cstdio>
#include <iostream>

using namespace std;

int t, tt, m, sel[17], ans, a, b, c, d;

void reset()
{
	for(int i = 1; i <= 16; i++)
	{
		sel[i] = 1;
	}
}

int main()
{
	cin >> t;
	tt = t;

	while(t--)
	{
		reset();
		ans = 0;

		cin >> m;
		for(int i = 1; i <= 4; i++)
		{
			cin >> a >> b >> c >> d;
			if(i != m)
			{
				sel[a] = 0;
				sel[b] = 0;
				sel[c] = 0;
				sel[d] = 0;
			}
		}

		cin >> m;
		for(int i = 1; i <= 4; i++)
		{
			cin >> a >> b >> c >> d;
			if(i != m)
			{
				sel[a] = 0;
				sel[b] = 0;
				sel[c] = 0;
				sel[d] = 0;
			}
		}

		for(int i = 1; i <= 16; i++)
		{
			if((ans == 0) && (sel[i]))
			{
				ans = i;
			}
			else if((ans != 0) && (sel[i]))
			{
				ans = -1;
				break;
			}
		}

		if(ans == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", tt-t);
		}
		else if(ans == -1)
		{
			printf("Case #%d: Bad magician!\n", tt-t);
		}
		else
		{
			printf("Case #%d: %d\n", tt-t, ans);
		}
	}
}
