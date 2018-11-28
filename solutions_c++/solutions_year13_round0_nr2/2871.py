#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <fstream>
using namespace std;
int ma[100][100];
int m, n;
bool compu(int i, int j)
{
    bool res1 = true, res2 = true;
    for(int ii = 0; ii < n; ++ii)
        if(ma[ii][j] > ma[i][j])
            res1 = false;
    for(int jj = 0; jj < m; ++jj)
        if(ma[i][jj] > ma[i][j])
            res2 = false;
    return (res1 or res2);
}
string judge( )
{
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j)
        {
            bool c = compu(i,j);
            if(!c)
                return "NO";
        }
    }
    return "YES";
}
int main()
{
    fstream fin;
    ofstream fout;
    fin.open("test.in");
    fout.open("res.out");
int t;fin>>t;
for(int times = 0; times < t; ++times)
{
//FW
    fin >> n >> m;
    string res;
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j)
            fin >> ma[i][j];
    res = judge();
    fout <<"Case #"<<times+1<<": ";
    fout << res<<endl;

//FW
}
fout.close();
}
