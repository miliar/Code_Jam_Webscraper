#include<iostream>

using namespace std;

int main()
{  
   int T,k,arr[10]={1,1,1,1,1,1,1,1,1,1};
   int flag=0,j=2,i=1;
   long long int N,temp;
   
   cin >> T;
   
   for(i=1,k=1;i<=T;i++)
   {
      cin >> temp;
      
      N = temp;
      
      if(temp != 0)
      {
         while(flag!=10)
         {
            while(N!=0)
            {
               if(arr[N%10]==k)
               {
                  arr[N%10]++;
                  flag++;
               }
               N = N / 10;
            }
            N = temp * j;
            j++;
         }
         flag=0;
         cout << "Case #" << i << ": " << N-temp << endl;
         j=2;
         k++;
      }
      else
         cout << "Case #" << i<< ": INSOMNIA" << endl;
   }

   return 0;
}
