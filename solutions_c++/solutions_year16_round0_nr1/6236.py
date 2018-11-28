#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <memory.h>
#include <string>
#include <cmath>
#include <map>
#include <queue>
#include <fstream>

using namespace std;

int T, n, check[10], cnt;

void checking(int temp){
	while (temp > 0){
		if (check[temp % 10] == 0){
			check[temp % 10] = 1;
			cnt++;
		}

		temp = temp / 10;
	}
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("output.txt");

	fin >> T;

	for (int casen = 1; casen <= T; casen++){
		fin >> n;
		memset(check, 0, sizeof(check));
		cnt = 0;
		if (n == 0){
			fout << "Case #" << casen << ": INSOMNIA" << endl;
			continue;
		}

		int temp = n;
		for (int i = 1;; i++){
			checking(temp);
			if (cnt == 10){
				fout << "Case #" << casen << ": " << temp << endl;
				break;
			}

			temp += n;
		}
	}
}