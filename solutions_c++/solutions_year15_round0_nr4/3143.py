#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>	
#include <ctime>
#include <cstring>

using namespace std;
#define ll long long
#define EPS 0.00000001


int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int t, z = 1;
	int c, r, x, a, b;
	fin >> t;
	string richard = "RICHARD", gab = "GABRIEL";
	string ans;
	while (t--){
		fin >> x >> r >> c;
		a = min(r, c);
		b = max(r, c);
		if (x > b) ans = richard;
		else if (x == 1) ans = gab;
		else if (x == 2){
			if ((a * b) % 2) ans = richard;
			else ans = gab;
		}
		else if (x == 3){
			if ((a * b) % 3 || (a * b) == 3) ans = richard;
			else ans = gab;
		}
		else if (x == 4){
			if (a <= 2) ans = richard;
			else ans = gab;
		}
		fout << "Case #" << z << ": " << ans << endl;
		z++;
	}

	fin.close();
	fout.close();
	return 0;
}