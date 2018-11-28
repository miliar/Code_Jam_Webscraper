#include <iostream>
#include <cstring>


using namespace std;

int main()
{
 int tcase;
 
 
 // Read the test case
  cin >> tcase;
  for (int i=0 ; i < tcase ; i++)
  {
    int buffer[6], lt, sum=0, ans=0;
    string str;

     cin >> lt;
     cin >> str;
    
     for (int j=0; j < lt; j++)
     {
     buffer[j] = str[j]-48;
     sum += buffer[j];
     if (sum < (j + 1)) 
     {ans +=  (j+1-sum); sum = j +1;}
     }
     cout << "Case #" << i+1 << ": "  << ans << endl;
  }
  
   return 0;
}

