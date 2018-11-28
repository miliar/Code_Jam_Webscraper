#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

struct GCase
{
    long long A,B;
    bool checkPalindrome(long long v)
    {
        char ch[200];
        int nD = log((double)v)/log(10.0) + 1;
        itoa(v, ch, 10);
        bool ret = true;
        for (int i = 0; i < nD/2; ++i)
            if (ch[i] != ch[nD-i-1])
                return false;
        return ret;
    }
    bool checkSquarePalindrome(long long v)
    {
        long long sv = sqrt((double)v);
        if (sv*sv != v)
            return false;
        if (checkPalindrome(sv))
            if (checkPalindrome(v))
                return true;
        return false;
    }
    long long output()
    {
        long long cnt = 0;
        for (long long i = A; i <= B; ++i)
            if (checkSquarePalindrome(i))
                ++cnt;
        return cnt;
    }
};

int g_nCases = 0;
vector<GCase*> g_cases;

void read_input()
{
    cin >> g_nCases;
    for (int i = 0; i < g_nCases; ++i)
    {
        GCase* gc = new GCase;
        // do sth
        cin >> gc->A >> gc->B;
        g_cases.push_back(gc);
    }
}

int main(int argc, char**argv)
{
    read_input();

    for (int i = 0; i < g_nCases; ++i)
    {
        long long a = g_cases[i]->output();
        cout << "Case #" << i+1 << ": " << a;
        cout << endl;
    }
    return 0;
}
