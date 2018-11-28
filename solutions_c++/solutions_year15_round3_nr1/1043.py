#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include<bitset>
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
	fin >> t;


	int n, m, w;



	while (t--){
		fin >> n >> m >> w;
		int ans = 0;
		if (n > 1){
			ans += (n - 1) * (m / w);
		}
		ans += (m / w);
		ans += w - 1;
		if (m % w) ans++;
		//--
		fout << "Case #" << z << ": ";
		z++;
		//--

		fout << ans << endl;
	}



	fin.close();
	fout.close();
	return 0;
}