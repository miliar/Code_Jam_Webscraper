#include<iostream>
#include<fstream>

using namespace std;
fstream f1,f2;



int main()
{  f1.open("large.in",ios::in);
   f2.open("out.out",ios::out);
   int a[4][4],b[4][4],i,j,count,g1,g2,flag,n=0,num,chose;

   f1>>count;

   while(count)
   {
       n++;
       flag=0;
   count--;
   f1>>g1;

   for(i=0;i<4;i++)
   {
       for(j=0;j<4;j++)
      {

       f1>>a[i][j];

      }
   }
   f1>>g2;

   for(i=0;i<4;i++)
   {
       for(j=0;j<4;j++)
      {

      f1>>b[i][j];


      }
   }
   for(i=0;i<4;i++)
   { num=a[g1-1][i];
       for(j=0;j<4;j++)
       {
         if(num==b[g2-1][j])
        {
         flag++;
         chose=num;

        }

       }
   }

   if(flag==1)
   f2<<"Case #"<<n<<": "<<chose<<"\n";
   else if(flag==0)
   f2<<"Case #"<<n<<": Volunteer cheated!\n";
   else
   f2<<"Case #"<<n<<": Bad magician!\n";
   }
   return 0;
}

