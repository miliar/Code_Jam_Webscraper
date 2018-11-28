#include<iostream.h>
#include<conio.h>
#include<fstream.h>


ifstream fin("a.txt");
ofstream fout("ans.txt");

int option1[4][4],option2[4][4];
int ch1,ch2;



void cal_card(int cse)
{
 int final,temp,ch=0;
 for(int i=0;i<4;i++)
 {
  temp=option1[ch1-1][i];
  for(int k=0;k<4;k++)
  {
   if(temp==option2[ch2-1][k])
   {
    final=temp;
    ch++;
   }
  }
 }
 if(ch==1)
  fout<<"Case #"<<cse+1<<": "<<final<<"\n";
 else if(ch==0)
  fout<<"Case #"<<cse+1<<": Volunteer cheated!\n";
 else
  fout<<"Case #"<<cse+1<<": Bad magician!\n";
}

void main()
{
 clrscr();
 int total;
 fin>>total;
 for(int i=0;i<total;i++)
 {
  fin>>ch1;
  for(int j=0;j<4;j++)
  {
   for(int k=0;k<4;k++)
    fin>>option1[j][k];
  }
  fin>>ch2;
  for(j=0;j<4;j++)
  {
   for(int k=0;k<4;k++)
    fin>>option2[j][k];
  }
  cal_card(i);
  cout<<"case"<<i<<"successful";
 }
 getch();
}

