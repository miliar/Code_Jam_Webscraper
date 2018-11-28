#include <iostream>
using namespace std;

void flipSymbols(int arr[100], int lim)
{
   for (int i=0; i<lim; i++)
      arr[i] ^= 1;
   
   return;
}

int solve(int arr[100], int size)
{
   int n = 0;
      
   for (int i=1; i<size; i++)
   {
      if (arr[i-1] != arr[i])
      {
         flipSymbols(arr, i);
         n++;
      }
   }
   
   if (arr[0] == 0)
      n++;

   return n;
}

int main()
{
   int t, n, size;
   int arr[100];
   string input;

   //read num of testcases
   cin >> t;
   getline(cin, input);

   for (int i=1; i<(t+1); i++)
   {
      n = 0;

      //read test input
      getline(cin, input);
      size = input.length();

      for (int k=0; k<size; k++)
      {
         if(input[k] == '+')
            arr[k] = 1;
         else
            arr[k] = 0;
      }
   
      n = solve(arr, size);
      cout << "Case #" << i << ": " << n << endl;
   }

   return 0;
}
