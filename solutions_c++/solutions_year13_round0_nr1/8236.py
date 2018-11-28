
#include<iostream.h>
#include<fstream.h>

ifstream fin("A.txt");
ofstream fout("ans.txt");

char c[4][4];

int check1(int a)
{
 char ch;
 int flag,k,i,j;

 for(i=0;i<4;i++)
 {
  flag=0;
  k=0;
  ch=c[i][0];
  if(ch!='.')
  {
   if(ch=='T')
   k=1;
   for(j=1;j<4;j++)
   {
    if(ch!=c[i][j])
    {
     if(c[i][j]=='T')
     {
      if(k!=0)
      {
       flag=1;
       break;
      }
      else
      k=1;
     }
     else
     {
      flag=1;
      break;
     }
    }
   }
   if(flag==0)
   {
    fout<<"Case #"<<a<<": "<<ch<<" won"<<"\n";
    return 0;
   }
  }
 }
 for(i=0;i<4;i++)
 {
  flag=0;
  k=0;
  ch=c[0][i];
  if(ch!='.')
  {
   if(ch=='T')
   k=1;
   for(j=1;j<4;j++)
   {
    if(ch!=c[j][i])
    {
     if(c[j][i]=='T')
     {
      if(k!=0)
      {
       flag=1;
       break;
      }
      else
      k=1;
     }
     else
     {
      flag=1;
      break;
     }
    }
   }
   if(flag==0)
   {
    fout<<"Case #"<<a<<": "<<ch<<" won"<<"\n";
    return 0;
   }
  }
 }

 ch=c[0][0];
 flag=0;
 k=0;
 if(ch!='.')
 {
  if(ch=='T')
  k=1;
  for(j=0;j<4;j++)
  {
   if(ch!=c[j][j])
   {
    if(c[i][j]=='T')
    {
     if(k!=0)
     {
      flag=1;
      break;
     }
     else
     k=1;
    }
    else
    {
     flag=1;
     break;
    }
   }
  }
  if(flag==0)
  {
   fout<<"Case #"<<a<<": "<<ch<<" won"<<"\n";
   return 0;
  }
 }

 flag=0;
 k=0;
 ch=c[0][3];
 if(ch!='.')
 {
  if(ch=='T')
  k=1;
  for(i=1,j=2;j>=0;i++,j--)
  {
   if(ch!=c[i][j])
   {
    if(c[i][j]=='T')
    {
     if(k!=0)
     {
       flag=1;
      break;
     }
     else
     k=1;
    }
    else
    {
     flag=1;
     break;
    }
   }
  }
  if(flag==0)
  {
   fout<<"Case #"<<a<<": "<<ch<<" won"<<"\n";
   return 0;
  }
 }
 for(i=0;i<4;i++)
 {
  for(j=0;j<4;j++)
  {
   if(c[i][j]=='.')
   {
    fout<<"Case #"<<a<<": Game has not completed"<<"\n";
    return 0;
   }
  }
 }
 fout<<"Case #"<<a<<": Draw"<<"\n";
 return 0;
}








void main()
{
 int a;
 fin>>a;
 for(int s=0;s<a;s++)
 {
  for(int i=0;i<4;i++)
  {
   fin>>c[i];
  }
  check1(s+1);
 }
}
