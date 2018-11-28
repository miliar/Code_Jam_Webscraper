#include <iostream>
 using namespace std;
 
 int main ()
 {
    unsigned int T, n, m, lawn[101][101], large, maxrow[100], maxcol[100];
    cin>>T;
    for (int i=0;i<T;i++)
    {
        cin>>n>>m;
        for (int j=0;j<n;j++)
        {
            large=0;
            for (int k=0;k<m;k++)
            {    
                cin>>lawn[j][k];
                if (lawn[j][k]>large)
                    large=lawn[j][k];
            }
            maxrow[j]=large;
        }
        for (int k=0;k<m;k++)
        {
            large=0;
            for (int j=0;j<n;j++)
            {    
                if (lawn[j][k]>large)
                    large=lawn[j][k];
            }
            maxcol[k]=large;
        }
        int flag=1;
        for (int j=0;j<n&&flag;j++)
        {
            for (int k=0;k<m;k++)
            {    
                if (lawn[j][k] != maxrow[j] && lawn[j][k] != maxcol[k])
                {
                    flag=0;
                    break;
                }
            }
            
        }
        if (flag)
            cout<<"Case #"<<i+1<<": YES\n";
        else
            cout<<"Case #"<<i+1<<": NO\n";
    }
    return 0;
 }
