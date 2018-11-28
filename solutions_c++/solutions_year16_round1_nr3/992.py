#include <iostream>
using namespace std;
const int MAXN = 10;
int n, f[MAXN + 1], result, c[MAXN + 1];
bool used[MAXN + 1];
void find_longest_circle_length(int pos)
{
	int i, j, temp[MAXN + 2];
	if(pos == n)
	{
		for(i = 2; i <= n; i++)
		{
			temp[0] = c[i - 1];
			for(j = 1; j <= i; j++)
				temp[j] = c[j - 1];
			temp[i + 1] = c[0];
			for(j = 1; j <= i; j++)
				if(f[temp[j]] != temp[j - 1] && f[temp[j]] != temp[j + 1])
					break;
			if(j == i + 1 && result < i)
				result = i;
		}
	}
	else
		for(i = 1; i <= n; i++)
			if(!used[i])
			{
				used[i] = true;
				c[pos] = i;
				find_longest_circle_length(pos + 1);
				used[i] = false;
			}
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, j, k, temp;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		cin >> n;
		for(j = 1; j <= n; j++)
		{
			cin >> f[j];
			used[j] = false;
		}
		result = 0;
		cout << "Case #" << i << ": ";
		find_longest_circle_length(0);
		cout <<result << endl;
	}
}

