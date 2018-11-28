#include<iostream>
#include<string>
#include<cstring>

using namespace std;

#define PLUS 1
#define MINUS 0
void stack_reverse(int *a, int n)
{
	for (int i = 0; i <= n/2; i++)
	{
		int temp = !a[i];
		a[i] = !a[n-i];
		a[n-i] = temp;
	}
}

int move_end(int *a, int n)
{
	int i = n;
	while(i != -1 && a[i] == PLUS) i--;
	return i;
}

int correct_start(int *a, int n)
{
	for (int i = 0; i <= n; i++)
		if (a[i] == PLUS)
		{
			a[i] = MINUS;
		}
		else
			return i==0?0:1;
}

int N;
char str[1000];
int a[1000];
int main()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> str;
		int n = strlen(str);
		for (int j = 0; j < n; j++)
			if (str[j] == '+') a[j] = PLUS;
			else a[j] = MINUS;

		n--;
		int cnt = 0;
		while(1)
		{
			n = move_end(a, n);
			if (n == -1) break;

			int ret = correct_start(a, n);
			if (ret == 1) cnt++;

			stack_reverse(a, n);
			cnt++;
		}
		cout << "Case #" << i + 1 << ": " << cnt << endl;
	}
	return 0;
}

