/*
 * CreditStore.c
 *
 *  Created on: Mar 30, 2014
 *      Author: mania
 */

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <math.h>
#include <complex.h>
#include <unistd.h>
#include <stdlib.h>     /* atoi */
using namespace std;

static const string filename = "SampleStoreCredit.txt";
int N, n;
int c;

#define fori(i,a,b) for(int i=a; i<b; i++)

int main() {

	string inFile = "./input/" + filename;
	string outFile = "./output/" + filename;

	freopen(inFile.c_str(), "rt", stdin);
	freopen(outFile.c_str(), "wt", stdout);

	string s;
	// read first line (N: number of tests)
	cin >> N;

	fori(ln, 1, N+1)
	{
		cout << "Case #" << ln << ": ";
		cin >> n;
		int arr1[4];
		fori(i,0,4)
		{
			if ((i + 1) == n) {
				fori(j,0,4)
				{
					cin >> arr1[j];
				}
			} else {
				fori(j,0,4)
				{
					cin >> s;
				}
			}
		}
		cin >> n;
		int arr2[4];
		fori(i,0,4)
		{
			if ((i + 1) == n) {
				fori(j,0,4)
				{
					cin >> arr2[j];
				}
			} else {
				fori(j,0,4)
				{
					cin >> s;
				}
			}
		}
		int x,y; x=y = 0;
		fori(i,0,4)
		{
			fori (j,0,4)
			{
				if (arr1[i] == arr2[j]) {
					x++;
					y = i;
				}
			}
		}

		if (x == 1) {
			cout << arr1[y];
		} else if (x > 1) {
			cout << "Bad magician!";
		} else {
			cout << "Volunteer cheated!";
		}

		cout << endl;
	}

	float seconds = float(clock()) / CLOCKS_PER_SEC;

	fclose(stdin);
	fclose(stdout);

	return 0;
}

