#include<iostream>

using namespace std;

char a[4][4];
int main()
{
    int T;
    int i,j,k;
    bool flag=false;
    int finish=1;
    char winner='N';
    char temp;
    cin>>T;

    for(k=0;k<T;k++)
    {
        //printf("inside");
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>a[i][j];
            } // FOR j
        } //FOR i

        if(a[0][0]=='.')
        {
            finish=0;
        }

        temp=a[0][0];
        for(i=1;i<4;i++)
        {
            if(a[0][i]=='.')
            {
                finish=0;
                flag=false;
                break;
            }

            if(temp=='T')
                temp=a[0][1];
            if(a[0][i]==temp || a[0][i]=='T')
            {
                flag=true;
                continue;
            }
            else
            {
                flag=false;
                break;
            }
        }

        if(flag==true)
        {
            winner=a[0][0];
            if(winner=='T')
                winner=a[0][1];
        }
        temp=a[0][0];
        if(flag==false)
        {
            for(i=1;i<4;i++)
            {
                if(a[i][0]=='.')
                {
                    finish=0;
                    flag=false;
                    break;
                }


                if(temp=='T')
                    temp=a[1][0];
                if(a[i][0]==temp || a[i][0]=='T')
                {
                    flag=true;
                    continue;
                }
                else
                {
                    flag=false;
                    break;
                }
            }

            if(flag==true)
            {
                winner=a[0][0];
                if(winner=='T')
                    winner=a[1][0];
            }
            else
            {
                temp=a[0][0];
                for(i=1;i<4;i++)
                {
                    if(a[i][i]=='.')
                    {
                        finish=0;
                        flag=false;
                        break;
                    }

                    if(temp=='T')
                        temp=a[1][1];
                    if(a[i][i]==temp || a[i][i]=='T')
                    {
                        flag=true;
                        continue;
                    }
                    else
                    {
                        flag=false;
                        break;
                    }
                }

                if(flag==true)
                {
                    winner=a[0][0];
                    if(winner=='T')
                        winner=a[1][1];
                }

                else
                {
                    for(i=1;i<4;i++)
                    {
                        temp=a[i][0];
                        for(j=1;j<4;j++)
                        {
                            if(a[i][j]=='.')
                            {
                                finish=0;
                                flag=false;
                                break;
                            }


                            if(temp=='T')
                                temp=a[i][1];
                            if(a[i][j]==temp||a[i][j]=='T')
                            {
                                flag=true;
                                continue;
                            }
                            else
                            {
                                flag=false;
                                break;
                            }
                        }//for j
                        if(flag==true)
                            break;


                    }//for i
                    if(flag==true)
                    {
                           winner=a[i][0];
                            if(winner=='T')
                                winner=a[i][1];
                    }
                }//else
                temp=a[0][j];
                if(flag==false)
                {
                    for(i=1;i<4;i++)
                    {
                        temp=a[0][i];
                        for(j=1;j<4;j++)
                        {
                            if(a[j][i]=='.')
                            {
                                finish=0;
                                flag=false;
                                break;
                            }


                            if(temp=='T')
                                temp=a[1][j];
                            if(a[j][i]==temp||a[j][i]=='T')
                            {
                                flag=true;
                                continue;
                            }
                            else
                            {
                                flag=false;
                                break;
                            }
                        }//for j
                        if(flag==true)
                            break;


                    }//for i
                    if(flag==true)
                    {
                           winner=a[0][i];
                            if(winner=='T')
                                winner=a[1][i];
                    }
                }


                if(flag==false)
                {
                    j=2;
                    temp=a[0][3];
                    for(i=1;i<4;i++)
                    {
                        if(a[i][j]=='.')
                        {
                            finish=0;
                            flag=false;
                            break;
                        }


                        if(temp=='T')
                            temp=a[1][2];
                        if(a[i][j]==temp||a[i][j]=='T')
                        {

                            j--;
                            flag=true;
                            continue;
                        }
                        else
                        {
                            flag=false;
                            break;
                        }
                    }

                    if(flag==true)
                    {
                        winner=a[0][3];
                        if(winner=='T')
                                winner=a[1][2];
                        //cout<<"here";
                    }
                }

                if(flag==false)
                {
                    temp=a[0][3];
                    if(temp=='T')
                        temp=a[1][3];
                    for(i=1;i<4;i++)
                    {
                        if(a[i][3]=='.')
                        {
                            finish=0;
                            flag=false;
                            break;
                        }
                        if(a[i][3]==temp || a[i][3]=='T')
                        {
                            flag=true;
                            continue;
                        }
                        else
                        {
                            flag=false;
                            break;
                        }
                    }
                    if(flag==true)
                    {
                        winner=a[0][3];
                        if(winner=='T')
                        {
                            winner=a[1][3];
                        }
                    }
                }



            //printf("%c %d\n",winner,finish);
            //cout<<winner<<" "<< finish << endl;
        }

                //printf("case : %c wins",winner);
    }
    if( (winner=='N' || winner=='.') && finish==0)
            {
                cout<<"Case #"<<k+1<<": "<<"Game has not completed"<<endl;

                //printf("case #: did not finish" );
            }
            else if(winner=='N' && finish==1)
            {
                cout<<"Case #"<<k+1<<": "<<"Draw"<<endl;
                //printf("finished");
            }
            else
                cout<<"Case #"<<k+1<<": "<<winner<<" won"<<endl;

        winner='N';
        finish=1;
        flag=false;
  //  scanf("%c",&T);
    }
    return 0;
}
