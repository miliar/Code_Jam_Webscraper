#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");


    int test_cnt = 0;
    fin >> test_cnt;

    for (int test_case = 1; test_case <= test_cnt; ++test_case) {
        int res = 0, Smax = 0;
        std::string digits;
        fin >> Smax >> digits;

        int standing = 0;
        for (int idx = 0; idx <= Smax; ++idx) {
            int cur = digits[idx] - '0';
            if (cur > 0 && standing < idx) {
                res += (idx - standing);
                standing += (idx - standing);
            }
            standing += cur;
        }

        fout << "Case #" << test_case << ": " << res << endl;
    }

    fin.close();
    fout.close();

    return 0;
}

