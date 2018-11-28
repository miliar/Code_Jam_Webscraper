#include <iostream>
#include<string>
#include<stdio.h>
#include <fstream>
#include<cmath>
using namespace std;
int con(string s)
{
    int n=s.length();
    int t=0;
    for(int i=0;i<n;i++)
    {
        t+=(s[i]-'0')*pow(10.00,n-1);
        n--;
    }
    return t;
}
int main()
{

   int cases=0,flag1[1000],flag2[1000],flag3[1000];
   int g;
   string line;
   string in[1000][4];
   //cin>>cases;
   //for(int t=0;t<cases;t++)
   //{for(int i=0;i<4;i++)
   //cin>>in[t][i];
   //}



  ifstream myfile ("E:\\downloadds\\A-large.in");
  if (myfile.is_open())
  {
   getline (myfile,line);
   cases=con(line);

  for(int t=0;t<cases;t++)
   {
    for(int i=0;i<4;i++)
   {
       getline (myfile,line);
       in[t][i]=line;

    }
    getline (myfile,line);
   }
    myfile.close();
  }





    for(int t=0;t<cases;t++)
   {
       flag1[t]=0;flag2[t]=0;flag3[t]=0;

     if(((in[t][0][0]=='X'||in[t][0][0]=='T')
          &&(in[t][1][1]=='X'||in[t][1][1]=='T')&&
          (in[t][2][2]=='X'||in[t][2][2]=='T')&&(in[t][3][3]=='X'||in[t][3][3]=='T'))||(
          (in[t][0][3]=='X'||in[t][0][3]=='T')
          &&(in[t][1][2]=='X'||in[t][1][2]=='T')&&
          (in[t][2][1]=='X'||in[t][2][1]=='T')&&(in[t][3][0]=='X'||in[t][3][0]=='T')))
          {
              flag2[t]=1;
        continue;
          }

     if(((in[t][0][0]=='O'||in[t][0][0]=='T')
          &&(in[t][1][1]=='O'||in[t][1][1]=='T')&&
          (in[t][2][2]=='O'||in[t][2][2]=='T')&&(in[t][3][3]=='O'||in[t][3][3]=='T'))||(
          (in[t][0][3]=='O'||in[t][0][3]=='T')
          &&(in[t][1][2]=='O'||in[t][1][2]=='T')&&
          (in[t][2][1]=='O'||in[t][2][1]=='T')&&(in[t][3][0]=='O'||in[t][3][0]=='T')))
          {
              flag3[t]=1;
        continue;
          }
        for(int i=0;i<4;i++)
   {
       if(in[t][i][0]=='.'||in[t][i][1]=='.'||in[t][i][2]=='.'||in[t][i][3]=='.')
       {
           flag1[t]=1;
           //continue;
       }
       if(((in[t][i][0]=='X'||in[t][i][0]=='T')
          &&(in[t][i][1]=='X'||in[t][i][1]=='T')&&
          (in[t][i][2]=='X'||in[t][i][2]=='T')&&(in[t][i][3]=='X'||in[t][i][3]=='T'))||(
          (in[t][0][i]=='X'||in[t][0][i]=='T')
          &&(in[t][1][i]=='X'||in[t][1][i]=='T')&&
          (in[t][2][i]=='X'||in[t][2][i]=='T')&&(in[t][3][i]=='X'||in[t][3][i]=='T')))
       {
                      flag2[t]=1;
           break;
       }
              if(((in[t][i][0]=='O'||in[t][i][0]=='T')
                 &&(in[t][i][1]=='O'||in[t][i][1]=='T')&&
                 (in[t][i][2]=='O'||in[t][i][2]=='T')&&(in[t][i][3]=='O'||in[t][i][3]=='T'))||
          ((in[t][0][i]=='O'||in[t][0][i]=='T')
          &&(in[t][1][i]=='O'||in[t][1][i]=='T')&&
          (in[t][2][i]=='O'||in[t][2][i]=='T')&&(in[t][3][i]=='O'||in[t][3][i]=='T')))
       {
                      flag3[t]=1;
           break;
       }

   }




       }

ofstream imyfile ("E:\\3 rd sem\\CodeChef\\Tic-Tac-Toe-Tomek\\result4.txt");
  if (imyfile.is_open())
  {
    for(int i=0;i<cases;i++)
{
if(flag2[i]==1)
imyfile<<"Case #"<<i+1<<": X won\n";
else if(flag3[i]==1)
imyfile<<"Case #"<<i+1<<": O won\n";
else if(flag1[i]==1)
imyfile<<"Case #"<<i+1<<": Game has not completed\n";
else
imyfile<<"Case #"<<i+1<<": Draw\n";}
  }


   return 0;
   }
