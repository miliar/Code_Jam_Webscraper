  /*  
    name : Adarsh K                    
    mail : aadarshkarthikeyan@gmail.com  || adarshkarthikeyan@outlook.com                 
  */

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // freopen("in.txt", "r", stdin);                 // for giving input as file  (in.txt)
    // freopen("out.txt", "w", stdout);               // for saving output to file (out.txt)
	long long T,N,t,i,n,flag,f,j,dig,a[10];
  for(cin >> T,t = 1; t <= T; t++)
  {
    flag = 1;
    f = 0;
    cin >> N;
    for(i = 0; i < 10; i++)
      a[i] = 0;
    for(i = 1; ; i++)
    {
      n = i*N;
      if(n == 0)
      {
        flag = 0;
        break;
      }
      while(n > 0)
      {
        dig = n%10;
        n /= 10;
        a[dig] = 1;
      }
      for(j = 0; j < 10; j++)
      {
        if(a[j] == 0)
          break;
        if(j == 9 && a[j] != 0)
        {
          f = 1;
          break;
        }
      }
      if( f == 1)
        break;

    }
    if(flag == 0)
      cout << "Case #" << t << ": INSOMNIA" << endl;
    else
      cout << "Case #" << t << ": " << i*N << endl;
  }
	
  return 0; 
}

