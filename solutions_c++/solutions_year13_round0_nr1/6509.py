#include <algorithm>
#include <iostream>
#include<string>
using namespace std;
int main()
{   int flag=0,flag2=0,flag3,flag4,flag5,flag6,flag7,flag8,flag9,flag10,flag11,flag12;
    char in[5][5],chk[10][5];
    string status1,status2,status3,status4;
    status1="X won";
    status2="O won";
    status3="Draw";
    status4="Game has not completed";
    int i,j,test,k,cases;
    cin>>cases;
    for(test=0; test<cases; test++)
    {
        flag=0;flag2=0;flag3=0;flag7=0;flag8=0;flag4=0;flag5=0;flag6=0;flag9=0;flag10=0;flag11=0;flag12=0;
            for(i=0; i<4; i++)
              cin>>in[i];
              k=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(i==j)
                {chk[9][j]=in[i][j];}
                
                chk[i][j]=in[i][j];
                
            }
        }
                
            k=4;
        for(j=0;j<4;j++)
        {
            for(i=0;i<4;i++)
            {
                chk[k][i]=in[i][j];
              
            }
              k++;
        }
                
                
        for(i=3;i>=0;i--)
        {
            for(j=0;j<4;j++)
            {
                if(i+j==3)
                {
                    chk[8][j]=in[i][j];
                }
            }
        }
        for(i=0;i<10;i++)
        chk[i][4]='\0';
        for(i=0;i<10;i++)
        {
            
            flag3=strcmp(chk[i],"XXXX");
            flag4=strcmp(chk[i],"XXXT");
            flag5=strcmp(chk[i],"OOOO");
            flag6=strcmp(chk[i],"OOOT");
            flag7=strcmp(chk[i],"TOOO");
            flag8=strcmp(chk[i],"TXXX");
            flag9=strcmp(chk[i],"XTXX");
            flag10=strcmp(chk[i],"XXTX");
            flag11=strcmp(chk[i],"OOTO");
            flag12=strcmp(chk[i],"OTOO");
            
            if(flag3==0||flag4==0||flag8==0||flag9==0||flag10==0)
           { cout<<"Case #"<<test+1<<": "<<status1<<endl;
            flag=1;
                break;}
           else if(flag5==0||flag6==0||flag7==0||flag11==0||flag12==0)           
            { cout<<"Case #"<<test+1<<": "<<status2<<endl;
            flag=1;
                break;}
            }
        if(flag==0)
        {
            for(i=0;i<10;i++)
            {
            for(j=0;j<4;j++)
            {
                if(chk[i][j]=='.')
                {flag2=1;
                break;}
                }
                }}
        if(flag==0&&flag2==0)
        {cout<<"Case #"<<test+1<<": "<<status3<<endl;}
         if(flag==0&&flag2==1)
        {cout<<"Case #"<<test+1<<": "<<status4<<endl;}
        
    }
   // system("pause");
    return 0;
}
