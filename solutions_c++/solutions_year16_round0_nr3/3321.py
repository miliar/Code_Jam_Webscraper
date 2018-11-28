#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
using namespace std;

ofstream fout("aout.txt");
ifstream fin("C-small-attempt3.in");

void print (vector<long long> a) {
    for (long long i = 0; i < a.size(); i++)
        fout << a[i];
}

bool IsPrime(long long a) {
    for (long long i = 2; i * i <= a; i++) {
        if (a % i == 0)
            return false;
    }
    return true;
}

long long MinDivisor(long long a) {
    long long i = 2;
    for (; a % i != 0; i++){}
    return i;
}

int main()
{
    long long n, m, t;
    fin >> t >> n >> m;
    fout << "Case #1:" << endl;
    long long solved = 0;
    for (long long i = pow(2, n - 1) + 1; i < pow(2, n) && solved < m; i += 2){
        vector<long long> temp(n);
        long long tn = i, j = 0;
        while (tn > 0) {
            temp[j++] = tn % 2;
            tn /= 2;
        }
        bool flag = 1;
        vector<long long> MinDivisors(9);
        for (long long j = 2; j < 11; j++) {
            //j is base
            long long cur = 0, k = 1;
            for (long long p = 0; p < temp.size(); p++) {
                cur += k * temp[p];
                k *= j;
            }
            if (IsPrime(cur)) {
                flag = 0;
            }
            else {
                //fout << "WTF";
                MinDivisors[j - 2] = MinDivisor(cur);
            }
            //fout << "WITH " << i << " IT WAS " << cur << " ON " << j << endl;
        }
        if (flag == 1) {
            reverse(temp.begin(), temp.end());
            print(temp);
            for (long long j = 0; j < 9; j++)
                fout << " " << MinDivisors[j];
            fout << endl;
            solved++;
        }
    }
    return 0;
}
