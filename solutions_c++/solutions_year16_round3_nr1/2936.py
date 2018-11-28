#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<algorithm>
#include<map>
using namespace std;

int main() {
	//FILE *fin = freopen("A-small-attempt0.in", "r", stdin);
	FILE *fin = freopen("A-small-attempt0.in", "r", stdin);
	assert(fin != NULL);
	//FILE *fout = freopen("A-small-attempt0.out", "w", stdout);
	FILE *fout = freopen("A-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int a[26];
		int N;
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> a[i];
		if (N == 2)
		{
			cout <<"AB";
			for (int i = 1; i < a[0];i++)
				cout<<" AB";
		}
		else
		{
			if (a[0] == a[1])
			{
				int x = a[2] / 2;
				int y = a[2] % 2;
				for (int i = 0; i < x; i++)
				{
					cout << "CC ";
				}
				if (y > 0) cout << "C ";
				cout << "AB";
				for (int i = 1; i < a[0]; i++)
				{
					cout << " AB";
				}

			}
			else if (a[0] == a[2])
			{
				int x = a[1] / 2;
				int y = a[1] % 2;
				for (int i = 0; i < x; i++)
				{
					cout << "BB ";
				}
				if (y > 0) cout << "B ";
				cout << "AC";
				for (int i = 1; i < a[0]; i++)
				{
					cout << " AC";
				}
			}
			else if (a[1] == a[2])
			{
				int x = a[0] / 2;
				int y = a[0] % 2;
				for (int i = 0; i < x; i++)
				{
					cout << "AA ";
				}
				if (y > 0) cout << "A ";
				cout << "BC";
				for (int i = 1; i < a[1]; i++)
				{
					cout << " BC";
				}
			}

			else
			{
				if (a[0] > a[1] && a[0] > a[2])
				{
					if (a[1] > a[2])
					{
						for (int i = 0; i < a[0] - a[1]; i++)
							cout << "A ";
						for (int i = 0; i < a[2]; i++)
							cout << "C ";
						cout << "AB";
						for (int i = 1; i < a[1]; i++)
							cout << " AB";
					}
					else
					{
						for (int i = 0; i < a[0] - a[2]; i++)
							cout << "A ";
						for (int i = 0; i < a[1]; i++)
							cout << "B ";
						cout << "AC";
						for (int i = 1; i < a[2]; i++)
							cout << " AC";
					}
				}
				else if (a[1] > a[0] && a[1] > a[2])
				{
					if (a[0] > a[2])
					{
						for (int i = 0; i < a[1] - a[0]; i++)
							cout << "B ";
						for (int i = 0; i < a[2]; i++)
							cout << "C ";
						cout << "AB";
						for (int i = 1; i < a[0]; i++)
							cout << " AB";
					}
					else
					{
						for (int i = 0; i < a[1] - a[2]; i++)
							cout << "B ";
						for (int i = 0; i < a[0]; i++)
							cout << "A ";
						cout << "BC";
						for (int i = 1; i < a[2]; i++)
							cout << " BC";
					}
				}
				else
				{
					if (a[0] > a[1])
					{
						for (int i = 0; i < a[2] - a[0]; i++)
							cout << "C ";
						for (int i = 0; i < a[1]; i++)
							cout << "B ";
						cout << "AC";
						for (int i = 1; i < a[0]; i++)
							cout << " AC";
					}
					else
					{
						for (int i = 0; i < a[2] - a[1]; i++)
							cout << "C ";
						for (int i = 0; i < a[0]; i++)
							cout << "A ";
						cout << "BC";
						for (int i = 1; i < a[1]; i++)
							cout << " BC";
					}
				}

			}

		}
		cout << endl;
	}
	exit(0);
}
