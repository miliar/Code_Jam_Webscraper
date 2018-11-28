#include <iostream>
#include <vector>
#include <set>
#include <fstream>
#include <iomanip>


using namespace std;



int main() {
	ofstream fout ("B-large.out");
	ifstream fin ("B-large.in");
    int T;
    fin >> T;
    for (int t = 1; t <= T; t++) {
        double C, F, X;
        fin >> C >> F >> X;
        double S = 2.0;
        double ans = X / S;
        int a = 0;
        while (ans > ans - X / (a*F + S) + C / (a*F + S) + X / ((a+1)*F + S)) {
            ans = ans - X / (a*F + S) + C / (a*F + S) + X / ((a+1)*F + S);
            a++;
        }
        fout.setf(ios::fixed);
        fout <<  "Case #" << t << ": " << setprecision(7) << ans << endl;
    }
}
