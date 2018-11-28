#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
using namespace std;
string solve (istream &cin)
{
    int n, m;
    cin>>n>>m;
    vector<vector<int> > v(n, vector<int>(m));
    for (int i=0;i<n;++i)
    {
        for (int j=0;j<m;++j)
        {
            cin>>v[i][j];
        }
    }
    for (int i=0;i<n;++i)
    {
        int a=0;
        for (int j=0;j<m;++j)
        {
            if (v[i][j]==1)
            {
                ++a;
            }
        }
        if (a==m)
        {
            for (int j=0;j<m;++j)
            {
                v[i][j]=3;
            }
        }
    }
    for (int i=0;i<m;++i)
    {
        int a=0;
        for (int j=0;j<n;++j)
        {
            if (v[j][i]==1 || v[j][i]==3)
            {
                ++a;
            }
        }
        if (a==n)
        {
            for (int j=0;j<n;++j)
            {
                v[j][i]=3;
            }
        }
    }
    for (int i=0;i<n;++i)
    {
        for (int j=0;j<m;++j)
        {
            if (v[i][j]==1)
            {
                return "NO";
            }
        }
    }
    return "YES";
}
int main()
{
    ifstream cin ("B-small-attempt0.in");
    ofstream cout("output.txt");
    int t;
    cin>>t;
    for (int i=0;i<t;++i)
    {
        cout<<"Case #"<<i+1<<": "<<solve(cin)<<endl;
    }
    return 0;
}
