#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("data/A-large.in");
    ofstream fout("data/A-large.out");

    int test_cnt = 0;
    fin >> test_cnt;

    for (int test_case = 1; test_case <= test_cnt; ++test_case) {
        std::string line; int k;
        fin >> line >> k;

        int kend = (int)line.size() - k;

        int res = 0;
        for (int i = 0; i <= kend; ++i) {
            if (line[i] == '-') {
                res++;
                for (int j = 0; j < k; ++j) line[i + j] = (line[i+j]=='-'?'+':'-');
            }
        }

        for (int i = 0; i < (int)line.size(); ++i) {
            if (line[i] == '-') {
                res = -1;
                break;
            }
        }


        fout << "Case #" << test_case << ": ";
        if (res >= 0) fout << res << endl;
        else fout << "IMPOSSIBLE"  << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
