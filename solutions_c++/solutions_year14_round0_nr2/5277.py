#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stdio.h>

using namespace std;
int main()
{
	FILE *out;
	FILE *in;

	freopen_s(&in, "B-large.in", "r", stdin);
	freopen_s(&out, "B-large.out", "w", stdout);

	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		double c;
		double f;
		double x;

		cin >> c;
		cin >> f;
		cin >> x;


		double produce = 2;
		
		double cost = 0;


		while (true){

			double invest = c / produce;

			if ((x / (produce + f) + invest) > (x / produce)) break;
			else {
				cost += invest;
				produce += f;
			}
		}


		cost += x / produce;

		cout.precision(10);
		cout << "Case #" << i << ": " << cost;

		cout << endl;

	}

	//system("pause");
}