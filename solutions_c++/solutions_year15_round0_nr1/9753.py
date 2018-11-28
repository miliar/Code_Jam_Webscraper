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
using namespace std;
int main()
{
 // freopen("in", "r", stdin);
  //freopen("out", "w", stdout);
int sum=0,t,n,count;
char a[1002];
cin>>t;
for(int j=0;j<t;j++)
{
  count=0;
  sum=0;
  cin>>n;
  cin>>a;
  for(int i=0;a[i]!='\0';i++)
   {
    if(a[i]=='0')
      continue;
    else {
     if(sum<i)
      {count+=(i-sum);sum+=count;}
    sum+=(a[i]-'0');
   }
  }
  cout<<"Case #"<<j+1<<": "<<count<<endl;
}
return 0;
}
