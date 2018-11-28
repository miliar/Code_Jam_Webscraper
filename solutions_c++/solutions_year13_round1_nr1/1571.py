#include<iostream>
#include<algorithm>
#include<cstdio>
#define pi 3.142857143
using namespace std;
int main()
{
  int tests;
  cin >> tests;
  for(int t=1;t<=tests;t++)
  {
    long long int r,p;
    cin>>r>>p;
    long long int cur=r;
    long long int c = 0;
    while(p>= ((cur+1)*(cur+1) - (cur*cur)))
    {
      c++;
      p-= ((cur+1)*(cur+1) - (cur*cur));
      cur+=2;
    }
    printf("Case #%d: %lld\n",t,c);
  }
}