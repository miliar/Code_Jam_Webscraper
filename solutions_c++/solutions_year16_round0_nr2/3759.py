#include<iostream>
#include<fstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	/*ifstream cin;
	ofstream cout;
	cin.open("pancakes.in");
	cout.open("pancakes.out");*/

    long long int testCases;
	cin >> testCases;

	long long int tc = 0;
    while (++tc <= testCases)
    {
		cout << "Case #" << tc << ": ";

        string input;
		cin >> input;

		int length = input.length();
		bool state = true;
		int flips = 0;
		for (int i = length - 1; i >= 0; i--)
		{
			if (state ^ input[i] == '+')
			{
				state = !state;
				flips++;
			}
		}

		cout << flips << endl;
    }

	/*cin.close();
	cout.close();*/
    
    return 0;
}
