#include<iostream.H>
#include<conio.h>
#include<fstream.h>
void main()
{
 int a[4][4],temp1[4],temp2[4],cas,row1,row2,out[100],t,no;
 ifstream input;
 ofstream output;
 output.open("output.txt");
 input.open("a.txt");
 input>>cas;
 for(int i=0;i<cas;i++)
 {
  t=0;
  input>>row1;
  for(int j=0;j<4;j++)
  {
   if(j==row1-1)
   {
    for(int k=0;k<4;k++)
    {
     input>>a[j][k];
     temp1[k]=a[j][k];
    }
   }
   else
   {
    for(int k=0;k<4;k++)
    {
     input>>a[j][k];
    }
   }
  }
  input>>row2;
  for(j=0;j<4;j++)
  {
   if(j==row2-1)
   {
    for(int k=0;k<4;k++)
    {
     input>>a[j][k];
     temp2[k]=a[j][k];
    }
   }
   else
   {
    for(int k=0;k<4;k++)
    {
     input>>a[j][k];
    }
   }
  }
  for(int k=0;k<4;k++)
  {
   for(j=0;j<4;j++)
   {
    if(temp1[k]==temp2[j])
    {
     t++;
     no=temp1[k];
    }
   }
  }
  if(t==1)
  out[i]=no;
  else if(t==0)
  out[i]=-2;
  else
  out[i]=-1;
 }
 for(i=0;i<cas;i++)
 {
  if(out[i]==-1)
  output<<"Case #"<<i+1<<": Bad magician!";
  else if(out[i]==-2)
  output<<"Case #"<<i+1<<": Volunteer cheated!";
  else
  output<<"Case #"<<i+1<<": "<<out[i];
  output<<"\n";
 }
}