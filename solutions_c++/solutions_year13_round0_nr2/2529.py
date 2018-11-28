#include<stdio.h>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int cal(int a[][105],int i,int j,int n,int m)
{
    int l,cns=0;
    for(l=0;l<n;l++)
    {
        if(a[l][j]>a[i][j])
        {
            cns=1;
            break;
        }
    }
    if(cns==1)
   {
       for(l=0;l<m;l++)
        {
            if(a[i][l]>a[i][j])
            return 1;
        }
   }
    return 0;
}
int main()
{
    int t,k=1,z;
    cin>>t;
    while(k<=t)
    {
        int n,m,i,j,ar[105][105],c=0;
       cin>>n>>m;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
            cin>>ar[i][j];
            }
        }
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if(cal(ar,i,j,n,m)==1){
                    c=1;
                    break;
                    }
                }
            if(c==1)
            break;
            }
        if(c!=1)
        cout<<"Case #"<<k<<": "<<"YES"<<endl;
        else
         cout<<"Case #"<<k<<": "<<"NO"<<endl;
        k++;
    }
    return 0;
}
