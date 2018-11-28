#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int p[2000];
int p1[2000];

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    if (!fin) {
        cout << "File not found" << endl;
        return 0;
    }
    int t;
    fin >> t;
    for (int tcase = 0; tcase < t; tcase++) {
        int d;
        fin >> d;

        for (int i = 0; i < d; i++) {
            fin >> p[i];
        }
        make_heap(p, p + d);
        int start = p[0];
        int minf = start;
        for (int m = start - 2; m > 0 ; m--) {
            copy(p, p + d, p1);
            int d1 = d;
            int mv = 0;
            while ((p1[0] > m) && (mv < start - m - 1)) {
                pop_heap(p1, p1 + d1);
                int el = p1[d1 - 1];
                p1[d1 - 1] = m;
                p1[d1] = el - m;
                push_heap(p1, p1 + d1);
                d1++;
                push_heap(p1, p1 + d1);
                mv++;
            }
            if (p1[0] <= m) {
                int minf1 = mv + m;
                if (minf > minf1) {
                    minf = minf1;
                }
            }
        }
        fout << "Case #" << (tcase + 1) << ": " << minf << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
