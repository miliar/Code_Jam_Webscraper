#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int t;
    char ch;
    ofstream fout("A-small-attempt2.out");
    ifstream fin("A-small-attempt2.in");
    fin>>t;
    int squ[4][4]; //O:1 X:2 T:3 .:0
    for(int i=1; i<=t; ++i)
    {
        for(int j=0; j<4; ++j)
            for(int k=0; k<4; ++k)
                squ[k][j]=0;
        for(int j=0; j<4; ++j)
            for(int k=0; k<4; ++k)
            {
                fin>>ch;
                if(ch=='O')squ[k][j]=1;
                else if(ch=='X')squ[k][j]=2;
                else if(ch=='T')squ[k][j]=3;
            }
        int chk=0;
        bool tchk=false,end=false;
        for(int k=0; k<4; ++k)
        {
            chk=0;
            tchk=false;
            end=false;
            for(int j=0; j<4; ++j)
            {
                if(squ[j][k]==1)chk++;
                else if(squ[j][k]==2)chk--;
                else if(squ[j][k]==3)tchk=!tchk;
            }
            if(chk==4||(chk==3&&tchk))
            {
                fout<<"Case #"<<i<<": O won"<<endl;
                end=true;
                break;
            }
            else if(chk==-4||(chk==-3&&tchk))
            {
                fout<<"Case #"<<i<<": X won"<<endl;
                end=true;
                break;
            }
        }
        if(end)continue;
        //-----
        for(int k=0; k<4; ++k)
        {
            chk=0;
            tchk=false;
            end=false;
            for(int j=0; j<4; ++j)
            {
                if(squ[k][j]==1)chk++;
                else if(squ[k][j]==2)chk--;
                else if(squ[k][j]==3)tchk=!tchk;
            }
            if(chk==4||(chk==3&&tchk))
            {
                fout<<"Case #"<<i<<": O won"<<endl;
                end=true;
                break;
            }
            else if(chk==-4||(chk==-3&&tchk))
            {
                fout<<"Case #"<<i<<": X won"<<endl;
                end=true;
                break;
            }
        }
        if(end)continue;
        //------
        if((squ[0][0]==squ[1][1]&&squ[0][0]==squ[2][2]&&squ[0][0]==squ[3][3]&&squ[0][0]!=0)||(squ[0][0]!=0&&squ[0][0]==squ[1][1]&&squ[0][0]==squ[2][2]&&squ[3][3]==3)
           ||(squ[0][0]!=0&&squ[0][0]==squ[1][1]&&squ[0][0]==squ[3][3]&&squ[2][2]==3)||(squ[0][0]!=0&&squ[0][0]==squ[2][2]&&squ[0][0]==squ[3][3]&&squ[1][1]==3)
           ||(squ[1][1]!=0&&squ[1][1]==squ[2][2]&&squ[1][1]==squ[3][3]&&squ[0][0]==3))
           {
                if(squ[0][0]==1||squ[1][1])
                fout<<"Case #"<<i<<": O won"<<endl;
                else
                fout<<"Case #"<<i<<": X won"<<endl;
                end=true;
                continue;
           }
           if((squ[0][3]!=0&&squ[0][3]==squ[1][2]&&squ[0][3]==squ[2][1]&&squ[0][3]==squ[3][0])||(squ[0][3]!=0&&squ[0][3]==squ[1][2]&&squ[0][3]==squ[2][1]&&squ[3][0]==3)
           ||(squ[0][3]!=0&&squ[0][3]==squ[1][2]&&squ[0][3]==squ[3][0]&&squ[2][1]==3)||(squ[0][3]!=0&&squ[0][3]==squ[2][1]&&squ[0][3]==squ[3][0]&&squ[1][2]==3)
           ||(squ[1][2]!=0&&squ[1][2]==squ[2][1]&&squ[1][2]==squ[3][0]&&squ[0][3]==3))
           {
                if(squ[0][3]==1||squ[1][2])
                fout<<"Case #"<<i<<": O won"<<endl;
                else
                fout<<"Case #"<<i<<": X won"<<endl;
                end=true;
                continue;
           }
        //-----
        bool chk2=false;
        for(int j=0;j<4;++j)
            for(int k=0;k<4;++k)
                if(squ[k][j]==0)chk2=true;
        if(chk2)fout<<"Case #"<<i<<": Game has not completed"<<endl;
        else fout<<"Case #"<<i<<": Draw"<<endl;
    }
    return 0;
}
