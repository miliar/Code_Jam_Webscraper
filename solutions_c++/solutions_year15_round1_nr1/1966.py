#include <iostream>
using namespace std;

int p[10000];

int main()
{
	int trials; cin >> trials;
	for (int trial = 1; trial <= trials; ++trial)
	{
		int N; cin >> N;
		for (int i = 0; i < N; ++i) cin >> p[i];
		
		int a = 0, b = 0;
		int bigJump = 0;
		for (int i = 0; i < N-1; ++i)
		{
			if (p[i+1] < p[i])
			{
				a += p[i]-p[i+1];
				if (p[i]-p[i+1] > bigJump)
					bigJump = p[i]-p[i+1];
			}
		}
		
		for (int i = 0; i < N-1; ++i)
			b += (bigJump>p[i]?p[i]:bigJump);
		cout << "Case #" << trial << ": " << a << " " << b << endl;
	}
}
