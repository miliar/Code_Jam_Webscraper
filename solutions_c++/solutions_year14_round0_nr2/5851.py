#include <iostream>

#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <limits>
#include <iomanip> 

using namespace std;

int T;

double solve()
{
	double C, F, X;
	cin >> C >> F >> X;

	double curr_rate=2.0;
	double sum = 0;

	//cout << "C:" << C << " F:" << F << " X:" << X << endl;
   cout.precision(7);

	
	while(true)
	{
		double curr_to_C = C/curr_rate;
		double curr_to_X = X/curr_rate;
		double next_to_X = X/(curr_rate+F);

		//	cout << "Rate:" << curr_rate << " toC:" << curr_to_C << " toX:" << curr_to_X << " nextX:" << next_to_X << endl;
		
		if(curr_to_C + next_to_X >= curr_to_X)
			return sum + curr_to_X;

		sum += curr_to_C;
		curr_rate += F;
	}
	return 0; // Ohi ohi ohi 
}

int main()
{
	cin >> T;
	for(int i=0; i < T; i++)
		cout << "Case #" << i+1 << ": " << fixed << solve() << endl;
	return 0;
}
