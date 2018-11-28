#include<iostream>
#include<cstdio>
#define max 1000
#include<fstream>
using namespace std;
char m[4][80];
char winner[max];
int cases;
int main()
{
    cin>>cases;
    for(int i=0;i<cases;i++)
        winner[i]='n';
    for(int u=0;u<cases;u++)
        {
            //cout<<"\n-----input-------\n";
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
                int flag=0;     //flag=0 means that no winner found
                char fe=m[i][0];
                if(fe=='T')
                {
                    fe=m[i][1];
                }
                for(int j=0;j<4;j++)
                {
                    if(fe=='.')
                    {
                        flag=1;
                        break;
                    }
                    if(m[i][j]!='T' && m[i][j] != fe)
                        {
                            flag=1;
                            break;
                        }
                }
                if(flag==0)
                {
                    winner[u]=fe;
                    //cout<<"\nwinner["<<u<<"]"<<winner[u];
                    break;
                }
                flag=0;
                fe=m[0][i];
                if(fe=='T')
                {
                    fe=m[1][i];
                }
                for(int j=0;j<4;j++)
                {
                    if(fe=='.')
                    {
                        flag=1;
                        break;
                    }

                    if(m[j][i]!='T' && m[j][i] != fe)
                        {
                            flag=1;
                            break;
                        }
                }
                if(flag==0)
                {
                    winner[u]=fe;
                    //cout<<"\nwinner["<<u<<"]"<<winner[u];
                    break;
                }
            }
            if(winner[u]=='.'|winner[u]=='n')
            {
                int dflag=0,diflag=0;
                char dfe=m[0][0];
                if(dfe=='T')
                {
                    dfe=m[1][1];
                }
                char dife=m[0][3];
                if(dife=='T')
                {
                    dife=m[1][2];
                }
                if(dfe=='.')
                    dflag=1;
                if(dife=='.')
                    diflag=1;
                for(int i=0;i<4;i++)
                {
                    if(dflag==0)
                        if(m[i][i]!='T' && m[i][i]!=dfe)
                            dflag=1;
                    if(diflag==0)
                        if(m[i][4-1-i]!='T' && m[i][4-1-i]!=dife)
                            diflag=1;
                    if(diflag==1 && dflag==1)
                        break;
                }
                if(diflag==0)
                {
                    winner[u]=dife;
                    //cout<<"\nwinner["<<u<<"]"<<winner[u];

                }
                if(dflag==0)
                {
                    winner[u]=dfe;
                    //cout<<"\nwinner["<<u<<"]"<<winner[u];
                }
            }
        }
    /*for(int i=0;i<cases;i++)
    {
        for(int j=0;j<4;j++)
            cout<<m[i][j]<<"\t";
        cout<<"\n";
    }*/
    ofstream myfile;
    myfile.open ("1.txt");
    for(int i=0;i<cases;i++)
    {
        myfile<<"\nCase #"<<i+1<<": ";
        switch(winner[i])
        {
            case 'n':
                myfile<<"Draw";
                break;
            case '.':
                myfile<<"Game has not completed";
                break;
            case 'X':
                myfile<<"X won";
                break;
            case 'O':
                myfile<<"O won";
                break;
            default:
                myfile<<"ERROR";
        }
    }
    int a;
    cin>>a;
}
