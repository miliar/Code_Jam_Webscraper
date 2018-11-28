#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

long long extract (string s)
{
    long long val = 0;

    for (int i=0; i<s.size(); i++)
    {
        val = val * 10LL;
        val = val + (long long)(s[i] - '0');
    }

    return val;
}

string fill (long long num)
{
    string ret = "";

    while (num != 0)
    {
        int c = num % 10LL;
        ret = (char)(c + '0') + ret;
        num = num / 10LL;
    }

    return ret;
}

long long palin1 (long long num)
{
    string tmp = "";
    string ans = "";
    string ret = "";
    long long val;

    tmp = fill (num);
    ans = tmp;
    reverse (tmp.begin(),tmp.end());
    ret = ans + tmp;
    val = extract (ret);

    return val;
}

long long palin2 (long long num)
{
    string tmp = "";
    string ans = "";
    string ret = "";
    long long val;

    tmp = fill (num);
    ans = tmp;
    tmp = tmp.substr(0,tmp.size()-1);
    reverse (tmp.begin(),tmp.end());
    ret = ans + tmp;
    val = extract (ret);

    return val;
}

int main ()
{
    ifstream fin ("C.in");
    ofstream fout ("C.out");

    int t;
    int k = 1;

    fin >> t;

    while( t -- )
    {
        long long a,b;
        long long cnt = 0;

        fin >> a;
        fin >> b;

        for (long long i=1; i<10000; i++)
        {
            long long fir = palin1(i);
            long long sec = palin2(i);
            fir = fir * fir;
            sec = sec * sec;
            if (fir >= a && fir <= b)
            {
                string FIR = "" , FIRTMP = "";
                FIR = fill (fir);
                FIRTMP = FIR;
                reverse(FIRTMP.begin(),FIRTMP.end());
                if (FIR == FIRTMP)
                    cnt = cnt + 1LL;
            }
            if (sec >= a && sec <= b)
            {
                string SEC = "" , SECTMP = "";
                SEC = fill (sec);
                SECTMP = SEC;
                reverse(SECTMP.begin(),SECTMP.end());
                if (SEC == SECTMP)
                    cnt = cnt + 1LL;
            }
        }

        fout << "Case #" << k ++ << ": ";
        fout << cnt << "\n";
    }
}
