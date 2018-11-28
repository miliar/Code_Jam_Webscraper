#include <iostream>
#include <fstream>
#include <vector>
#include <limits>
#include <math.h>
#include <algorithm>

#define MAXN 10

using namespace std;

int T,N,N1,_min;
int motes[MAXN];

int solve(int n,int j,int A);

int main()
{
    int A;
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    fin >> T;
    for (int i=1;i<=T;i++)
    {
        fin >> A >> N;
        N1=N;
        for (int j=0;j<N;j++)
            fin >> motes[j];
        sort(motes,motes+N);
        _min = MAXN;
        solve(0,0,A);
        fout << "Case #" << i << ": " << _min << endl;
    }
    return 0;
}

int solve(int n,int j,int A)
{
    if (n>=N)
    {
        if (n<_min) _min=n;
        return 0;
    }
    while(motes[j]<A && j<N1)
    {
        A+=motes[j];
        j++;
    }
    if (j==N1)
    {
        if (_min>n) _min=n;
        return 0;
    }
    N1--;
    solve(n+1,j,A);
    N1++;
    A+=A-1;
    solve(n+1,j,A);
    A=(A-1)/2;
    return 0;
}
