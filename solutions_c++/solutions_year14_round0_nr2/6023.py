#include <fstream>
#include <iomanip>

using namespace std;

int main() {
        ifstream fin("B-large.in");
        ofstream fout("B-large.out");
        int T;
        fin >> T;
        for (int casenum = 1; casenum <= T; ++casenum) {
                double C, F, X, r = 2;
                fin >> C >> F >> X;
                double ans = 0;
                while (true) {
                        double t1 = X / r;
                        double t2 = C / r + X / (r + F);
                        if (t1 < t2) {
                                ans += t1;
                                break;
                        }
                        ans += C / r;
                        r += F;
                }
                fout << "Case #" << casenum << ": ";
                fout << fixed << setprecision(7) << ans << '\n';
        }
        fin.close();
        fout.close();
        return 0;
}