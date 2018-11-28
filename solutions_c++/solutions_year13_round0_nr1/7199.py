#include <iostream>
#include <algorithm>
#include <stdlib.h>
using namespace std;
int main()
{
    int n,i,j,k,w;
    cin>>n;
    int a[n];
    //int h[4][4];
    string s;
    for(i=0;i<n;i++)
    {
       int h[4][4]= {{0,0,0,0}, {0,0,0,0}, {0,0,0,0}, {0,0,0,0}};
       int d[2][4]={{0,0,0,0},{0,0,0,0}};
        w=0;
        for(j=0;j<4;j++)
        {
            cin>>s;
            if(w==0){
                //horizontal
            if(s=="XXXX" || s=="XXXT" || s=="XXTX" || s=="XTXX" || s=="TXXX")
            {a[i]=1; w=1;}
            else if(s=="OOOO" || s=="OOOT" || s=="OOTO" || s=="OTOO" || s=="TOOO")
            {a[i]=2;w=1;}
            //vertical
            for(k=0;k<4;k++)
            {
                if(s[k]=='O')
                h[k][0]++;
                else if(s[k]=='X')
                h[k][1]++;
                else if(s[k]=='T')
                h[k][2]++;
                else if(s[k]=='.')
                h[k][3]++;

                if(h[k][0]==4 || (h[k][0]==3 && h[k][2]==1))
                {
                a[i]=2;w=1;
                }
                if(h[k][1]==4 || (h[k][1]==3 && h[k][2]==1))
                {
                a[i]=1;w=1;
                }

            }
            //diagonal 1
            if(s[j]=='O')
            d[0][0]++;
            else if(s[j]=='X')
            d[0][1]++;
            else if(s[j]=='T')
            d[0][2]++;
            else if(s[j]=='.')
            d[0][3]++;

            if(d[0][0]==4 || (d[0][0]==3 && d[0][2]==1))
            {
                a[i]=2;w=1;
            }
            if(d[0][1]==4 || (d[0][1]==3 && d[0][2]==1))
            {
                a[i]=1;w=1;
            }

            //diagonal2
            if(s[abs(3-j)]=='O')
            d[1][0]++;
            else if(s[abs(3-j)]=='X')
            d[1][1]++;
            else if(s[abs(3-j)]=='T')
            d[1][2]++;
            else if(s[abs(3-j)]=='.')
            d[1][3]++;

            if(d[1][0]==4 || (d[1][0]==3 && d[1][2]==1))
            {
                a[i]=2;w=1;
            }
            if(d[1][1]==4 || (d[1][1]==3 && d[1][2]==1))
            {
                a[i]=1;w=1;
            }
            }

        }
	//incomplete or draw
        if(w==0)
        {
            if(h[0][3]==0 && h[1][3]==0 && h[2][3]==0 && h[3][3]==0)
            a[i]=3;
            else
            a[i]=4;
        }

    }
    for(i=0;i<n;i++)
    {
        if(a[i]==1)
        cout<<"Case #"<<i+1<<": X won"<<endl;
        else if(a[i]==2)
        cout<<"Case #"<<i+1<<": O won"<<endl;
        else if(a[i]==3)
        cout<<"Case #"<<i+1<<": Draw"<<endl;
        else if(a[i]==4)
        cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
    }
}
