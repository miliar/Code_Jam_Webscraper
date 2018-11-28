#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
char row_check(string a[]);
char col_check(string a[]);
char dia_check(string a[]);
int dot;
int main()
{
 ifstream fin("gc.in");
 ofstream fout("gout.txt");

int t,i,j;
char res;
string a[5];
fin>>t;
for(i=0;i<t;i++)
{
    dot=0;
 for(j=0;j<4;j++)
   {
       fin>>a[j];

   }
   res=row_check(a);
   if(res!='a')
   {

   fout<<"Case #"<<i+1<<": "<<res<<" won"<<endl;
   continue;
   }

if(res=='a')
{
res=col_check(a);

}
if(res!='a')
{
   fout<<"Case #"<<i+1<<": "<<res<<" won"<<endl;
   continue;
}
if(res=='a')
{
    res=dia_check(a);
}
if(res!='a')
{
   fout<<"Case #"<<i+1<<": "<<res<<" won"<<endl;
   continue;
}
if(res=='a')
 {
     if (dot==1)
    fout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
     else
     fout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
 }



}







return 0;
}


char row_check(string a[])
{
    char t;
    int j,i;
    for(i=0;i<4;i++)
     {

         t=a[i][0];
         if(t=='T')
         t=a[i][1];
         for(j=0;j<4;j++)
           {
               if((a[i][j]!=t && a[i][j]!='T')||(a[i][j]=='.'))
               {
                if(dot!=1)
               {
                   if(a[i][j]=='.')
                   dot=1;

               }
               break;
               }
           }

           if(j==4)
           {
             break;

           }
     }

     if(i==4)
     t='a';

     return t;
}

char col_check(string a[])
{
    char t;
    int k,i;

      for(k=0;k<4;k++)
     {

         t=a[0][k];
         if(t=='T')
         t=a[1][k];
         for(i=0;i<4;i++)
           {
               if((a[i][k]!=t && a[i][k]!='T')||(a[i][k]=='.'))
               break;

           }

           if(i==4)
            break;

     }


     if(k==4)
     t='a';


     return t;
}


char dia_check(string a[])
{
    char t;
    int j,i;
     t=a[0][0];
     if(t=='T')
     t=a[1][1];
     for(i=0;i<4;i++)
      {
          if((a[i][i]!=t && a[i][i]!='T')||(a[i][i]=='.'))
          break;
      }
      if(i==4)
      return t;
     else
       {

           t=a[0][3];
           if(t=='T')
            t=a[1][2];
          for(i=3;i>-1;i--)
      {
          if((a[3-i][i]!=t && a[3-i][i]!='T')||(a[3-i][i]=='.'))
          break;
      }

      if(i==-1)
       return t;
      else
       return 'a';

       }





}
