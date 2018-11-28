#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <set>

using namespace std;

void solve(ifstream &in, ofstream &out, int i)
{
    out << "Case #" << i+1 << ": ";
    out.precision(16);
    in.precision(16);
    //read data
    double c, f, x;
    in >> c >> f >> x;
    double res = x / 2, pre = 0;
    double rate = 2;
    while(1)
    {
        double cur = 0;
        pre += c / rate;
        rate += f;
        cur = pre + x / rate;
        if(res < cur)
            break;
        else
            res = cur;
    }
    out << res << endl;
}

void codeJam()
{
    ifstream in("D:\\WorkProjects\\CodeBlocks\\CodeJam\\B.in");
    ofstream out("D:\\WorkProjects\\CodeBlocks\\CodeJam\\B.out");
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
