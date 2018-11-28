#include <iostream>
#include <vector>
#include <string>

using namespace std;

string solve_D_get_ans(int x, int r, int c)
{
	string name = "GABRIEL";

	if (r * c % x) return "RICHARD";

	//‰½‚Å‚à–„‚ß‚ç‚ê‚é
	if (x == 1) return "GABRIEL";

	//
	if (x == 2) return "GABRIEL";

	if (x == 3)
	{
		if (r * c == 3) return "RICHARD";
		else return "GABRIEL";
	}

	if (x == 4)
	{
		if (r * c == 4 || r * c == 8) return "RICHARD";
		else return "GABRIEL";
	}

	return name;
}

void solve_D()
{
	//cout << "solve D" << endl;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int x, r, c;
		string name;

		cin >> x >> r >> c;
		//cout << x << " " << r << " " << c << endl;
		name = solve_D_get_ans(x, r, c);
		cout << "Case #" << i + 1 << ": " << name << endl;
	}

	//cout << "GABRIEL" << endl;
	//cout << "RICHARD" << endl;
}

int main()
{
	solve_D();
	return 0;
}