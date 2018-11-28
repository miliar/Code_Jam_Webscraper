#include <iostream>
#include<fstream>
using namespace std;

int main()
{
   ifstream in;
   ofstream out;
   in.open("input.txt");
   out.open("output.txt");
   while(in.good())
   {

    int test,i=0,r1,r2,c=0,num;
    int arr[4][4];
    int arr2[4][4];
    in>>test;
    while(i<test)
    {
        in>>r1;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
                in>>arr[j][k];
        }
        in>>r2;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
                in>>arr2[j][k];
        }
          for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
             {

                 if(arr[r1-1][j]==arr2[r2-1][k])
                {

                c++;

                num=arr[r1-1][j];

        }
             }
        }
        if(c==1)
           out<<"Case #"<<i+1<<": "<<num<<"\n";
        else{
                if(c==0)
                out<<"Case #"<<i+1<<": "<<"Volunteer cheated!\n";
            else
                out<<"Case #"<<i+1<<": "<<"Bad magician!\n";

        }
        c=0;
        i++;
    }
    in.close();
   out.close();
   }

    return 0;
}
