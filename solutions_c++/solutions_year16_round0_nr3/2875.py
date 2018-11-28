#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

typedef long long int lnum;


lnum Decimal(int system, int n)
{
    lnum res = 1;
    for (int i = 0; i < n; i++) {
        res *= system;
    }
    return res;
}


lnum ToInt(string s, int system)
{
    lnum sum = 0;
    for (int i = 0; i < s.length(); i++) {
        lnum n = (int(s[i]) - 48) * Decimal(system, (s.length() - i - 1));
        sum += n;
    }
    return sum;
}


lnum MinDivisor(lnum n)
{
    int root = sqrt(n) + 1;
    int i = 2;
    while (i < root && n % i) {
        i++;
    }
    if (i == root) {
        return n;
    } else {
        return i;
    }
}


pair<bool, vector<lnum> > IsJamcoin(string s)
{
    pair<bool, vector<lnum> > res;
    res.first = false;

    if (s[0] != '1' || s[s.length() - 1] != '1') {
        return res;
    }
    for (int i = 2; i <= 10; i++) {
        lnum n = ToInt(s, i);
        lnum div = MinDivisor(n);
        if (div == n) {
            return res;
        } else {
            res.second.push_back(div);
        }
    }
    res.first = true;
    return res;
}


ofstream ouf;
int max_cnt;
int cnt;
int gen(string prefix, int n)
{
    if (cnt >= max_cnt) {
        return 0;
    }
    if (n < prefix.length()) {
        prefix[n] = '0';
        gen(prefix, n + 1);
        prefix[n] = '1';
        gen(prefix, n + 1);
    } else {
        pair<bool, vector<lnum> > a = IsJamcoin(prefix);
        if (a.first) {
            cnt++;
            ouf << prefix << " ";
            for (int i = 0; i < a.second.size(); i++) {
                ouf << a.second[i] << " ";
            }
            ouf << "\n";
        }
    }
}


int main()
{
    ouf.open("out.txt");
    // j
    max_cnt = 50;
    // n
    int n = 16;
    string a = "";
    for (int i = 0; i < n; i++) {
        a.append("0");
    }
    gen(a, 0);

    ouf.close();
    return 0;
}
