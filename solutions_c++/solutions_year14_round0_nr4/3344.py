#include<fstream.h>
#include<conio.h>

double nao[1000],ken[1000];
int num,counter=1;

ifstream fin("input.txt");
ofstream fout("output.txt");

void compare_war()
{
 int fn=0,en=num-1,fk=0,ek=num-1;
 int wins=0;

 while(fk<num && fn<=en)
 {
  if(ken[fk]>nao[fn])
  {
   wins++;
   fk++;
   fn++;
  }
  else
  {
   fk++;
   en--;
  }
 }

 wins=num-wins;

 fout<<" "<<wins<<"\n";

}

void compare_deceitful()
{
 int fn=0,en=num-1,fk=0,ek=num-1;
 int wins=0;

 while(fn<num && fk<=ek)
 {
   if(nao[fn]>ken[fk])
   {
    wins++;
    fn++;
    fk++;
   }
   else
   {
    fn++;
    ek--;
   }
 }

 fout<<"Case #"<<counter<<": "<<wins;
}

void swap(int pos1,int pos2,int flag)
{
  if(flag==0)
  {
   double temp=nao[pos1];
   nao[pos1]=nao[pos2];
   nao[pos2]=temp;
  }
  else
  {
   double temp=ken[pos1];
   ken[pos1]=ken[pos2];
   ken[pos2]=temp;
  }
}

int sort_partition(int beg,int end,int flag)
{
  if(flag==0)
  {
    //Pivot element
    double pivot=nao[beg];

    //Starting for the checking
    int b=beg+1;

   //Ending for the checking
   int e=end;

   while(b<e)
   {
     //Checking for the lower elements
     while(pivot>nao[b] && b<=end)
     b++;

     //Checking for the higher elements
     while(pivot<nao[e] && e>beg)
     e--;

     if(b<e)
     swap(b,e,flag);
   }

   if(nao[beg]>nao[e])
   swap(beg,e,flag);

   return e;

  }
  else
  {
    //Pivot element
    double pivot=ken[beg];

    //Starting for the checking
    int b=beg+1;

    //Ending for the checking
    int e=end;

    while(b<e)
    {
      //Checking for the lower elements
      while(pivot>ken[b] && b<=end)
      b++;

      //Checking for the higher elements
      while(pivot<ken[e] && e>beg)
      e--;

      if(b<e)
      swap(b,e,flag);
    }

    if(ken[beg]>ken[e])
    swap(beg,e,flag);

    return e;

  }

}

void quick_sort(int start,int last,int flag)
{

 if(start<last)
 {
  //to store the position of the partition
  int pos=sort_partition(start,last,flag);

  //array to the left of the new pivot
  quick_sort(start,pos-1,flag);

  //array to the right of the new pivot
  quick_sort(pos+1,last,flag);
 }
}

void main()
{
 clrscr();

 //Loop variable
 int i,test;

 fin>>test;

 while(counter<=test)
 {
   fin>>num;

   for(i=0;i<num;i++)
   fin>>nao[i];

   for(i=0;i<num;i++)
   fin>>ken[i];

   quick_sort(0,num-1,0);
   quick_sort(0,num-1,1);

   compare_deceitful();
   compare_war();

   counter++;
 }


 getch();
}
