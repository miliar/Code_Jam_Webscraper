#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <deque>
#include <cmath>
#include <map>
#define mod 1000000007LL
using namespace std;

int a[111][111];
int b[111][111];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int re,i,j,m,n,x,cases=1;
    cin>>re;
    while(re--)
    {
        cin>>m>>n;
        for(i=0;i<m;i++)
        for(j=0;j<n;j++)
        {
          cin>>a[i][j];
          b[i][j]=100;
        }
        
        for(i=0;i<m;i++)
        {
            x=0;
            for(j=0;j<n;j++)
                x=max(x,a[i][j]);
            for(j=0;j<n;j++)
                b[i][j]=x;
        }
        
        for(j=0;j<n;j++)
        {
            x=101;
            for(i=0;i<m;i++)
            {
                if(a[i][j]==b[i][j])
                continue;
                x=min(x,a[i][j]);
            }
            if(x!=101)
            {
                for(i=0;i<m;i++)
                    b[i][j]=x;
            }
        }
        
        bool ff=true;
        for(i=0;i<m;i++)
        for(j=0;j<n;j++)
        if(a[i][j]!=b[i][j])
        ff=false;
        
        printf("Case #%d: ",cases++);
        if(ff)
        cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
        
        
        
        
    }
}
