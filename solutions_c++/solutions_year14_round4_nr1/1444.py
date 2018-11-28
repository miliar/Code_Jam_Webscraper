#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int n, m;
int a[100000];
bool v[100000];

int solve()
{
    int ans=0,i,j;
    for(i=0; i<n; ++i)
        v[i]=false;
    j=0; 
    sort(a, a+n);
    for(i=n-1; i>=j; --i)
    {
        if(a[i]+a[j]<=m)
            ++j;
        ans++;
    }
    return ans;
}

int main()
{
    int t,tt;
    fin>>tt;
    for(t=1; t<=tt; ++t)
    {
        fin >> n >> m;
        for(int i=0; i<n; ++i)
            fin>>a[i];
        fout<<"Case #"<<t<<": ";
        fout<<solve();
        fout<<endl;
    }
    return 0;
}

