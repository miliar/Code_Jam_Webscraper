//in the name of GOD
#include<fstream.h>
#include<stdio.h>
#include<conio.h>
void main()
{
int cases,row1,row2,matrix1[4][4],matrix2[4][4],match=0,done=0,number,i,j;
ifstream ifile("a1.in",ios::in);
ofstream ofile("a1.out",ios::out);
ifile>>cases;

while(done<cases)
{
 match=0;
 ifile>>row1;
 for(i=0;i<4;i++)
 {
  for(j=0;j<4;j++)
  {
  ifile>>matrix1[i][j];
  }
 }
 ifile>>row2;
 for(i=0;i<4;i++)
 {
  for(j=0;j<4;j++)
  {
  ifile>>matrix1[i][j];
  }
 }
 for(i=0;i<4;i++)
 {
  for(j=0;j<4;j++)
  {
  if(matrix1[row1-1][i]==matrix2[row2-1][j])
  {
  match=match+1;
  number=matrix1[row1-1][i];
  }
  }
 }
done=done+1;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
ofile<<matrix1[i][j];
}
}
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
ofile<<matrix2[i][j];
}
}
if(match==0)
{
ofile<<"Case #"<<done<<": "<<"Volunteer cheated!\n";
}
else if(match==1)
{
ofile<<"Case #"<<done<<": "<<number<<"\n";
}
else if(match==2)
{
ofile<<"Case #"<<done<<": "<<"Bad magician!\n";
}
}



}