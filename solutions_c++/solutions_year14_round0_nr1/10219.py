#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;
int main ()
{
   int cases , choice1 , choice2;
   ifstream in("A-small-attempt0.in");
   ofstream out("google.txt");
   in>>cases; // read lal 3
   //cout<<cases<<endl;
   int temp; // 7ata nqra2 al satre as integers
   string row; // meshan al getline
   int a[2][4]; // to contain the tow rows
    //getline(in , row);
   for ( int r=1 ; r<=cases ; r++)
   {
      in>>choice1;
      getline(in , row);
      //cout<<choice1<<endl;
      for ( int j=0;j<choice1-1 ; j++)
         getline(in , row);
         for(int kl=0;kl<4;kl++)
            in>>a[0][kl];
         getline(in , row);
         for(int j=0;j<4-choice1;j++)
            getline(in , row);
         in>>choice2;
         getline(in,row);

   for ( int j=0;j<choice2 -1; j++)
         getline(in , row);
         for(int kl=0;kl<4;kl++)
            in>>a[1][kl];
            getline(in , row);
         for(int j=0;j<4-choice2;j++)
            getline(in , row);

   int c=0; // lm3rafet 3adad al arqaam al motakarera
   int choice; // al raqam ele e5taro
for ( int i=0 ; i<4 ; i++)
{
for ( int j=0 ; j<4 ; j++)
{
   if (a[0][i]==a[1][j])
   {
      choice=a[0][i];
      c++;
   }
}
}
   if (c==1)
      out<<"Case #"<< r <<": " <<choice<<endl;
      else
         if(c==0)
         out<<"Case #"<< r <<": Volunteer cheated!\n";
      else
         out<<"Case #"<< r <<": Bad magician!\n";
}// for cases

//   return 0;

   }// main


