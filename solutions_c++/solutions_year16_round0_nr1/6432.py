/* 
 * File:   main.cpp
 * Author: Sebastan
 *
 * Created on April 8, 2016, 5:53 PM
 */

#include <iostream>
#include <cmath>
#include <string.h>
//#include "hashmap.h"
using namespace std;
bool digits[10][100];
int T;
string number;
int n;
unsigned long long N, iN;
int allSum;
int main(int argc, char** argv) {

	cin >> T;
	for (int c = 0; c < T; ++c)
	{
		int cont = 0;
		allSum = 0;
		iN = 0;
		cin >> n;
		if (n == 0)
			cout << "Case #" << c+1 << ": " << "INSOMNIA" << endl;
		else
		{
			while(allSum !=45 || !digits[0][c])
			{
				iN += n;
				number = to_string(iN);
				for (int i = 0; i < number.size(); ++i)
				{
					if (!digits[number[i] - '0'][c])
					{
						digits[number[i] - '0'][c] = true;
						allSum += (number[i] - '0');
					}
				}
			}
		cout << "Case #" << c+1 << ": " << iN << endl;
		}
	}
    return 0;
}

