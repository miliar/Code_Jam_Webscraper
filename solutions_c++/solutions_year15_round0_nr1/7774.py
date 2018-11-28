#include<iostream>
#include<stdio.h>

using namespace std;
char A[1005];
int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t,s,d,f;
  cin>>t;
  for(int k=1; k<=t; k++)
  {
    d = f = 0;
    cin>>s;
    cin>>A;
    for(int i=0; i<=s; i++)
    {
      int x = A[i] - '0';
      if(!x)
        continue;
      else
      {
        if(d>=i){
          d += x;
        }
        else
        {
          f += i-d;
          d = i+x;
        }
      }
    }

    printf("Case #%d: %d\n", k, f);
  }

  return 0;
}
