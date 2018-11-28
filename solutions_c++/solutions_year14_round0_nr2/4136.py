#include<vector>
#include<fstream>
#include<iostream>
#include<string>
#include<algorithm>
#include<ctime>
#include<iomanip>
using namespace std;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	cout << fixed << setprecision(7);
	int n;
	cin >> n;
	for ( int i = 0 ; i < n ; i++ )
	{

		double C, F, X, T = 0.0, S;
		cin >> C >> F >> X;
		S = 2.0;
		while(true)
		{
			if ( (double)(X-C)/S < (double)X/(S+F) ) 
				break;
			else 
			{
				T+=(double)C/(S);
				S+=F;
			}
		}
		T+=(X)/(S);
		cout << "Case #" << i+1 << ": " <<  T << endl;


	}
}