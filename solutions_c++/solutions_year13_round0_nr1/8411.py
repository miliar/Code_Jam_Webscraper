#include<fstream.h>
#include<conio.h>
#include<stdio.h>
void main()
{
 int i, j,k, num, count, count2, flag, flag1, flag2;
 char gameline[4][5], ch, temp, temp2;
 clrscr();
 ofstream fout("Output1.txt");
 ifstream fin("Test1.txt");
 fin.seekg(0);
 fin>>num;
 fin.get(ch);
 for(i=0;i<num;i++)
 {
  fin.get(gameline[0],5);
  fin.get(ch);
  fin.get(gameline[1],5);
  fin.get(ch);
  fin.get(gameline[2],5);
  fin.get(ch);
  fin.get(gameline[3],5);
  fin.get(ch);
  fin.get(ch);
  flag=0;
  flag1=0;
  flag2=0;
  for(j=0;j<4;j++)
  {
   count=0;
   if(gameline[j][0]!='T')
    temp=gameline[j][0];
   else
    {
     temp=gameline[j][1];
     count++;
    }
   k=count+1;
   if(temp=='.')
   {
    flag=1;
    k=4;
   }
   while(k<4)
   {
    if((temp==gameline[j][k])||(gameline[j][k]=='T'))
    {
     count++;
    }
    if(gameline[j][k]=='.')
    {
     flag=1;
     k=4;
     if((k==j)||(k==3-j))
     flag2=1;
    }
    k++;
   }
   //cout<<count<<endl;
   if((count==3)&&(temp!='.'))
   {
    fout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<'\n';
    j=4;
    flag1=1;
   }
  }
  if(flag1!=1)
  {
  for(j=0;j<4;j++)
  {
   count=0;
   if(gameline[0][j]!='T')
    temp=gameline[0][j];
   else
    {
     temp=gameline[1][j];
     count++;
    }
   if(temp=='.')
   {
    flag=1;
    k=4;
    count--;
   }
   k=count+1;
   while(k<4)
   {
    if((temp==gameline[k][j])||(gameline[k][j]=='T'))
    {
     count++;
    }
    if(gameline[k][j]=='.')
    {
     flag=1;
     k=4;
     count--;
     if((k==j)||(k==3-j))
     flag2=1;
    }
    k++;
   }
   //cout<<count<<endl;
   if((count==3)&&(temp!='.'))
   {
    fout<<"Case #"<<i+1<<": "<<temp<<" won"<<'\n';
    j=4;
    flag2=1;
   }
  }
  }
  if((flag1!=1)&&(flag2!=1))
  {
   count=0; count2=0;
   temp=gameline[0][0];
   temp2=gameline[0][3];
   for(j=1;j<4;j++)
   {
    if(gameline[j][j]==temp)
    {
     count++;
    }
    if(gameline[j][3-j]==temp2)
    {
     count2++;
    }
   }
   if((count==3)&&(temp!='.'))
   {
    fout<<"Case #"<<i+1<<": "<<temp<<" won"<<'\n';
    flag1=1;
   }
   else if((count2==3)&&(temp2!='.'))
   {
    fout<<"Case #"<<i+1<<": "<<temp2<<" won"<<'\n';
    flag1=1;
   }
  }
  if(((flag1==0)&&(flag2==0))&&(flag==0))
  {
   fout<<"Case #"<<i+1<<": "<<"Draw"<<'\n';
  }
  if(((flag1==0)&&(flag2==0))&&(flag==1)&&(temp=='.'))
  {
   fout<<"Case #"<<i+1<<": "<<"Game has not completed"<<'\n';
  }
 }
 fout.close();
 getch();
}


