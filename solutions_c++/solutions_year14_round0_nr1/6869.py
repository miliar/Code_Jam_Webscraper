#include <iostream>

using namespace std;

int main()
{
   int array1[4][4];
   int array2[4][4];
   int choice1, choice2;
   int testCaseCount = 0, i = 0, j, k;
   
   cin >> testCaseCount;
   for(i = 0; i < testCaseCount ; i++)
   {
       int pick = -1;
       cin >> choice1;
       for(j=0; j < 4; j++)
       {
           for(k=0; k < 4; k++)
           {
               cin >> array1[j][k];
           }
       }
       cin>>choice2;
       
       for(j=0; j < 4; j++)
       {
           for(k=0; k<4; k++)
           {
               cin>>array2[j][k];
               
           }
           
       }
       
       for(j=0; j < 4; j++)
       {
           for(k=0;k<4; k++)
           {
               if(array1[choice1-1][j] == array2[choice2-1][k])
               {
                   if(pick == -1)
                   {
                       pick = array1[choice1-1][j];
                   }
                   else if(pick != -2)
                   {
                       pick = -2;
                       break;
                   }
               }
           }
       }
       
       cout <<"Case #" <<i+1 <<": ";
       if(pick == -1)
       {
           cout << "Volunteer cheated!" << endl;
       }
       else if(pick == -2)
       {
           cout << "Bad magician!" << endl;
           
       }
       else
       {
           cout <<pick << endl;
       }
   }
   return 0;
}