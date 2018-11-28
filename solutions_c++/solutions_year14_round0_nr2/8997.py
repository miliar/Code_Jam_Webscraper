#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>


using namespace std;
int main()
{
    fstream fin, fout;
     int test,i,j;
    double directtime,currenttime,currentrate,min,maxtime,mintime,rate,max,x,sample;

     fin.open("input.txt",ios::in);
    fout.open("output.txt",ios::out);

    freopen("output.txt", "w", stdout);

    fin>>test;
      i=0;
   while(test--)
   {  i++;
     j=0;
       fin>>min>>rate>>max;

     currenttime=0;

     directtime=0;

     currentrate=2;

     mintime=max/2;

     while(directtime>=currenttime)
     {
         directtime=currenttime+(max/currentrate);

           x=min/currentrate;

           currenttime+=x;

          currentrate+=rate;

          //printf("dire time==%f and curr time==%f \n",directtime,currenttime);

          if(directtime<=mintime)
          mintime=directtime;

          else
          break;
     }

     cout<<"Case #"<<i<<": ";

	   printf("%0.7lf\n",mintime);

   }

   fout.close();
    return 0;
}
