#include<fstream.h>
#include<conio.h>

char a[4][4];
int flag=0,tr;

ifstream fin("C.txt");
ofstream fout("OutA.txt");

void diagonal_check_2()
{
 char ch;
 int i,j;

 ch=a[0][3];

 if(ch=='T')
 {
  for(i=0;i<4;i++)
  {
   for(j=0;j<4;j++)
   {
    if(i+j==3)
    {
     ch=a[i][j];
     if(ch!='T')
     break;
    }
   }
   if(ch!='T')
   break;
  }
 }

 for(i=0;i<4;i++)
 {
  if(ch=='X' || ch=='O')
  {
   for(j=0;j<4;j++)
   {
    if(i+j==3)
    {
     if(ch!=a[i][j] && a[i][j]!='T')
     {
      flag=0;
      break;
     }
     else
     flag=1;
    }
   }
  }

  if(flag==0)
  break;
 }

 if(flag==1)
 fout<<"Case #"<<tr<<": "<<ch<<" Won"<<'\n';
}

void diagonal_check_1()
{
 char ch;
 int i,j;

 ch=a[0][0];

 if(ch=='T')
 {
  for(i=1;i<4;i++)
  for(j=1;j<4;j++)
  {
   if(i==j)
   {
    ch=a[i][j];
    if(ch!='T')
    break;
   }
  }
 }

 for(i=0;i<4;i++)
 {
  if(ch=='X' || ch=='O')
  {
   for(j=0;j<4;j++)
   {
    if(i==j)
    {
     if(ch!=a[i][j] && a[i][j]!='T')
     {
      flag=0;
      break;
     }
     else
     flag=1;
    }
   }
  }
  if(flag==0)
  break;
 }

 if(flag==1)
 fout<<"Case #"<<tr<<": "<<ch<<" Won"<<'\n';
}

void column_check()
{
 char ch;
 int i,j,k;

 for(i=0;i<4;i++)
 {
  ch=a[0][i];
  k=1;

  while(ch=='T')
  {
   if(a[k][i]!='T')
   {
    ch=a[k][i];
    break;
   }
   else
   k++;
  }

  if(ch=='X' || ch=='O')
  {
   for(j=0;j<4;j++)
   {
    if(ch!=a[j][i] && a[j][i]!='T')
    {
     flag=0;
     break;
    }
    else
    flag=1;
   }
  }

  if(flag==1)
  break;
 }

 if(flag==1)
 fout<<"Case #"<<tr<<": "<<ch<<" Won"<<'\n';
}

void row_check()
{
 int i,j,k;
 char ch;

 for(i=0;i<4;i++)
 {
  ch=a[i][0];
  k=1;

  while(ch=='T')
  {
   if(a[i][k]!='T')
   {
    ch=a[i][k];
    break;
   }
   else
   k++;
  }

  if(ch=='X' || ch=='O')
  {
   for(j=0;j<4;j++)
   {
    if(ch!=a[i][j] && a[i][j]!='T')
    {
     flag=0;
     break;
    }
    else
    flag=1;
   }
  }

  if(flag==1)
  break;
 }

 if(flag==1)
 fout<<"Case #"<<tr<<": "<<ch<<" Won"<<'\n';
}

void game_check()
{
 int i,j;

 for(i=0;i<4;i++)  //game check
 {
  for(j=0;j<4;j++)
  {
   if(a[i][j]=='.')
   {
    fout<<"Case #"<<tr<<": Game has not completed"<<'\n';
    flag=1;
    break;
   }
  }
  if(flag==1)
  break;
 }
}

void main()
{
 clrscr();
 int test;

 fin>>test;

 for(tr=1;tr<=test;tr++)
 {

  fin>>a[0];
  fin>>a[1];
  fin>>a[2];
  fin>>a[3];


  if(flag==0)
  row_check();

  if(flag==0)
  column_check();

  if(flag==0)
  diagonal_check_1();

  if(flag==0)
  diagonal_check_2();

  if(flag==0)
  game_check();

  if(flag==0)
  fout<<"Case #"<<tr<<": Draw"<<'\n';
 }

 getch();
}