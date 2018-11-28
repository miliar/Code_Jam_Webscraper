#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int n,m,test,i,ct=0,j,k,arr[101][101],failed=0,won;
    cin>>test;
    while(test--)
    {
        won=1;
        cin>>n>>m;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&arr[i][j]);
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                failed=0;
                for(k=0;k<m;k++)
                {
                    if(arr[i][k]>arr[i][j])
                    {
                        failed=1;
                        break;
                    }
                }
                if(failed==1)
                for(k=0;k<n;k++)
                {
                    if(arr[k][j]>arr[i][j])
                    {
                        failed=1;
                        break;
                    }
                }
                if(k==n)
                    failed=0;
                if(failed==1)
                {
                    won=0;
                    i=n+1;
                    break;
                }
            }
        }
        ct++;
        if(won==1)
            cout<<"Case #"<<ct<<": YES";
        else cout<<"Case #"<<ct<<": NO";
        cout<<"\n";
    }
}
