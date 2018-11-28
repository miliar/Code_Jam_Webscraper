#include <iostream>
#include <fstream>
using namespace std;
const int MAXN = 100;
bool digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

bool check_num(int v)
{
    int mod;
    while (v)
    {
        mod = v % 10;
        v /= 10;
        digits[mod] = true;
    }
    for (int i = 0; i < 10; ++i)
    {
        if (! digits[i]) return true;
    }
    return false;
}
void nil_digits()
{
    for (int i = 0; i < 10; ++i)
    {
        digits[i] = false;
    }
}
int main(int argc, char * argv[]) {

    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int T;
    int N;
    int curVal;
    fin >> T;
    for (int i = 1; i <= T; ++i)
    {
        fin >> N;
        if (N == 0)
        {
            fout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        nil_digits();
        curVal = N;
        while (check_num(curVal))
        {

            //cerr << curVal << endl;
            curVal += N;
        }
        fout << "Case #" << i << ": " << curVal << endl;
        //cerr << N << " - " << curVal << endl;
    }
    return 0;
}
