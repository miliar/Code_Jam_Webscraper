#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#define N 110


using namespace std;

int a[N][N],x[N],y[N];

int main(int argc, char *argv[])
{
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "w+t", stdout);
    
    int i,j,k;
    int t;
    int m,n;
    int z;
    
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n>>m;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                cin>>a[i][j];
            }
        }
        cout<<"Case #"<<k<<": ";
        if(n==1||m==1)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            memset(x,0,sizeof(x));
            memset(y,0,sizeof(y));
            for(i=0;i<n;i++)
            {
                for(j=0;j<m;j++)
                {
                    x[i]=max(a[i][j],x[i]);
                    y[j]=max(a[i][j],y[j]);
                }
            }
            for(i=0;i<n;i++)
            {
                for(j=0;j<m;j++)
                {
                    if(a[i][j]<x[i]&&a[i][j]<y[j])
                        break;
                }
                if(j<m)
                    break;
            }
            if(i<n)
            {
                cout<<"NO"<<endl;
            }
            else
            {
                cout<<"YES"<<endl;
            }
        }
        
    }
    
   // system("PAUSE");
    return EXIT_SUCCESS;
}
