#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int K=0;
    int n,countt,counto,countx,flag1,flag2,flag3,i,j,k,t;
      char a[4][4];
       ifstream fin;
       ofstream fout;
       string test;
       fin.open("input1.txt");
       fout.open("output1.txt");
       fin>>n;
     //  cout<<n;
       t=1;
       while(t<=n)
       {
             flag3=0;

                        for(i=0; i<4; i++)
                         for(j=0; j<4; j++)
                         {
                          fin>>a[i][j];
                          if(a[i][j]=='.')
                          flag3=1;
                          }

        K++;
        flag1=0;
        flag2=0;

        for(i=0;i<4;i++)
        {

                countx=0;
                counto=0;
                countt=0;

                    for(k=0;k<4;k++)
                   {
                       if(a[i][k]=='T')
                    countt++;
                    else if(a[i][k]=='X')
                    countx++;
                    else if(a[i][k]=='O')
                    counto++;
                   }
                    if(countt+countx==4)
                    flag1=1;
                    else if(countt+counto==4)
                    flag2=1;


        }

               for(j=0;j<4;j++)
               {
                    countx=0;
                counto=0;
                countt=0;

                    for(k=0;k<4;k++)
                   {

                    if(a[k][j]=='T')
                    countt++;
                    else if(a[k][j]=='X')
                    countx++;
                    else if(a[k][j]=='O')
                    counto++;
                   }

                    if(countt+countx==4)
                    flag1=1;
                    else if(countt+counto==4)
                    flag2=1;
            }



             countx=0;
                counto=0;
                countt=0;

                    for(k=0;k<4;k++)
                    {
                    if(a[k][k]=='T')
                    countt++;
                    else if(a[k][k]=='X')
                    countx++;
                    else if(a[k][k]=='O')
                    counto++;
                    }
                     if(countt+countx==4)
                    flag1=1;
                    else if(countt+counto==4)
                    flag2=1;

                 countx=0;
                counto=0;
                countt=0;
                int m=3;
                    for(k=0;k<4;k++)
                    {

                if(a[k][m]=='T')
                    countt++;
                    else if(a[k][m]=='X')
                    countx++;
                    else if(a[k][m]=='O')
                   { counto++;}
                    m--;
                    }
                     if(countt+countx==4)
                    flag1=1;
                    else if(countt+counto==4)
                    flag2=1;

//cout<<countx<<" "<<counto<<" "<<countt;

       if(flag1==1)
        fout<<"Case #"<<K<<": X won\n";
        else if(flag2==1)
        {
              fout<<"Case #"<<K<<": O won\n";
        }
        else if(flag3==1)
          fout<<"Case #"<<K<<": Game has not completed\n";

        else
         fout<<"Case #"<<K<<": Draw\n";

                    getline(fin,test);
                         // cout<<q;
                          t++;
         }
       fin.close();
       fout.close();

}

