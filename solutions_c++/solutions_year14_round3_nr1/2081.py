#include<fstream.h>
#include<conio.h>

ifstream fin("a.txt");
ofstream fout("ans.txt");

int num[110]={0},den[110]={0};
int inc=0;
/*
int chk_ind(int t)
{
 int m=0;
 while(t!=0)
 {
  t=t/2;
  m++;
 }
 return m;
}
 */
int calc(int cse)
{
 if(den[cse]%2==0)
 {
//  int m=chk_ind(num[cse]);
 // int n=chk_ind(den[cse]);
//  fout<<"Case #"<<cse+1<<": "<<n-m<<"\n";
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
 clrscr();
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
 getch();
}

