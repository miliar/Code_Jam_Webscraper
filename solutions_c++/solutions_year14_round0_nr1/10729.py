#include <iostream>
using namespace std;
#define SIZE 4

int main()
{
   int T; //test cases
   int firstSlot;
   int secondSlot;
   int dummy[SIZE];
   int firstArr[SIZE];
   int secondArr[SIZE];
   cin>>T;
   for(int i = 0; i < T; i++)
   {
        bool map[SIZE*SIZE]={false};
        int count = 0;
        int val = 0;
       cin>>firstSlot;
       for(int j = 1; j <= SIZE; j++)
       {
           if(j == firstSlot)
           {
               for(int k = 0; k < SIZE; k++)
               {
                   cin>>firstArr[k];
               }
           }
           else
           {
               for(int k = 0; k < SIZE; k++)
               {
                   cin>>dummy[k];
               }
           }
       }
       cin>>secondSlot;
       for(int j = 1; j <= SIZE; j++)
       {
           if(j == secondSlot)
           {
               for(int k = 0; k < SIZE; k++)
               {
                   cin>>secondArr[k];
               }
           }
           else
           {
               for(int k = 0; k < SIZE; k++)
               {
                   cin>>dummy[k];
               }
           }
       }
       for(int j = 0; j < SIZE; j++)
       {
           map[firstArr[j]-1]=true;
       }
       for(int j = 0; j < SIZE; j++)
       {
           if(map[secondArr[j]-1]==true)
           {
               val = secondArr[j];
                count++;
           }
       }
       if(count == 1)
       {
           cout<<"Case #"<<i+1<<": "<<val<<endl;
       }
       else if(count > 1)
        {
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }
        else if(count == 0)
        {
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }
       
   }
   return 0;
}

