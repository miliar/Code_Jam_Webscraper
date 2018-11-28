#include <stdio.h>
#include <iostream>
#include <string>
#include <math.h>
#include <sstream>

using namespace std;
bool cekPalindrom(string word);
bool cekFairNSquare(int numb);

int main()
{
    int t;
    scanf("%d", &t);
    for(int s=0; s<t; s++)
    {
        int awal, akhir;
        int ctr = 0;
        scanf("%d %d", &awal, &akhir);
        for (int i=awal; i<=akhir; i++)
        {
            if(cekFairNSquare(i))
            {
                ctr++;
            }
        }
        cout << "Case #" << s+1 << ": " << ctr << "\n";
    }
    return 0;
}

bool cekPalindrom(string word)
{
    string temp = string(word.rbegin(), word.rend());
    if(word.compare(temp)==0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool cekFairNSquare(int numb)
{
    int hasil = sqrt(numb);

    if(hasil*hasil == numb)
    {
        stringstream ss;
        ss << numb;
        string s = ss.str();
        if (cekPalindrom(s))
        {
            stringstream ss2;
            ss2 << hasil;
            s = ss2.str();
            if(cekPalindrom(s))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }
}
