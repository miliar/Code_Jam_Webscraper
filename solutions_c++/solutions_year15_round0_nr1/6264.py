#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <inttypes.h>
#include <string>
#include <fstream>

using namespace std;


int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	int T, n, count, i,j,obs,diff; 
	string file = "A-large.in";
	string outfile = "A-large.out";
	ifstream fs(file, ios::in);
	ofstream ofs(outfile, ios::out);
	string s;

	fs >> T;
	for (j = 1; j <= T; j++){
		fs >> n >> s;
		count = 0;
		obs = s[0]-'0';
		for (i = 1; i <= n; i++){
			diff = i - obs;
			if (diff > 0){
				count += diff;
				obs += diff;
			}
			obs += s[i]-'0';
		}
		ofs << "Case #" << j << ": " << count << endl;
	}
	fs.close();
	ofs.close();
	return 0;
}
