#include<fstream.h>
#include<conio.h>

int answer1,answer2,arran1[4][4],arran2[4][4],counter=1,test;

ifstream fin("input.txt");
ofstream fout("output.txt");

void compare_rows()
{
 int common,num=0,i,j;

 for(i=0;i<4;i++)
 {
  for(j=0;j<4;j++)
  {
   if(arran1[answer1][i]==arran2[answer2][j])
   {
    num++;
    common=arran1[answer1][i];
   }
  }
 }

 if(num==1)
 fout<<"Case #"<<counter<<": "<<common<<"\n";
 else if(num>1)
 fout<<"Case #"<<counter<<": Bad magician!\n";
 else if(num==0)
 fout<<"Case #"<<counter<<": Volunteer cheated!\n";
}

void main()
{
 clrscr();

 int i,j;

 fin>>test;

 while(counter<=test)
 {
  fin>>answer1;
  answer1=answer1-1;

  for(i=0;i<4;i++)
  {
   for(j=0;j<4;j++)
   fin>>arran1[i][j];
  }

  fin>>answer2;
  answer2=answer2-1;

  for(i=0;i<4;i++)
  {
   for(j=0;j<4;j++)
   fin>>arran2[i][j];
  }

  compare_rows();

  counter++;
 }


 getch();
}