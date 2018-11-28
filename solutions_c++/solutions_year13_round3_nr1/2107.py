#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <memory.h>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <queue>
#include <list>

using namespace std;

string in;

int main () {

	ofstream myfile;
	myfile.open ("/Users/mac/Desktop/out.txt");
    ifstream filein ("/Users/mac/Desktop/A-large-practice.in");


	int t,n,len,goal;
	filein >> t;
	map <char, int> mm;
	mm['a'] = mm['e'] = mm['i'] = mm ['o'] = mm['u'] = 10;
	for(int i=1;i<=t;i++) {
		filein >> in >> n;
		len = in.length();	
		int count = 0;
		
		for(int j=len-1;j > -1;j--) {
			goal = n;
			for(int x = j;x > -1;x--) {	
				// cout << goal << " " << in[j] << " " << in[x] << " " << endl;
				if(mm[in[x]] != 10) {
					goal -= 1;
				}else {
					goal = n;
				}
				// cout << goal << " " << in[j] << " " << in[x] << " " << endl;
				if(goal == 0) {
					count += len - (len - x) + 1;
					break;
				}
			}
		}

		myfile << "Case #" << i << ": " << count << endl;

	}

	

}















