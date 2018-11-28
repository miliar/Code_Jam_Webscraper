#include <iostream>
#include<stdio.h>

using namespace std;

#define gi(n) scanf("%d",&n)

int main()
{
    freopen("D-small-attempt4.in","r",stdin);
    freopen("output_small.txt", "w", stdout);
    int cases,i=1,X,R,C;
    int win=0;
    gi(cases);
    while(cases--)
    {
        gi(X);
        gi(R);
        gi(C);
        switch(X)
        {
        case 1:
            win=1;
            break;
        case 2:
            if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
                win=0;
            else
                win=1;
            break;
        case 3:
            if(R==1||C==1)
                win=0;
            else if(R==3||C==3)
                win=1;
            else
                win=0;
            break;
        case 4:
            if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
                win=1;
            else
                win=0;
        }
        if(win==1)
            cout<<"Case #"<<i++<<": "<<"GABRIEL"<<endl;
        else
            cout<<"Case #"<<i++<<": "<<"RICHARD"<<endl;
    }
    return 0;
}

