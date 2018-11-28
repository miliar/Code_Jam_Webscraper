
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
int pal(int n)
        {
         int r,temp=n,sum=0;
         while(temp){
             r=temp%10;
             temp=temp/10;
             sum=sum*10+r;
          }
         if(n==sum)
           return 1;
         else
           return 0;
        }

bool is_perfect_square(int n) {
    if (n < 0)
        return false;
    int root(round(sqrt(n)));
    return n == root * root;
}
int main()
{    
     
     int t;
     cin>>t;
     int a,i,k,j,b,c=0;
     for(j=0;j<t;j++)
     {
      c=0;
      cin>>a>>b;
      for(i=a;i<=b;i++)
       {
         k=sqrt(i);
         if(pal(i)==1&&is_perfect_square(i)&&pal(k)==1)
           c++;
       }
      cout<<"Case #"<<j+1<<":"<<" "<<c<<endl; 
     }
    return 0;
}   