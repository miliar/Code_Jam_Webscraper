#include<iostream>
using namespace std;
int main()
{
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        int testcase,i,j;
        int temp;
        char array[4][4]={{'.','.','.','.'},
                        {'.','.','.','.',},
                        {'.','.','.','.'},
                        {'.','.','.','.'}};
        cin>>testcase;
        temp=testcase;
        while(testcase>0)
        {
           for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    cin>>array[i][j];
                }
            }
            //for(i=0;i<4;j++)
            //scanf("%s",array[i]);
            //scanf("",NULL);
            /*for(i=0;i<4;i++)
             {
                 for(j=0;j<4;j++)
                 {
                  cout<<array[i][j]<<" ";
                 }
                 cout<<endl;
             }*/

            if((array[0][0]==array[1][1])&&(array[1][1]==array[2][2])&&(array[2][2]==array[3][3])&&(array[3][3]=='X'))
            {
                cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
               goto z;
            }
                else if((array[0][0]=='T')&&(array[1][1]==array[2][2])&&(array[2][2]==array[3][3])&&(array[3][3]=='X'))
                {
                cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
                   goto z;
                }
                else if((array[0][0]==array[1][1])&&(array[1][1]==array[2][2])&&(array[2][2]=='X')&&(array[3][3]=='T'))
                {cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
               goto z;
            }
                if((array[0][0]==array[1][1])&&(array[1][1]==array[2][2])&&(array[2][2]==array[3][3])&&(array[3][3]=='O'))
                {cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
                   goto z;
            }
                else if((array[0][0]=='T')&&(array[1][1]==array[2][2])&&(array[2][2]==array[3][3])&&(array[3][3]=='O'))
                {cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
                   goto z;
            }
                else if((array[0][0]==array[1][1])&&(array[1][1]==array[2][2])&&(array[2][2]=='X')&&(array[3][3]=='O'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
               goto z;
            }




            if((array[0][3]==array[1][2])&&(array[1][2]==array[2][1])&&(array[2][1]==array[3][0])&&(array[3][0]=='X'))
            {
                cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
               goto z;
            }
                else if((array[0][3]=='T')&&(array[1][2]==array[2][1])&&(array[2][1]==array[3][0])&&(array[3][0]=='X'))
                {
                cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
                   goto z;
                }
                else if((array[0][3]==array[1][2])&&(array[1][2]==array[2][1])&&(array[2][1]=='X')&&(array[3][0]=='T'))
                {cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
               goto z;
            }
             if((array[0][3]==array[1][2])&&(array[1][2]==array[2][1])&&(array[2][1]==array[3][0])&&(array[3][0]=='O'))
            {
                cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
               goto z;
            }
                else if((array[0][3]=='T')&&(array[1][2]==array[2][1])&&(array[2][1]==array[3][0])&&(array[3][0]=='O'))
                {
                cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
                   goto z;
                }
                else if((array[0][3]==array[1][2])&&(array[1][2]==array[2][1])&&(array[2][1]=='O')&&(array[3][0]=='T'))
                {cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
               goto z;
            }







            for(i=0;i<4;i++)
            {
                if((array[i][0]==array[i][1])&&(array[i][1]==array[i][2])&&(array[i][2]==array[i][3])&&(array[i][3]=='X'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
                   goto z;
                }
                else if((array[i][0]=='T') && (array[i][1]==array[i][2])&&(array[i][2]==array[i][3])&&(array[i][3]=='X'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
                   goto z;
                }
                else if((array[i][0]==array[i][1])&&(array[i][1]==array[i][2])&&(array[i][2]=='X') && (array[i][3]=='T'))
                {
                   // cout<<"i m in";
                    cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
                   goto z;
                }
                else if((array[i][0]==array[i][1])&&(array[i][1]==array[i][2])&&(array[i][2]==array[i][3])&&(array[i][3]=='O'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
                   goto z;
                }
                else if((array[i][0]=='T') && (array[i][1]==array[i][2])&&(array[i][2]==array[i][3])&&(array[i][3]=='O'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
                   goto z;
                }
                else if((array[i][0]==array[i][1])&&(array[i][1]==array[i][2])&&(array[i][2]=='O') && (array[i][3]=='T'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
                   goto z;
                }



                else if((array[0][i]==array[1][i])&&(array[1][i]==array[2][i])&&(array[2][i]==array[3][i])&&(array[3][i]=='X'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
                   goto z;
                }
                else if((array[0][i]=='T') && (array[1][i]==array[2][i])&&(array[2][i]==array[3][i])&&(array[3][i]=='X'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
                   goto z;
                }
                else if((array[0][i]==array[1][i])&&(array[1][i]==array[2][i])&&(array[2][i]=='X') && (array[3][i]=='T'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": X won"<<endl;
                   goto z;
                }
                else if((array[0][i]==array[1][i])&&(array[1][i]==array[2][i])&&(array[2][i]==array[3][i])&&(array[3][i]=='O'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
                   goto z;
                }
                else if((array[0][i]=='T') && (array[1][i]==array[2][i])&&(array[2][i]==array[3][i])&&(array[3][i]=='O'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
                   goto z;
                }
                else if((array[0][i]==array[1][i])&&(array[1][i]==array[2][i])&&(array[2][i]=='O') && (array[3][i]=='T'))
                {
                    cout<<"Case #"<<temp-testcase+1<<": O won"<<endl;
                   goto z;
                }
                }
             for(i=0;i<3;i++)
             {
                 for(j=0;j<3;j++)
                 {if(array[i][j]=='.')
                    {
                        cout<<"Case #"<<temp-testcase+1<<": Game has not completed"<<endl;
                       goto z;
                    }
                 }
             }

             cout<<"Case #"<<temp-testcase+1<<": Draw"<<endl;




        z:    testcase--;
        //cin>>temp;
        }


        return 0;
}
