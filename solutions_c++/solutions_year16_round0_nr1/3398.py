#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    //ifstream fin("input.in");
    //ifstream fin("A-small-attempt0.in");
    ifstream fin("A-large.in");
    ofstream fout("output.out");

    if (!fin.is_open()) cout << "input.in open fail" << endl;
    if (!fout.is_open()) cout << "output.out open fail" << endl;

    int numCase;
    fin >> numCase;

    int i;
    long long n, answer;
    for (i = 0; i < numCase; i++)
    {
        fin >> n;
        if (n == 0) {
            cout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;
            fout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;
            continue;
        }

        int allNumber = 0;

        long long mult = n;
        long long tmp = mult;
        while (tmp > 0) {
           // cout << "found " << (tmp % 10)<< endl;
           allNumber = allNumber | (1 << (tmp % 10));
           tmp = tmp / 10;
        }

        while (allNumber != 0x3ff) {
            mult += n;
            long long tmp = mult;
            while (tmp > 0) {
               //cout << tmp << " " << tmp % 10<< " " << (1 << (tmp % 10)) << endl;
               //cout << "found " << (tmp % 10)<< endl;
               allNumber = allNumber | (1 << (tmp % 10));
               tmp = tmp / 10;
            }
        }

        answer = mult;
        cout << "Case #" << (i + 1) << ": " << answer << endl;
        fout << "Case #" << (i + 1) << ": " << answer << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
