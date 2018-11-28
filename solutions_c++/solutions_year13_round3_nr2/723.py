#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

#define N 1000

using namespace std;

char a[N];

int main(int argc, char *argv[])
{
    int i,j,k;
    long long int x,y;
    int t;
    
    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("B-small-attempt0.out", "w+t", stdout);
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>x>>y;
        if(x>=0)
        {
            for(j=0,k=0;j<x;j++)
            {
                a[k]='W';
                k++;
                a[k]='E';
                k++;
            }
        }
        else
        {
            for(j=0,k=0;j<x*-1;j++)
            {
                a[k]='E';
                k++;
                a[k]='W';
                k++;
            }
        }
        if(y>=0)
        {
            for(j=0;j<y;j++)
            {
                a[k]='S';
                k++;
                a[k]='N';
                k++;
            }
        }
        else
        {
            for(j=0;j<y*-1;j++)
            {
                a[k]='N';
                k++;
                a[k]='S';
                k++;
            }
        }
        cout<<"Case #"<<i<<": ";
        for(j=0;j<k;j++)
        {
            cout<<a[j];
        }
        cout<<endl;
    }
    
    
    
  //  system("PAUSE");
    return EXIT_SUCCESS;
}
