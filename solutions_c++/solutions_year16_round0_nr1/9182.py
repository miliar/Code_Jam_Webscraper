#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

bool mark[10];

void work(int x)
{
	while(x)
	{
		mark[x % 10] = 1;
		x /= 10;
	}
}

int main()
{
	int t = in();
	int tt = 0;
	while(t--)
	{
		int x = in();
		tt++;
		cout << "Case #" << tt << ": ";
		if(!x)
			cout << "INSOMNIA" << endl;
		else
		{
			fill(mark, mark + 10, 0);
			int y = 0;
			while(1)
			{
				y += x;
				work(y);
				if(*min_element(mark, mark + 10))
					break;
			}
			cout << y << endl;
		}
	}
}
