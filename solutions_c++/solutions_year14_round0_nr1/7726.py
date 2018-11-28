#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <set>

using namespace std;

int fir[16];
int sec[16];
void solve(ifstream &in, ofstream &out, int i)
{
    out << "Case #" << i+1 << ": ";
    //read data
    int first, second;
    memset(fir, 0, sizeof(fir));
    memset(sec, 0, sizeof(sec));
    in >> first;
    for(int i = 0; i < 16; i++)
        in >> fir[i];
    in >> second;
    for(int i = 0; i < 16; i++)
        in >> sec[i];
    int same = 0, lastsame = 0;
    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j <4; j++)
        {
            if(fir[(first-1)*4+i] == sec[(second-1)*4+j])
            {
                same++;
                lastsame = fir[(first-1)*4+i];
            }
        }
    }
    if(same == 0)
        out << "Volunteer cheated!" << endl;
    else if(same == 1)
        out << lastsame << endl;
    else
        out << "Bad magician!" << endl;
}

void codeJam()
{
    ifstream in("D:\\WorkProjects\\CodeBlocks\\CodeJam\\A.in");
    ofstream out("D:\\WorkProjects\\CodeBlocks\\CodeJam\\A.out");
    int testcase;
    in >> testcase;

    for(int i = 0; i < testcase; i++) {
        solve(in, out, i);
    }
    in.close();
    out.close();
}

int main()
{
    codeJam();
    return 0;
}
