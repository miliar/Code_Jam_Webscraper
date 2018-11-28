#include <fstream>
#include <iterator>
#include <string>

using namespace std;

int main () {
	int T;
	ifstream fin ("input.txt");
	ofstream fout ("output.txt");
    fin >> T;
    for (int t = 0; t < T; t++) {
    	string s;
    	fin >> s;
    	int n = s.length();
    	int dp1[102], dp2[102];
    	if (s[0] == '-') {
    		dp1[0] = 1;
    		dp2[0] = 0;
    	} else {
    		dp1[0] = 0;
    		dp2[0] = 1;
    	}
    	for (int i = 1; i < n; i++) {
    		if (s[i] == '-') {
    			dp2[i] = dp2[i - 1];
    			dp1[i] = dp2[i - 1] + 1;
    		} else {
    			dp1[i] = dp1[i - 1];
    			dp2[i] = dp1[i - 1] + 1;
    		}
    	}
    	fout << "Case #" << t + 1 << ": " << dp1[n - 1] << endl;

    }
    fin.close ();
    fout.close ();
    return 0;
}
