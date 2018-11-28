#include<iostream>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<string.h>
#include<sstream>
using namespace std;
int plaind(string s, int st, int en)
{
    if(st == en || st > en)
          return 1;
    if(s[st] != s[en])
          return 0;
    return plaind(s, st+1, en-1);
}
int main()
{
    ifstream ifile ("C-small-attempt0.in");
    ofstream ofile ("output1.out");
    int t, a, b, val, cnt, flag1, flag2;
    string s, res;
    ifile >> t;
    getline(ifile, s);
    for(int k = 0 ; k < t ; k++)
    {
        ifile >> a >> b;
        val = (int)sqrt(a);
        cnt = 0;
        for(int i = val ; (i * i) <= b ; i++)
        {
            flag1 = 0, flag2 = 0;
            if(i * i < a)
                 continue;
            ostringstream convert;
            convert << i;
            res = convert.str();
            flag1 = plaind(res, 0, res.size()-1);
            if(flag1 == 0)
                 continue;
            ostringstream convert1;
            convert1 << i*i;
            res = convert1.str();
            flag2 = plaind(res, 0, res.size()-1);
            if(flag1 == 1 && flag2 == 1)
                 cnt++;
        }
        ofile << "Case #" << k+1 << ": " << cnt;
        if (k != t-1)
           ofile << endl;
    }
    ifile.close();
    ofile.close();
    return 0;
}
