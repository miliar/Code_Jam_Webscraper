#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

double t[100011];

int main()
{
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);
	int n;
	scanf ("%d", &n);
	for (int i = 0; i < n; i++)
	{
		for (int k = 0; k < 100011; k++)
			t[k] = 0.0;
		double c, f, x;
		scanf ("%lf%lf%lf", &c, &f, &x);
		double cur = 2.0 - f;
		int cnt = 1;
		t[0] = 0;
		while (cur < 100000)
		{
			t[cnt] = t[cnt - 1] + c / (cur + f);
			cur += f;
			cnt++;
		}
		for (int k = 1; k < 100011; k++)
			if (t[k] == 0.0)
				t[k] = t[k - 1] + 10.0;
		int r = 100010;
		int l = 0;
		while (r - l > 2)
		{
			int curl = l + (r - l) / 3;
			int curr = l + (r - l) * 2 / 3;
			if ((t[curl] + x / (curl * f + 2)) < (t[curr] + x / (curr * f + 2)))
				r = curr;
			else
				l = curl;
		}
		double minans = 1000000.0;
		for (int k = l; k <= r; k++)
			if ((t[k] + x / (k * f + 2)) < minans)
				minans = t[k] + x / (k * f + 2);
		printf ("Case #%d: %.7f\n", i + 1, minans);
	}
	return 0;
}
