#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");

//#define fin cin
//#define fout cout

int main()
{
    int t;
    fin >> t;
    for(int cas = 1; cas <= t; cas++)
    {

        fout << "Case #" << cas << ": ";
        string str;
        fin >>str;
        int len = str.length(), ans = 0;
        for(int i = 0; i < len - 1; i++)
        {
            if(str[i] != str[i + 1])ans++;
        }
        cout << ans << endl;
        if(ans == 0 && str[0] == '+')
        {
            fout << "0" << endl;
            continue;
        }
        if(ans == 0 && str[0] == '-')
        {
            fout << "1" << endl;
            continue;
        }
        if(str[len - 1] == '-')ans++;
        fout << ans << endl;
    }
    return 0;
}
