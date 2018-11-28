#include <iostream>
#include <fstream>
using namespace std;

int** a;

bool checkr(int i, int j, int n, int m)
{
    for(int k=0; k<m; k++)
    {
        if(a[i][k]>a[i][j])
            return false;
    }
    return true;
}
bool checkc(int i, int j, int n, int m)
{
    for(int k=0; k<n; k++)
    {
        if(a[k][j]>a[i][j])
            return false;
    }
    return true;
}

int main()
{
    int t;
    ifstream in;
    in.open("B-large.in");
    in>>t;
    ofstream out;
    out.open("out.txt");
    int c=0;
    int n,m;
    while(t>0)
    {
        t--;
        c++;
        in>>n>>m;
        a = new int*[n];
        for(int i=0; i<n; i++)
        {
            a[i] = new int[m];
        }
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                in>>a[i][j];
            }
        }
        bool f = true;
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(!checkr(i,j,n,m) && !checkc(i,j,n,m))
                    f = false;
            }
        }
        if(f)
            out<<"Case #"<<c<<": YES"<<endl;
        else
            out<<"Case #"<<c<<": NO"<<endl;

    }
    return 0;
}
