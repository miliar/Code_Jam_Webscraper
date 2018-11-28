#include<iostream.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream.h>

int mat[30][20],m,n,mm_r[30][2]={0},mm_c[30][2]={0};
ofstream of("of_lm.txt",ios::out);
void intit_minmax()
{
  int i,j;
  for(i=0;i<m;i++)
  {
    mm_r[i][0]=mat[i][0];
    mm_r[i][1]=mat[i][0];
  }
  for(i=0;i<n;i++)
  {
    mm_c[i][0]=mat[0][i];
    mm_c[i][1]=mat[0][i];

  }

  for(i=0;i<m;i++)
  {
   for(j=0;j<n;j++)
   {
     if(mat[i][j]>mm_r[i][1])
      mm_r[i][1]=mat[i][j];
     if(mat[i][j]<mm_r[i][0])
      mm_r[i][0]=mat[i][j];
     // cout<<"\n"<<i<<" "<<j;

     if(mat[i][j]>mm_c[j][1])
      mm_c[j][1]=mat[i][j];
     if(mat[i][j]<mm_c[j][0])
      mm_c[j][0]=mat[i][j];
   }
  }

  for(i=0;i<n;i++)
  {
   cout<<"   "<<mm_c[i][0]<<" "<<mm_c[i][1];

  }


}
void print_res()
{
 int i,j,t;
 intit_minmax();
 for(i=0;i<m;i++)
  for(j=0;j<n;j++)
  {
    t=mat[i][j];
    //if(!(t<=mm_r[i][1]&&t>=mm_c[j][0]) && (t>=mm_r[i][0]&&t<=mm_c[j][0]))
    if((t<mm_r[i][1]&&t<mm_c[j][1]) )
    {
      of<<"NO";
      cout<<"no "<<i<<" "<<j<<" "<<mm_r[i][1]<<" "<<mm_c[i][1]<<" "<<mm_r[i][0]<<" "<<mm_c[i][0];
      return;
    }
  }
  of<<"YES";
  cout<<"YES";


}


void main()
{
 clrscr();
 long nc,i,j,k;
 char str[10],*ptr;
 fstream mf("lmip.txt",ios::in);
 mf.getline(str,8,'\n');
 nc=strtol(str,&ptr,10);
 cout<<"nc"<<nc;
 getch();

 for(i=1;i<=nc;i++)
 {
   of<<"Case #"<<i<<": ";
   mf.getline(str,5,' ');
   m=atoi(str);
   mf.getline(str,5,'\n');
   n=atoi(str);
   //cout<<"\n"<<m<<" "<<n;
   for(j=0;j<m;j++)
   {
     for(k=0;k<n-1;k++)
     {
       mf.getline(str,4,' ');
       mat[j][k]=atoi(str);
     }
     mf.getline(str,4,'\n');
     mat[j][k]=atoi(str);
   }

   for(j=0;j<m;j++)
   {
    cout<<"\n";
    for(k=0;k<n;k++)
     cout<<" "<<mat[j][k];
   }

   print_res();
   of<<"\n";
   /*
    print_res();
     */

 }
 cout<<"done";
 getch();
}