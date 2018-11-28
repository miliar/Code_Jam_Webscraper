		//	   - -- --- ---- -----be name khoda----- ---- --- -- -		\\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

int main()
{
	int _ = in();
	for(int i = 1; i <= _; i++)
	{
		printf("Case #%d: ", i);
		int x = in(), r = in(), c = in();
		bool ans = 0;
		if(r * c % x != 0)
			ans = 1;
		if(r > c)
			swap(r, c);
		if(c < x)
			ans = 1;
		if(x == 3)
			if(r < 2 || c < 3)
				ans = 1;
		if(x == 4)
			if(r < 3 || c < 4)
				ans = 1;
		if(x == 5)
			if(r < 3 || (r == 3 && c < 10) || (r == 4 && c < 5))
				ans = 1;
		if(x == 6)
			if(r < 4)
				ans = 1;
		if(x > 6)
			ans = 1;
		if(ans)
			cout << "RICHARD\n";
		else
			cout << "GABRIEL\n";
	}
}
