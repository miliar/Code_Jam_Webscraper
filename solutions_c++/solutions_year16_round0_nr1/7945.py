// число на цифры.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <fstream>

using namespace std;

void parse(long long n, vector<short int>& vec) {
	while (n != 0)
	{
		vec.insert (vec.begin(),n % 10);
		n = n / 10;
	}
}

int main() {
	ofstream fout("output.out");
	ifstream fin("A-large.in");
	short int n;
	fin >> n;
	long long num,num_out;
	for (int i = 1;i <= n;i++) {
		fin >> num;
		num_out = 0;
		if (num == 0) {
			fout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		int a[10];
		for (int j = 0;j < 10;j++)
			a[j] = 1;
		short int sum;
		do {
			num_out += num;
			sum = 0;
			vector <short int> vec;
			parse(num_out, vec);
			for (unsigned int j = 0;j < vec.size();j++)
				a[vec[j]] = 0;
			for (int k = 0;k < 10;k++)
				sum += a[k];
			
		} while (sum > 0);
		fout << "Case #" << i << ": "<< num_out << endl;
		}

	

	cout << endl;
}

