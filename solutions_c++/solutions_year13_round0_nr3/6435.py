#include "iostream"
#include "math.h"
using namespace std;

int is_pal(long n)
{
  long n1, rev = 0, rem;
  n1 = n;
  while (n > 0)
  {
    rem = n % 10;
    rev = rev * 10 + rem;
    n = n / 10;  
  }
  if (n1 == rev)
  {
    return 1; 
  }
  else
  {
    return 0;   
  }
}
  


int main()
{
  long long A,B;
  float temp;
  int T;
  cin >> T;
  int cnt[T];
  for(int i = 0;i<T;i++)
  {  
    cin >> A >> B;
    cnt[i] =0;
    for(long long x = A;x<=B;x++)
    {
      temp = sqrt(x);
      
      if((int)temp == temp)
      {
          if(is_pal(x)  == 1 && is_pal(temp) ==1)
        {
            cout<<x<<endl;
            cnt[i]++;
        }
      } 
    }  
  }
  for(int i = 0;i<T;i++)
    cout << "Case #"<<i+1<<": "<<cnt[i]<<endl;
  cout<<endl;
  return 0;
  
}
