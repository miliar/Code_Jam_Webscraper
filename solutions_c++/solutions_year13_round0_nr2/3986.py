#include<iostream>
#include<fstream>
#include<cstdio>
//#define inp cin
//#define out cout
using namespace std;
int arr[105][105];
int main()
{
    ifstream inp("input.txt");
    ofstream out("output.txt");
    int t,n,m;
    inp>>t;
    for(int T=1;T<=t;++T)
    {
        int maxrow[105]={};
        int maxcol[105]={};
        inp>>n>>m;
        for(int i=1;i<=n;++i)
        {
            for(int j=1;j<=m;++j)
            {
                inp>>arr[i][j];
            }
        }
        for(int i=1;i<=n;++i)
        {
            for(int j=1;j<=m;++j)
            {
                maxrow[i] = max(maxrow[i],arr[i][j]);
            }
        }
        for(int i=1;i<=m;++i)
        {
            for(int j=1;j<=n;++j)
            {
                maxcol[i] = max(maxcol[i],arr[j][i]);
            }
        }
        bool flag=0;
        for(int i=1;i<=n;++i)
        {
            for(int j=1;j<=m;++j)
            {
                if(arr[i][j]!=min(maxrow[i],maxcol[j]))
                {
                    flag=1;break;
                }
            }
            if(flag)break;
        }
        out<<"Case #"<<T<<": ";
        if(flag)out<<"NO\n";
        else out<<"YES\n";
    }
    return 0;
}
