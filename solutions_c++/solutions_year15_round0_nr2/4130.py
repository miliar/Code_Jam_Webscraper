#include <iostream>
using namespace std;
int sort(int *a, int d)
{
	int t;
	for (int i = 0; i < d - 1; i++)
		for (int j = i + 1; j < d; j++)
			if (a[i] < a[j]){
				t = a[i];
				a[i] = a[j];
				a[j] = t;
			}
	return *a;
}

int main()
{ 
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int d, i, t, n, m, s;
	cin >> s;
	for (int j = 1; j <= s; j++)
	{
		int p[100000] = { 0 };
		cin >> d;
		for (i = 0; i < d; i++)
			cin >> p[i];
		*p = sort(p, d);
		m = n = p[0];

		for (t = 1; t<n; t++, d++)
		{
			if (p[0] == 9 &&( p[1]<4||(p[1]==6 && p[2]<4)))
			{
				p[0] -= 3; p[d] = 3;
			}
			else
			{
				p[d] = p[0] / 2;
				p[0] -= p[d]; 
			}
			*p = sort(p, d);
			if (m>t + p[0])m = t + p[0];
		}
	//	cout << m;
	//	system("pause");
		cout<<"Case #"<<j<<": " << m<<endl;
	}
	return 0;

}
