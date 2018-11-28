#include<iostream.h>
#include<conio.h>
#include<fstream.h>
//Input file provided was renamed as a.txt
void main()
{
 int cas,a,b,k;
 long con;
 ifstream input;
 ofstream output;
 output.open("output.txt");
 input.open("a.txt");
 input>>cas;
 for (int i=0;i<cas;i++)
 {
  con=0;
  input>>a;
  input>>b;
  input>>k;
  for(int y=0;y<a;y++)
  {
   for(int r=0;r<b;r++)
   {
    if((y&r)<k)
    con++;

   }
  }
 output<<"Case #"<<i+1<<": "<<con<<"\n";
 }
}
