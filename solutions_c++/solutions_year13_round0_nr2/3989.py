#include <stdio.h>
#include <iostream>
#include <vector>
#define size 100
using namespace std;
int check(int a[size][size],int i,int j,int n,int m)
{
    int max2=a[i][j],k;
    int max1=a[i][j];
    for(k=0;k<m;k++)
    {
        if(max1<a[i][k])
        max1=a[i][k];
    }
     for(k=0;k<n;k++)
    {
        if(max2<a[k][j])
        max2=a[k][j];
    }
        if(max1==a[i][j]||max2==a[i][j])
        return 1;
        else return 0;
}      
    
    
int main()
{
    int t,num=0;
    cin>>t;
    while(t--)
    {
        num++;
        int n,m,a[size][size],flag=1,i,j;
        cin>>n>>m;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            cin>>a[i][j];
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
               int c=check(a,i,j,n,m);
               if(c==0)
               flag=0;
            }
        }
        if(flag==0)
        cout<<"Case #"<<num<<": NO"<<endl;
        else cout<<"Case #"<<num<<": YES"<<endl;
    }
    return 0;
}        
                    
