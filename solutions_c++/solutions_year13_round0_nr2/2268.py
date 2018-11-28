#include<iostream>
#include<cstdio>
#define s(n) scanf("%d",&n)
#define ULL unsigned long long
#include<cstring>
using namespace std;
int main()
{
    int t,c=0;
    s(t);
    while(t--)
    {
        c++;
        int n,m;
        s(n);s(m);
        int arr[n][m];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                s(arr[i][j]);
            }
        }//cout<<"aman";
        int row[n];
        int col[m];
        for(int i=0;i<n;i++)
        {
            int m2=arr[i][0];
            for(int j=1;j<m;j++)
            {
                if(arr[i][j]>m2)m2=arr[i][j];
            }
            row[i]=m2;
        }
        //cout<<"aman";
        for(int j=0;j<m;j++)
        {
            int m2=arr[0][j];
            for(int i=0;i<n;i++)
            {
                if(arr[i][j]>m2)m2=arr[i][j];
            }
            col[j]=m2;
        }
        int match[n][m];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                match[i][j]=min(row[i],col[j]);
            }
        }
        //cout<<"aman";
        int flag=1;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(arr[i][j]<match[i][j]){flag=0;break;}
            }
        }
        //cout<<"aman";
        if(flag)printf("Case #%d: YES\n",c);
        else
        printf("Case #%d: NO\n",c);
    }
}
        
