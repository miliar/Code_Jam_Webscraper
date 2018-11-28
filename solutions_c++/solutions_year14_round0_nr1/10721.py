#include<iostream>
using namespace std;
#include<stdio.h>
#include<stdlib.h>
int main()
{
    //freopen("A-small-attempt3.in","r",stdin);
    //freopen("Output.txt","w",stdout);
    int t;
    int x,y,i,k,q,j,c,a[4][4],b[4][4];
    cin>>t;
    q=0;
    while(t--)
    {
        cin>>x;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                cin>>a[i][j];
        }
        cin>>y;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                cin>>b[i][j];
        }
        c=0;

        /*for(i=0;i<4;i++)
        {
         cout<<a[x-1][i]<<"   "<<b[y-1][i]<<endl;
        }*/
        for(i=0;i<4;i++)
        {
                if(a[x-1][i]==b[y-1][0])
               {
                   c++;k=i;
               }
               else if(a[x-1][i]==b[y-1][1])
               {
                   c++;k=i;
               }
               else if(a[x-1][i]==b[y-1][2])
               {
                   c++;k=i;
               }
               else if(a[x-1][i]==b[y-1][3])
               {
                   c++;k=i;
               }
        }

        if(c==0)
        {
            cout<<"Case #"<<++q<<": "<<"Volunteer cheated!"<<endl;
        }
        else if(c==1)
        {
            cout<<"Case #"<<++q<<": "<<a[x-1][k]<<endl;
        }
        else
        {
            cout<<"Case #"<<++q<<": "<<"Bad magician!"<<endl;
        }
    }
}
