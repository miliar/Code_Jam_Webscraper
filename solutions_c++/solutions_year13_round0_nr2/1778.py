#include<iostream>
#include<ostream>
#include<stdlib.h>
#include<stdio.h>
#include<fstream>
#include<iomanip>
#include<map>
#include<math.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
    
    freopen("input.txt","r",stdin);
    freopen("output.in","w",stdout);
    int t,a[10][10],i,j,x,y,index=1;
    cin>>t;
    while(index<=t)
    {
        int r[10],c[10],f=0;
        cin>>x>>y;
        for(i=0;i<x;i++)
        {  r[i]=0;
            for(j=0;j<y;j++)
            { cin>>a[i][j];
                r[i]+=a[i][j];
            }
        }
        for(i=0;i<y;i++)
        {  c[i]=0;
            for(j=0;j<x;j++)
            {
                c[i]+=a[j][i];
            }
        }
        
        for(i=0;i<x;i++)
        {
            for(j=0;j<y;j++)
            {
              if(a[i][j]==1)
              {
                  if(c[j]!=x&&r[i]!=y)
                  {  f=1;break;}
                  
              }
            }
            if(f==1)
                break;
        }
        cout<<"Case #"<<index<<": ";
        if(f==1)
            cout<<"NO"<<"\n";
        else
            cout<<"YES\n";
        index++;
    }
    
    return 0;
}