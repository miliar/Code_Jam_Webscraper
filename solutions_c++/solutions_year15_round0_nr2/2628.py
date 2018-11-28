#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int p[20000];
int d, t;

int main()
{
    cin >> t;
    for (int c = 1; c <= t; c++)
    {
	memset(p, 0, sizeof(p));
	cout << "Case #" << c << ": ";
	cin >> d;
	for (int i = 0; i < d; i++)
	    cin >> p[i];
	int answer = 10000;
	for (int i = 1; i <= 2000; i++)
	{
	    int sum = 0;
	    for (int j = 0; j < d; j++)
		sum += (p[j] - 1) / i;
	    answer = min(answer, i + sum);
	}
	cout << answer << endl;
    }
}
