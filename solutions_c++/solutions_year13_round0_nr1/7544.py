#include<iostream>
#include<cstring>
#include <iomanip>
#include <fstream>
using namespace std;
int main()
{
    char shuzu[4][4];
    freopen("A-large.in", "r", stdin);
    freopen("outputlarge.txt", "w", stdout);

    int t;

    cin>>t;

    int k=0;
    while(t--)
    {
            int xresult=0;
            int oresult=0;
            int result=0;

        k++;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>shuzu[i][j];
            }
        }

        int flag1=1;
        for(int i=0;i<4;i++)
        {
            xresult=0;
            oresult=0;
            if(flag1==1)
            {
            for(int j=0;j<4;j++)
            {
                if(shuzu[i][j]=='X'||shuzu[i][j]=='T')
                {
                    xresult++;
                }
                if(shuzu[i][j]=='O'||shuzu[i][j]=='T')
                {
                    oresult++;
                }
            }
            if(xresult==4) {result=1;flag1=0;}
            if(oresult==4) {result=2;flag1=0;}
            }
        }

        if(result==0)
        {
            xresult=0;
            oresult=0;
            int flag2=1;
            for(int j=0;j<4;j++)
        {
            xresult=0;
            oresult=0;
            if(flag2==1)
            {

            for(int i=0;i<4;i++)
            {
                if(shuzu[i][j]=='X'||shuzu[i][j]=='T')
                {
                    xresult++;
                }
                if(shuzu[i][j]=='O'||shuzu[i][j]=='T')
                {
                    oresult++;
                }
            }
            if(xresult==4) {result=1;flag2=0;}
            if(oresult==4) {result=2;flag2=0;}
            }
        }
        }

        if(result==0)
        {
            xresult=0;
            oresult=0;
            for(int i=0;i<4;i++)
            {
                if(shuzu[i][i]=='X'||shuzu[i][i]=='T')
                {
                    xresult++;
                }
                if(shuzu[i][i]=='O'||shuzu[i][i]=='T')
                {
                    oresult++;
                }
            }
             if(xresult==4) {result=1;}
            if(oresult==4) {result=2;}

        }

        if(result==0)
        {
            xresult=0;
            oresult=0;
            for(int i=0;i<4;i++)
            {
                if(shuzu[i][3-i]=='X'||shuzu[i][3-i]=='T')
                {
                    xresult++;
                }
                if(shuzu[i][3-i]=='O'||shuzu[i][3-i]=='T')
                {
                    oresult++;
                }

            }
            if(xresult==4) {result=1;}
                if(oresult==4) {result=2;}
        }
        if(result==0)
        {
            int flag3=0;
            for(int i=0;i<4;i++)
            {
                for(int j=0;j<4;j++)
                {
                    if(shuzu[i][j]=='.') flag3=1;
                }
            }
            if(flag3==0) result=3;
            else result=4;
        }

        switch(result)
        {

            case 1: cout<<"Case #"<<k<<": "<<"X won"<<endl;
            break;
            case 2: cout<<"Case #"<<k<<": "<<"O won"<<endl;
            break;
            case 3: cout<<"Case #"<<k<<": "<<"Draw"<<endl;
            break;
            case 4: cout<<"Case #"<<k<<": "<<"Game has not completed"<<endl;
            break;
        }
    }
}
