#include <fstream>
#include <set>

using namespace std;

int main() {
        ifstream fin("A-small-attempt0.in");
        ofstream fout("A-small-attempt0.out");
        int T;
        fin >> T;
        for (int casenum = 1; casenum <= T; ++casenum) {
                int a, b, p[4][4], q[4][4];
                fin >> a;
                for (int i = 0; i < 4; ++i)
                        for (int j = 0; j < 4; ++j)
                                fin >> p[i][j];
                fin >> b;
                for (int i = 0; i < 4; ++i)
                        for (int j = 0; j < 4; ++j)
                                fin >> q[i][j];
                set<int> s;
                for (int i = 0; i < 4; ++i) s.insert(p[a - 1][i]);
                int cnt = 0, ans;
                for (int i = 0; i < 4; ++i)
                        if (s.find(q[b - 1][i]) != s.end())
                                ++cnt, ans = q[b - 1][i];
                fout << "Case #" << casenum << ": ";
                if (cnt == 1)
                        fout << ans;
                else if (cnt == 0)
                        fout << "Volunteer cheated!";
                else
                        fout << "Bad magician!";
                fout << '\n';
        }
        fin.close();
        fout.close();
        return 0;
}