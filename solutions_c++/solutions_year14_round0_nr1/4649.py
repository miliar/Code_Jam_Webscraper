#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int t,row,x,y;
    cin >>t;
    for(x=1;x<=t;x++)
    {
        int grid1[4][4],grid2[4][4],card[17]={0},k=0;
        cin >>row;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin >>grid1[i][j];
        for(int l=0;l<4;l++)
            card[grid1[row-1][l]]++;
        cin >>row;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin >>grid2[i][j];
        for(int l=0;l<4;l++)
            card[grid2[row-1][l]]++;
        for(int l=1;l<17;l++)
            if(card[l]==2)
            {
                k++;
                y=l;
            }
        if(k==0)
            cout <<"Case #"<<x<<": Volunteer cheated!"<<endl;
        else if(k==1)
            cout <<"Case #"<<x<<": "<<y<<endl;
        else
            cout <<"Case #"<<x<<": Bad magician!"<<endl;
    }
    return 0;
}
