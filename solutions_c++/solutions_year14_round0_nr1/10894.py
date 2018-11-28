#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <fstream>
using namespace std;
int a[5][5];
int b[5][5];
int testCase;
int main()
{
    int T,first,second;
    int total = 0;
    int ans = 0;
    ifstream fin("abc.txt");
    ofstream fout("a.txt");
    fin>>T;
    for(testCase = 1; testCase <= T;testCase++)
    {
        total = 0;
        ans = 0;
        fin>>first;
        for(int i = 1; i <= 4; i++)
        {
            for(int j = 1; j <= 4; j++)
            {
                fin>>a[i][j];
            }
        }
        fin>>second;
         for(int i = 1; i <= 4; i++)
        {
            for(int j = 1; j <= 4; j++)
            {
                fin>>b[i][j];
            }
        }
        for(int i = 1; i <= 4; i++)
        {
            for(int j = 1; j <=4; j++)
            if(a[first][i] == b[second][j])
            {
                total++;
                ans = a[first][i];
            }
        }
        if(total == 1)
        fout<<"Case #"<<testCase<<": "<<ans<<endl;
        else if(total == 0)
        fout<<"Case #"<<testCase<<": "<<"Volunteer cheated!"<<endl;
        else fout<<"Case #"<<testCase<<": "<<"Bad magician!"<<endl;
    }
    return 0;
}
