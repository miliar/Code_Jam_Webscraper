#include <iostream>
#include <algorithm>
using namespace std;
string s[10];
int t[10][10], a[111],wyn,czyt,ti,tj,k;
int pyk()
{
    for(int i=0;i<4;i++)
    {
        a[i]=t[i][0]+t[i][1]+t[i][2]+t[i][3];
        a[i+4]=t[0][i]+t[1][i]+t[2][i]+t[3][i];
    }
    a[8]=t[0][0]+t[1][1]+t[2][2]+t[3][3];
    a[9]=t[3][0]+t[2][1]+t[1][2]+t[0][3];

    for(int i=0;i<10;i++)
    {
        if(a[i]==4)
        {
            return 1;
        }
        if(a[i]==0)
        {
            return 0;
        }
    }
    return -1;

}
void funk(int iii)
{
    cin >>s[0]>>s[1]>>s[2]>>s[3];

        cout << "Case #" << iii << ": ";

    wyn=0;
    czyt=0;
    ti=-1;
    tj=1;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(s[i][j]=='O')
            {
                t[i][j]=0;
            }
            if(s[i][j]=='X')
            {
                t[i][j]=1;
            }
            if(s[i][j]=='.')
            {
                t[i][j]=-100;
                wyn++;
            }
            if(s[i][j]=='T')
            {
                t[i][j]=0;
                czyt=1;
                ti=i;
                tj=j;
            }
        }
    }
    k=pyk();
     if(k==1)
        {
            cout << "X won\n"; return;
        }
        if(k==0)
        {
            cout << "O won\n"; return;
        }
        if(ti*tj>=0){
    t[ti][tj]=1;
    k=pyk();
     if(k==1)
        {
            cout << "X won\n"; return;
        }
        if(k==0)
        {
            cout << "O won\n"; return;
        }
        }

    if(wyn>0)
    {
        cout << "Game has not completed\n";
        return;
    }

    cout << "Draw\n"; return;
}
int main()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        funk(i+1);
    }
    return 0;
}
