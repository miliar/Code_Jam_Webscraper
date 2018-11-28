#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>
#include <utility> 
using namespace std;

void solve()
{
   char s[1000];
   int k,index,fm=0,count=0;
   cin>> s>>k;
   int len=strlen(s);
   for(int i=0;i<len;i++)
   {
       if(s[i]=='-')
       {
           fm=1;
           index=i;
           if((index+k-1)<len)
           {
               count++;
               for(int j=0;j<k;j++)
               {
                   if(s[index]=='+')
                   {
                       s[index]='-';
                       fm=1;
                   }
                   else
                   {
                       s[index]='+';
                       fm=0;
                   }
                   index++;
               }
           }
       }
   }
   if(fm==0)
   {
       cout<<count<<endl;
   }
   else
   {
       cout<<"IMPOSSIBLE"<<endl;
   }
}
int main() 
{
    int t;
    cin >>t;
    for(int i=1;i<=t;i++)
    {
        cout << "Case #"<<i<<": ";
        solve();
    }
	return 0;
}

