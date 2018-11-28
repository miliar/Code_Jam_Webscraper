#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int x=1;
    while(t--)
    {
        string ch[4];
        int flag=0;
        int cx=0,co=0;
        for(int i=0;i<4;i++)
        {
            cin>>ch[i];
            cx=0;
            co=0;
            for(int j=0;j<4;j++)
            {
                if(ch[i][j]=='X')
                cx++;
                else if(ch[i][j]=='O')
                co++;
                else if(ch[i][j]=='T')
                {
                    cx++;
                    co++;
                }
                if(cx==4)
                flag=1;
                else if(co==4)
                flag=2;
            }
        }
        if(flag==0)
        {
            cx=0;
            co=0;
            for(int i=0;i<4;i++)
            {
                cx=0;
                co=0;
                for(int j=0;j<4;j++)
                {
                    if(ch[j][i]=='X')
                    cx++;
                    else if(ch[j][i]=='O')
                    co++;
                    else if(ch[j][i]=='T')
                    {
                        cx++;
                        co++;
                    }
                }
                if(cx==4)
                flag=1;
                else if(co==4)
                flag=2;
            }
        }
        if(flag==0)
        {
            cx=0;
            co=0;
            for(int i=0;i<4;i++)
            {
                if(ch[i][i]=='X')
                cx++;
                else if(ch[i][i]=='O')
                co++;
                else if(ch[i][i]=='T')
                {
                    cx++;
                    co++;
                }
            }
            //cout<<endl<<cx<<" "<<co<<endl;
            if(cx==4)
            flag=1;
            else if(co==4)
            flag=2;
        }
        if(flag==0)
        {
            cx=0;
            co=0;
            for(int i=0;i<4;i++)
            {
                if(ch[i][3-i]=='X')
                cx++;
                else if(ch[i][3-i]=='O')
                co++;
                else if(ch[i][3-i]=='T')
                {
                    cx++;
                    co++;
                }
            }
            //cout<<endl<<cx<<" "<<co<<endl;
            if(cx==4)
            flag=1;
            else if(co==4)
            flag=2;
        }
        if(flag==0)
        {
            for(int i=0;i<4;i++)
            {
                if(flag==3)
                break;
                for(int j=0;j<4;j++)
                if(ch[i][j]=='.')
                {
                    flag=3;
                    break;
                }
            }
        }
        if(flag==0)
        flag=4;
        cout<<"Case #"<<x++<<": ";
        switch(flag)
        {
            case 1: cout<<"X won\n";
                    break;
            case 2: cout<<"O won\n";
                    break;
            case 3: cout<<"Game has not completed\n";
                    break;
            case 4: cout<<"Draw\n";
                    break;
        }
    }
    return 0;
}
