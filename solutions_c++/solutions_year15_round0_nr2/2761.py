#include <iostream>
#include <map>
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("Bresultlarge1.out");


int main() {
    int t, n, pi, cases = 1;
    string str;
    fin >> t;
    //map<int, int> mp;
    while (t--) {
        vector<int> vv;

        fin >> n;
        int maxpi = 0;
        for (int i = 0; i < n; ++i) {
            fin >> pi;
            maxpi = max(maxpi, pi);
            vv.push_back(pi);
        }
        int sizevv = vv.size();
        int res = 1000000000;
        for (int i = 1; i <= maxpi; ++i) {
            int tmpsum = 0;
            for (int j = 0; j < sizevv; ++j) {
                tmpsum += ((vv[j] - 1) / i);
            }
            tmpsum += i;
            res = min(res, tmpsum);
        }

        fout << "Case #" << cases++ << ": " << res << endl;
    }

	return 0;
}
