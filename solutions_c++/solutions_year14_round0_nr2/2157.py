#include <iostream>
#include <fstream>
#include <iomanip> 
using namespace std;
int main() {
	ifstream fin("B-large.in");
	ofstream fout("out.txt");
	int t, n;
	double c, f, x, ans;
	fin >> t;
	for (int k = 0; k < t; k++){
		fin >> c >> f >> x;
		n = 0;
		ans = 1.0 * x / 2;
		
		while (true){
			double tmp = 0.0;
			n++;
			for (int i = 0; i < n; i++)
				tmp += 1.0 / (2 + i * f);

			tmp *= c;
			tmp += x / (2 + n * f);
			if (tmp > ans)
				break;
			else
				ans = tmp;
		}
		fout << "Case #" << k + 1 << ": ";
		fout << setprecision(7) << setiosflags(ios::fixed | ios::showpoint) << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}