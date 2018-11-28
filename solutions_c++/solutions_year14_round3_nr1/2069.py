#include<fstream>
#include<conio.h>
#include<iostream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("ans.txt");
int num[110]={0},den[110]={0};
int inc=0;
int calc(int cse)
{
 if(den[cse]%2==0)
 {
  double target=(double)num[cse]/den[cse];
  int move=0;
   while((target-1)<0)
   {
    target=2*target;
    move++;
    if(move>40)
    {
     fout<<"Case #"<<cse+1<<": impossible\n";
     return 0;
    }
   }
   int temp_m=move;
   target=target-1;
   while(target>0)
   {
    while((target-1)<0)
    {
     target=2*target;
     temp_m++;
     if(temp_m>40)
     {
      fout<<"Case #"<<cse+1<<": impossible\n";
      return 0;
     }
    }
    target=target-1;
   }
   if(target!=0)
   {
    fout<<"Case #"<<cse+1<<": impossible\n";
    return 0;
   }
   fout<<"Case #"<<cse+1<<": "<<move<<"\n";
 }
 else
 {
  fout<<"Case #"<<cse+1<<": impossible\n";
  return 0;
 }
 return 1;
}

void main()
{
 
 int total;
 fin>>total;
 char temp;
 int k;
 for(int i=0;i<total;i++)
 {
  fin>>num[inc];
  fin.get(temp);
  fin>>den[inc];
  inc++;
  k=calc(i);
 }
 _getch();
}

