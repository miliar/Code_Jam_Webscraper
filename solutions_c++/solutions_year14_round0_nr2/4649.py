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
	ifstream fin("input2.in");
	ofstream fout("out2.txt");
	int n;	
	
	int i, j, k, l;
	fin >> n;
	cout << n << endl;

	for(i = 0; i < n; i++) {
		double currentRate = 2.0;
		double extra = 0.0;
		double cost = 0.0;
		double total = 0.0;
		double t = 0.0;

		fin >> fixed >> setprecision(7) >> cost; //cout << fixed << setprecision(7) << cost << endl;
		fin >> fixed >> setprecision(7) >> extra; //cout << fixed << setprecision(7) << extra << endl;
		fin >> fixed >> setprecision(7) >> total; //cout << fixed << setprecision(7) << total << endl;

		while(total/currentRate - (cost/currentRate + total/(currentRate + extra)) > 1e-7) {
			//cout << i << endl;
			t += cost/currentRate;
			currentRate += extra;
			//if(i == 3) cout << "**" << currentRate << endl;
		}
		t += total/currentRate;
		
		fout << "Case #" << i+1 << ": " << fixed << setprecision(7) << t << endl;
	}

	fout.close();
	fin.close();
	
    return 0;
}
