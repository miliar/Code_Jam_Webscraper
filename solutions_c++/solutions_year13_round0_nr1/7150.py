#include<iostream>
#include<fstream>
using namespace std;
int main()
{
char ch;
int T,m,n,i,t,reset=0,unc=1,sc=0,sl=0,sd=0,result=2,j,q[100][100];
ifstream in("a.txt");
ofstream out("b.txt");
in>>T;
for(t=1;t<=T;t++)
{result=2;
sc=0;
sd=0;
sl=0;
unc=0;
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            in>>ch;
            if (ch=='X') q[i][j]=1;
            if (ch=='O') q[i][j]=0;
            if (ch=='T') q[i][j]=50;
            if (ch=='.')
            {
                unc=1;
                q[i][j]=100;
            }
        }
    }

    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
    {
        sl=sl+q[i][j];
        sc=sc+q[j][i];
        reset++;
        if (reset==4)
        {
            reset=0;
            if(sc==4||sc==53||sl==4||sl==53)
            {
                cout<<t<<" "<<sc<<" ";
                i=5;
                j=5;
                result=1;
            }
            if(sc==0||sc==50||sl==0||sl==50)
            {

                i=5;
                j=5;
                result=0;
            }
            sc=0;
            sl=0;
        }
    }
    }
    for(i=1;i<=4;i++)
    {
        sd=sd+q[i][i];
    }
        if(sd==0||sd==50)
        {
            result=0;
            //cout<<sd;
        }
        if(sd==4||sd==53)
        {
            result=1;
        }

    sd=0;
    i=0;
    //cout<<result;
        for(j=4;j>=1;j--)
        {
        i++;
        sd=sd+q[j][i];
        }
        if(sd==0||sd==50)
        {
            result=0;
            //cout<<sd;
        }
        if(sd==4||sd==53)
        {
            //cout<<sd;
            result=1;
        }


    if (result==2&&unc==1) result=9;
    if (result==2&&unc==0) result=10;
    if (result==1) out<<"Case #"<<t<<": "<<"X won\n";
    if (result==0) out<<"Case #"<<t<<": "<<"O won\n";
    if (result==9) out<<"Case #"<<t<<": "<<"Game has not completed\n";
    if (result==10) out<<"Case #"<<t<<": "<<"Draw\n";

}
}
