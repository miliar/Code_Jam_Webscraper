#include<conio.h>
#include<iostream>
using namespace std;


int main()
{
    int t,x=0;
    cin>>t;
    while(t>0)
    {
        x++;
        int m,n,i,j,k,c,flag=0;
        cin>>m>>n;
        int a[m][n];
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>a[i][j];
            }
        }
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                flag=0;
                c=a[i][j];
                for(k=0;k<n;k++)
                {
                    if(a[i][k]>c)
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==0)
                {
                    continue;
                }
                for(k=0;k<m;k++)
                {
                    if(a[k][j]>c)
                    {
                        flag=2;
                        break;
                    }
                }
                if(flag==2)
                {
                    break;
                }
            }
            if(flag==2)
            {
                break;
            }
        }
        if(flag==2)
        {
           flag=0;
            cout<<"\nCase #"<<x<<": NO";
        }
        else
        {
            flag=0;
            cout<<"\nCase #"<<x<<": YES";
        }
        t--;
    }
}
