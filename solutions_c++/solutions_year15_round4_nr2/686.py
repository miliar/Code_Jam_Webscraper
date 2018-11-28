#include <bits/stdc++.h>
using namespace std;
#define int long long

int n;
double v, x, r1, c1, r2, c2;
double nowv, nowt, r, c;

void pre()	{

}

void pain()	{
	cin >> n;
	if(n == 1)	{
		cin >> v >> x >> r1 >> c1;
		if(fabs(c1 - x) < 1e-9)	{
			cout << v / r1 << "\n";
		}	else	{
			cout << "IMPOSSIBLE\n";
		}
		return;
	}
	cin >> v >> x >> r1 >> c1 >> r2 >> c2;
	if(x > c1 and x > c2)	{
		cout << "IMPOSSIBLE\n";
		return;
	}
	if(x < c1 and x < c2)	{
		cout << "IMPOSSIBLE\n";
		return;
	}
	if(fabs(x - c1) < 1e-9 and fabs(x - c2) < 1e-9)	{
		cout << v / (r1 + r2) << "\n";
		return;
	}
	double q1 = (x * v - v * c2) / (c1 - c2);
	double q2 = v - q1;
	cout << max(q1 / r1, q2 / r2) << "\n";
}

#undef int
int main()	{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string input = "2ain.txt";
	string output = "2aout.txt";
	freopen(input.c_str(), "r", stdin);
	freopen(output.c_str(), "w", stdout);
	int tt; cin >> tt;
	pre();
	cout << fixed << setprecision(10);
	for(int iii=1; iii<=tt; iii++)	{
		cout << "Case #" << iii << ": ";
		pain();
	}
}

