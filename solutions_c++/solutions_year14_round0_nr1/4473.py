#include <iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main()
{
    freopen("E:\\in.c","r",stdin);
    freopen("E:\\out","w",stdout);
    int i,j,t,x,y;
    int mark[30];
    int a[5][4];
    int b[4][4];
    int T;
    cin>>T;
    for(t=1;t<=T;++t)
    {
        cin>>x;
        x--;
        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
            cin>>a[i][j];
        cin>>y;
        y--;
        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
            cin>>b[i][j];
        for(i=1;i<=16;++i)
            mark[i]=0;
        for(i=0;i<4;++i)
            mark[a[x][i]]++;
        for(i=0;i<4;++i)
            mark[b[y][i]]++;
        int num=0;
        int in;
        for(i=1;i<=16;++i)
            if(mark[i]>1)
            {
                num++;
                in=i;
            }
        if(num>1)
            cout<<"Case #"<<t<<": Bad magician!\n";
        else
            if(num==0)
            cout<<"Case #"<<t<<": Volunteer cheated!\n";
            else
               cout<<"Case #"<<t<<": "<<in<<"\n";
    }
    return 0;
}
