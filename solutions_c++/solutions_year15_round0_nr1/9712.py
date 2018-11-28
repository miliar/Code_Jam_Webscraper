#include <iostream>
#include <fstream>
using namespace std;


ifstream fin;
ofstream fout;


int solve(int smax, int scounts[])
{
    int i, acc = scounts[0];
    int ret = 0;
    for (i=1; i<=smax; i++)
    {
        if (scounts[i] > 0 && acc < i)
        {
            ret += i - acc;
            acc += ret;
        }
        acc += scounts[i];
    }
    return ret;
}


int main()
{
    fin.open("in.txt");
    fout.open("out.txt");

    int cases, ci, cj;
    int smax;
    int scounts[1001];
    int ans;
    char x;
    fin >> cases;
    for (ci=1; ci<=cases; ci++)
    {
        fin >> smax;
        for (cj=0; cj<=smax; cj++)
        {
            fin >> x;
            scounts[cj] = x-48;
        }
        ans = solve(smax, scounts);
        fout << "Case #" << ci << ": " << ans << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
