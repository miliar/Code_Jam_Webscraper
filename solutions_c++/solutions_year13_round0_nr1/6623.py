#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
char m[4][80];
char winner[1000];
int noc;
int main()
{
    cin>>noc;
    for(int i=0;i<noc;i++)
        winner[i]='n';
    for(int u=0;u<noc;u++)
        {
            int finished=1;
            for(int i=0;i<4;i++)
            {
                cin>>m[i];
                if(finished==1)
                    for(int j=0;j<4;j++)
                    {
                        if(m[i][j]=='.')
                            finished=0;
                    }
            }
            winner[u]='n';
            if(finished==0)
                winner[u]='.';
            for(int i=0;i<4;i++)
            {
                int flag=0;
                char first_el=m[i][0];
                if(first_el=='T')
                {
                    first_el=m[i][1];
                }
                for(int j=0;j<4;j++)
                {
                    if(first_el=='.')
                    {
                        flag=1;
                        break;
                    }
                    if(m[i][j]!='T' && m[i][j] != first_el)
                        {
                            flag=1;
                            break;
                        }
                }
                if(flag==0)
                {
                    winner[u]=first_el;
                    break;
                }
                flag=0;
                first_el=m[0][i];
                if(first_el=='T')
                {
                    first_el=m[1][i];
                }
                for(int j=0;j<4;j++)
                {
                    if(first_el=='.')
                    {
                        flag=1;
                        break;
                    }

                    if(m[j][i]!='T' && m[j][i] != first_el)
                        {
                            flag=1;
                            break;
                        }
                }
                if(flag==0)
                {
                    winner[u]=first_el;
                    //cout<<"\nwinner["<<u<<"]"<<winner[u];
                    break;
                }
            }
            if(winner[u]=='.'|winner[u]=='n')
            {
                int dflag=0,diflag=0;
                char dfirst_el=m[0][0];
                if(dfirst_el=='T')
                {
                    dfirst_el=m[1][1];
                }
                char difirst_el=m[0][3];
                if(difirst_el=='T')
                {
                    difirst_el=m[1][2];
                }
                if(dfirst_el=='.')
                    dflag=1;
                if(difirst_el=='.')
                    diflag=1;
                for(int i=0;i<4;i++)
                {
                    if(dflag==0)
                        if(m[i][i]!='T' && m[i][i]!=dfirst_el)
                            dflag=1;
                    if(diflag==0)
                        if(m[i][4-1-i]!='T' && m[i][4-1-i]!=difirst_el)
                            diflag=1;
                    if(diflag==1 && dflag==1)
                        break;
                }
                if(diflag==0)
                {
                    winner[u]=difirst_el;


                }
                if(dflag==0)
                {
                    winner[u]=dfirst_el;

                }
            }
        }
    ofstream op;
    op.open ("1.txt");
    for(int i=0;i<noc;i++)
    {
        op<<"\nCase #"<<i+1<<": ";
        switch(winner[i])
        {
            case 'n':
                op<<"Draw";
                break;
            case '.':
                op<<"Game has not completed";
                break;
            case 'X':
                op<<"X won";
                break;
            case 'O':
                op<<"O won";
                break;
            default:
                op<<"ERROR";
        }
    }
    int a;
    cin>>a;
}
