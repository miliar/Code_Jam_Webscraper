
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <iomanip>

using namespace std;

int main()
{
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cout << fixed << std::setprecision(7)<< "Case #" << i + 1 << ": ";
		double C, F, X;
		cin >> C >> F >> X;
		double curdcookie = 2.0f, allTime1, farm = 0, other = 0, prev = 0, tmp = 0, prev_prev = 0, prev_prev_prev = 0, prev_other = 0;
		if (C / curdcookie>X / curdcookie) cout << X / curdcookie<<endl;
		else
		{
		
			farm = C / curdcookie;
			other = X / curdcookie;
			tmp = other;
			prev = farm;


			
			do
			{
				
				curdcookie += F;
				farm = C / curdcookie;
				prev_other = other;
				other = X / curdcookie;
				allTime1 = tmp;
				tmp = prev+other;
				prev_prev_prev = prev_prev;
				prev_prev = prev;
				prev = prev+farm;
				

			}while (allTime1 > tmp);

			double out = prev_prev_prev + prev_other;
			cout << out<<endl;


		}

	}
}

