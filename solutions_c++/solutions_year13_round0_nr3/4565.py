#include <vector>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <fstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define f(i,a,b) for(int i=a;i<b;i++)
using namespace std;
int pali(int n);
int main()
{
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
   int te;
   in>>te;
   int cas=1;
   while(te--)
   {
              int n,m;
              in>>n>>m;
              int sum=0;
              f(i,n,(m+1))         
              {
                                   float x=sqrt(i);
                                   if(x!=(int)x) 
                                   continue;
                                   
                                   else
                                   {
                                       int y=(int) x;
                                       if((pali(i)==1)&&(pali(y)==1))
                                       sum++;
                                   }
              }
              out<<"Case #"<<cas<<": "<<sum<<"\n";
              cas++;
   }
return 0;
}
int pali(int n)
{
    if(n<10) return 1;
    char arr[20];
    sprintf(arr,"%d",n);
    int x=strlen(arr);
    int i=0,j=x-1;
    while(i<j)
    {
              if(arr[i]!=arr[j]) return 0;
              i++;
              j--;
    }
    
    
    
    
    return 1;    
}
