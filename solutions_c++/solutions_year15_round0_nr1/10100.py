#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
    int i,j,tcase,smax[100],temp[100][1000],add[100];
    char ch,si[100][1000];
    scanf("%d",&tcase);
    for(i=0;i<tcase;i++)
    {
        add[i]=0;
        ch=NULL;
        scanf("%d",&smax[i]);
        scanf("%c",&ch);
        for(j=0;j<=smax[i];j++)
        {
            scanf("%c",&si[i][j]);
            temp[i][j]=si[i][j]-'0';
        }
        ch=NULL;
        scanf("%c",&ch);
    }
    /*
    for(i=0;i<tcase;i++)
    {
        for(j=0;j<=smax[i];j++)
        {
            //temp[i][j]=si[i][j]-'0';
            cout<<temp[i][j];
        }
        cout<<'\n';
    }*/
    for(i=0;i<tcase;i++)
    {
        for(j=1;j<=smax[i];j++)
        {
            if(temp[i][j-1]<j)
            {
                temp[i][j-1]+=1;
                add[i]+=1;
            }
            temp[i][j]+=temp[i][j-1];
        }
    }
    for(i=0;i<tcase;i++)
    {
        cout<<"Case #"<<i+1<<": "<<add[i]<<'\n';
    }
    return 0;
}
