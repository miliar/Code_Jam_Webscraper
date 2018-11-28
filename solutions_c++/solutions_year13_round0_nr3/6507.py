#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
using namespace std;
int reverse(int num)
{
 int rev = 0,dig=0;
 while (num > 0)
 {
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
 }
 return rev;
}
int main()
{
 int t,i,j,sum=0,a,b,cnt=0;
 cin>>t;
 while(t--)
  {
   cnt++;
   sum=0;
   cin>>a>>b;
   int sqa=ceil(sqrt(a));
   int sqb=floor(sqrt(b));
   for(i=sqa;i<=sqb;i++)
    {
     int s=i*i;
     if(i==reverse(i) && s==reverse(s)){
    sum++;}
    }
   cout<<"Case #"<<cnt<<":"<<" ";
   cout<<sum;
   cout<<"\n";
  }
return 0;
}
   