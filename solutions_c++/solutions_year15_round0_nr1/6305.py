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
	int t, n, z = 1;
	fin >> t;
	string s;
	while (t--){
		fin >> n >> s;
		int cnt = 0, ans = 0;
		for (int i = 0; i< s.size(); i++){
			if (s[i] > '0') {
				ans += max(0, (i - cnt));
				cnt += max(0, (i - cnt));
			}
			cnt += (s[i] - '0');
		}
		fout << "Case #" << z << ": " << ans << endl;
		z++;
	}


	fin.close();
	fout.close();
	return 0;
}