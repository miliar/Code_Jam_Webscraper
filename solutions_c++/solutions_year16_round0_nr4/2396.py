#include <iostream>
#include <fstream>
#include <cstdlib>
#include<string>
#include<vector>
#include<cmath>
#include <sstream>

using namespace std;

unsigned long long int temp;

int cases = 0;
int S, K, C;

int main()
{


	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> cases;


	for (int i = 0; i < cases; i++)
	{

		cin >> K;
		cin >> C;
		cin >> S;
		//temp = pow(K, C);


		cout << "Case #" << i + 1 << ": ";
		for (int a = 0; a < K; a++)
		{
			//for s = K case

			cout << a + 1 << " ";


		}

		cout << endl;
	}



	return 0;
}
