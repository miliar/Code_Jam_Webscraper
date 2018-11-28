#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	
	for(int i=1; i<=cases; i++) {
		cout<<"Case #" << i << ": ";
		
		double C, F, X, income = 2.0, actual=0.0, timer=0.0;
		cin >> C >> F >> X;
		
		while( (X/income) > ( X/(income + F) + (C/income) ) )
		{
			timer += C/income;
			actual = 0.0;
			income += F;
		}
		
		timer += (X-actual)/income;
		
		//cout << std::setprecision(7) << timer << endl;
		printf("%5.7f\n", timer);
	}
	return 0;
}

