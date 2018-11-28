#include <iostream>
using namespace std;
int main()
{
    string s[5];
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        for(int j=0;j<4;j++)
            cin>>s[j];
        int posj,posk;
        bool flag=true;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                if(s[j][k]=='T')
                {
                    posj=j;
                    posk=k;
                }
                else if(s[j][k]=='.')
                    flag=false;
        bool won=false;
        for(int j=0;j<4;j++)
        {
            if(s[j]=="XXXX")
            {
                cout<<"Case #"<<(i+1)<<": X won"<<endl;
                won=true;
                break;
            }
            if(s[j]=="OOOO")
            {
                cout<<"Case #"<<(i+1)<<": O won"<<endl;
                won=true;
                break;    
            }
            if(s[0][j]=='X'&&s[1][j]=='X'&&s[2][j]=='X'&&s[3][j]=='X')
            {
                cout<<"Case #"<<(i+1)<<": X won"<<endl;
                won=true;
                break;
            }
            if(s[0][j]=='O'&&s[1][j]=='O'&&s[2][j]=='O'&&s[3][j]=='O')
            {
                cout<<"Case #"<<(i+1)<<": O won"<<endl;
                won=true;
                break;    
            }
        }
        if(!won&&((s[0][0]=='X'&&s[1][1]=='X'&&s[2][2]=='X'&&s[3][3]=='X')||(s[0][3]=='X'&&s[1][2]=='X'&&s[2][1]=='X'&&s[3][0]=='X')))
        {
            cout<<"Case #"<<(i+1)<<": X won"<<endl;
            won=true;
        }
        if(!won&&((s[0][0]=='O'&&s[1][1]=='O'&&s[2][2]=='O'&&s[3][3]=='O')||(s[0][3]=='O'&&s[1][2]=='O'&&s[2][1]=='O'&&s[3][0]=='O')))
        {
            cout<<"Case #"<<(i+1)<<": O won"<<endl;
            won=true;
        }
        if(!won)
        {
            if(posj==0)
            {
                if(posk==0)
                {
                    if(s[0]=="TXXX")
                    {
                        cout<<"Case #"<<(i+1)<<": X won"<<endl;
                        won=true;
                    }
                    else if(s[0]=="TOOO")
                    {
                        cout<<"Case #"<<(i+1)<<": O won"<<endl;
                        won=true;
                    }
                    else if((s[1][0]=='X'&&s[2][0]=='X'&&s[3][0]=='X')||(s[1][1]=='X'&&s[2][2]=='X'&&s[3][3]=='X'))
                    {
                        cout<<"Case #"<<(i+1)<<": X won"<<endl;
                        won=true;
                    }
                    else if((s[1][0]=='O'&&s[2][0]=='O'&&s[3][0]=='O')||(s[1][1]=='O'&&s[2][2]=='O'&&s[3][3]=='O'))
                    {
                        cout<<"Case #"<<(i+1)<<": O won"<<endl;
                        won=true;
                    }
                }
                else if(posk==3)
                {
                    if(s[0]=="XXXT")
                    {
                        cout<<"Case #"<<(i+1)<<": X won"<<endl;
                        won=true;
                    }
                    else if(s[0]=="OOOT")
                    {
                        cout<<"Case #"<<(i+1)<<": O won"<<endl;
                        won=true;
                    }
                    else if((s[1][3]=='X'&&s[2][3]=='X'&&s[3][3]=='X')||(s[1][2]=='X'&&s[2][1]=='X'&&s[3][0]=='X'))
                    {
                        cout<<"Case #"<<(i+1)<<": X won"<<endl;
                        won=true;
                    }
                    else if((s[1][3]=='O'&&s[2][3]=='O'&&s[3][3]=='O')||(s[1][2]=='O'&&s[2][1]=='O'&&s[3][0]=='O'))
                    {
                        cout<<"Case #"<<(i+1)<<": O won"<<endl;
                        won=true;
                    }
                }
                else
                {
                    if(s[1][posk]=='X'&&s[2][posk]=='X'&&s[3][posk]=='X')
                    {
                        cout<<"Case #"<<(i+1)<<": X won"<<endl;
                        won=true;
                    }
                    else if(s[1][posk]=='O'&&s[2][posk]=='O'&&s[3][posk]=='O')
                    {
                        cout<<"Case #"<<(i+1)<<": O won"<<endl;
                        won=true;
                    }
                }
            }
            else if(posj==3)
            {
                if(posk==0)
                {
                    if(s[3]=="TXXX")
                    {
                        cout<<"Case #"<<(i+1)<<": X won"<<endl;
                        won=true;
                    }
                    else if(s[3]=="TOOO")
                    {
                        cout<<"Case #"<<(i+1)<<": O won"<<endl;
                        won=true;
                    }
                    else if((s[1][0]=='X'&&s[2][0]=='X'&&s[0][0]=='X')||(s[0][3]=='X'&&s[1][2]=='X'&&s[2][1]=='X'))
                    {
                        cout<<"Case #"<<(i+1)<<": X won"<<endl;
                        won=true;
                    }
                    else if((s[1][0]=='O'&&s[2][0]=='O'&&s[0][0]=='O')||(s[0][3]=='O'&&s[1][2]=='O'&&s[2][1]=='O'))
                    {
                        cout<<"Case #"<<(i+1)<<": O won"<<endl;
                        won=true;
                    }
                }
                if(posk==3)
                {
                    if(s[0]=="XXXT")
                    {
                        cout<<"Case #"<<(i+1)<<": X won"<<endl;
                        won=true;
                    }
                    else if(s[0]=="OOOT")
                    {
                        cout<<"Case #"<<(i+1)<<": O won"<<endl;
                        won=true;
                    }
                    else if((s[1][3]=='X'&&s[2][3]=='X'&&s[0][3]=='X')||(s[1][1]=='X'&&s[2][2]=='X'&&s[0][0]=='X'))
                    {
                        cout<<"Case #"<<(i+1)<<": X won"<<endl;
                        won=true;
                    }
                    else if((s[1][3]=='O'&&s[2][3]=='O'&&s[0][3]=='O')||(s[2][2]=='O'&&s[1][1]=='O'&&s[0][0]=='O'))
                    {
                        cout<<"Case #"<<(i+1)<<": O won"<<endl;
                        won=true;
                    }
                }
            }
            else
            {
                if(s[posj]=="TXXX"||s[posj]=="XXXT")
                {
                    cout<<"Case #"<<(i+1)<<": X won"<<endl;
                    won=true;
                }
                else if(s[posj]=="TOOO"||s[posj]=="OOOT")
                {
                    cout<<"Case #"<<(i+1)<<": O won"<<endl;
                    won=true;
                }
            }
        }
        if(!won&&flag)
            cout<<"Case #"<<(i+1)<<": Draw"<<endl;
        if(!won&&!flag)
            cout<<"Case #"<<(i+1)<<": Game has not completed"<<endl;
    }
    return 0;
}