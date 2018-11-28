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

ll a[20000];
int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int t, z = 1;
	fin >> t;
	int n;
	while (t--){
		fin >> n;
		for (int i = 0; i < n; i++) fin >> a[i];
		ll a1 = 0;
		for (int i = 1; i < n; i++) if (a[i] < a[i - 1]) a1 += a[i - 1] - a[i];
		ll r = 0;
		for (int i = 1; i < n; i++) r = max(r, a[i - 1] - a[i]);
		ll a2 = 0;
		for (int i = 0; i < n - 1; i++){
			a2 += min(a[i], r);
		}
		fout << "Case #" << z << ": ";
		fout << a1 << " " << a2 << endl;
		z++;
	}






	fin.close();
	fout.close();
	return 0;
}