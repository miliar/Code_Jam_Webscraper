#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <fstream>


using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
	ifstream fin("D-large.in");
	ofstream fout("out3.txt");
	int n;		
	int i, j, k, l;
	fin >> n;
	for(i = 0; i < n; i++) {
		int num;
		fin >> num;
		int pt1 = num, pt2 = 0;
		vector<double> Naomi(num, 0.0);
		vector<double> Ken(num, 0.0);

		for(j = 0; j < num; j++) {
			fin >> Naomi[j];
		}
		for(j = 0; j < num; j++) {
			fin >> Ken[j];
		}

		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());

		j = num - 1;
		k = num - 1;
		while(j >= 0 && k >= 0) {
			if(Naomi[j] > Ken[k]) {
				pt2++;
				j--;
				k--;
			}
			else k--;
		}

		j = 0;
		k = 0;
		while(k < num) {
			if(Naomi[j] < Ken[k]) {
				pt1--;
				j++;
				k++;
			}
			else k++;						
		}

		fout << "Case #" << i+1 << ": " << " " << pt2 << " " << pt1 << endl;
	}

	fout.close();
	fin.close();
	
    return 0;
}
