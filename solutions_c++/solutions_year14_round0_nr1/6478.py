#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <memory.h>
#include <assert.h>
using namespace std;

ifstream fin;
ofstream fout;

int testNum;
int rowChoice1, rowChoice2;
int rowProf1[4];
int rowProf2[4];

void init();
void solve(int &status, int &pos);
void output(int status, int pos, int T);

bool isFactorialofTwo(int n){
    return (n>0)?((n & (n-1))== 0):false;
}

int main()
{
    int T;
    fin.open("A-small-attempt1.in");
    fout.open("A-small-attempt1.out");
    fin >> testNum;
    for (T=1; T<=testNum; T++)
    {
        int res, pos;
        init();
        solve(res, pos);
        output(res, pos, T);
    }
    fin.close();
    fout.close();
    return 0;
}

void init()
{
    memset(rowProf1, 0, sizeof(int)*4);
    memset(rowProf2, 0, sizeof(int)*4);
    fin >> rowChoice1;
    for (int i=0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {
            int tmp;
            fin >> tmp;
            rowProf1[i] |= (1 << (tmp-1));
        }
    }
    fin >> rowChoice2;
    for (int i=0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {
            int tmp;
            fin >> tmp;
            rowProf2[i] |= (1 << (tmp-1));
        }
    }
}

void solve(int &status, int &pos)
{
    int ret = rowProf1[rowChoice1-1] & rowProf2[rowChoice2-1];
    pos = 0;
    if (ret == 0)
    {
        status = 0;
    }
    else if (isFactorialofTwo(ret))
    {
        status = 1;
        while (ret)
        {
            pos ++;
            ret = ret >> 1;
        }
    }
    else
    {
        status = -1;
    }
}
void output(int status, int pos, int T)
{
    switch (status){
        case 1:
            fout << "Case #"<<T<<": " << pos << endl;
            break;
        case 0:
            fout << "Case #"<<T<<": Volunteer cheated!" << endl;
            break;
        default:
            fout << "Case #"<<T<<": Bad magician!" << endl;
            break;
    }
}
