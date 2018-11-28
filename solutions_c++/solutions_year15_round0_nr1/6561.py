#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include<cmath>
#include<fstream>
#include <iostream>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T, i, j;
	in >> T;

	for (i = 1; i <= T; i++){
		int sMax;
		int standing = 0;
		int friends = 0;
		int arr[1001] = { 0, };		
		char str[1001];
		in >> sMax >> str;
		
		for (j = 0; j <= sMax; j++){
			arr[j] = (int)str[j] - 48;
		}

		standing = arr[0];

		for (j = 1; j <= sMax; j++){
			
			if (j <= standing){
				standing += arr[j];
			}
			else if (j > standing && arr[j] > 0){
				int fr = j - standing;
				friends += fr;
				standing += fr;
				standing += arr[j];
			}
			
		}
		
		out << "Case #"<<i<<": "<<friends<< endl;

	}

	in.close();
	out.close();
	return 0;
}