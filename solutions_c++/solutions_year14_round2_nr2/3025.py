#include <iostream>
#include <fstream>

//#define unsigned long long lint;
using namespace std;

int  main()
{
    int test,a,b,k;
    int count = 0,c=0,maxab,minab;
    static int arr [1000][1000];
    ifstream myfile;
    ofstream ans;

    ans.open("ans.txt");
    myfile.open("A-small-attempt0.in");
    if (myfile.is_open())
      {
       myfile>>test;
       //test=2;
       while(test--)
       {
           //cout<<"\ntest"<<test<<"\n";
           for(int i=0; i<1000 ; i++)
           {
               for(int j= 0; j <1000; j++)
               {
                   arr[i][j]=0;
               }
           }

           count = 0;
           c++;
           myfile>>a>>b>>k;
           maxab = a<b ? b : a;
           minab = a<b ? a : b;
           for(int i=0; i<minab ; i++)
           {
               for(int j= 0; j <maxab; j++)
               {
                   if((i&j)<k && arr[i][j] != 1)
                   {
                    count++;
                    arr[i][j]=1;
                    if(i != j && j< minab && arr[j][i] !=1)
                    {
                        arr[j][i]=1;
                        count++;
                    }
                    //cout<<i<<" "<<j<<"\n";
                   }

               }
           }





           ans<<"Case #"<<c<<": "<<count<<"\n";


       }

      }

    myfile.close();
    ans.close();

    return 0;
}
