#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include "InfInt.h"

using namespace std;

vector<InfInt> vecPrimers;

bool IsPrime(InfInt a)
{
    for (InfInt i = 2; i < 1000; ++i)
    {
        if (a % i == 0)
        {
            return false;
        }
    }
    return true;
}


void GetValue(vector<InfInt>& vec, int n)
{
    for (int j = 2; j <= 10; j++)
    {
        InfInt reslut = 1;
        for (int i = 0; i < n - 1; i++)
        {
            reslut *= j;
        }
        vec[j-2] =(reslut + 1);
    }
}
string GetValueStr(InfInt a, InfInt base)
{
    string result = "";
    while (a > 0)
    {
        result.insert(result.begin(), (a%base).toString()[0]);
        a /= 2;
    }
    return result;
}

InfInt StrToValue(string& str, InfInt base)
{
    InfInt count = 1;
    InfInt result = 0;
    for (int i = str.size()-1; i >=0; --i)
    {
        result += count * (str[i] - '0');
        count *= base;
    }
    return result;
}

void GetNext(vector<InfInt>& vec)
{
    vec[0] += 2;
    string strb = GetValueStr(vec[0], 2);
    for (int i = 1; i < 9; i++)
    {
        vec[i] = StrToValue(strb, i+2);
    }
}



bool IsPrime(vector<InfInt>& vec)
{
    for (int i = 0; i < 9; i++)
    {
        if (IsPrime(vec[i]))
        {
            return true;
        }
    }
    return false;
}

int main()
{
    errno_t err;
    FILE* fin = nullptr;
    err = freopen_s(&fin, "C-small-attempt0.in", "r", stdin);
    if (err != 0)
        fprintf(stdout, "error on freopen\n");

    FILE* fout = nullptr;
    err = freopen_s(&fout, "output.out", "w", stdout);
    if (err != 0)
        fprintf(stdout, "error on freopen\n");

    int T = 0;
    cin >> T;
    vector<InfInt>vecV(9, 0);
    for (size_t i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ": "<<endl;
        long n = 0, m = 0;
        cin >> n >> m;
        GetValue(vecV, n);
        for (int j = 0; j < m; j++, GetNext(vecV))
        {
            vector<InfInt> vecR(9, 0);
            while (IsPrime(vecV))
            {
                GetNext(vecV);
            }
            for (int k = 0; k < 9; k++)
            {
                InfInt ullb = vecV[k];
                for (InfInt t = 2; t < ullb; ++t)
                {
                    if (vecV[k] % t == 0)
                    {
                        vecR[k] = t;
                        break;
                    }
                }
            }

            string result = "";
            string rrrr = GetValueStr(vecV[0],2);
            result.append(rrrr);
            for (int bt = 0; bt < 9; bt++)
            {
                result.append(" ");
                result.append(vecR[bt].toString());
            }
            cout << result << endl;
        }
        



        
    }


}
