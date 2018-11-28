#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
#include <cctype>

using namespace std;
long long MAX=10000000;

long long a,b;
vector<long long> v;
bool check(long long k)
{
    vector<int> v1;
    while(k)
    {
        v1.push_back(k%10);
        k/=10;
    }
    for(int i=0,j=v1.size()-1;i<j;i++,j--)
        if(v1[i]!=v1[j])
         return 0;

    return 1;
}

int get_index(long long k)
{
    int s=0;
    int e=v.size();

    while(s<e)
    {

        int mid=(e+s)/2;
        //cout<<v[s]<<" "<<v[mid]<<" "<<v[e]<<endl;
        if(v[mid]<k)
            s=mid+1;
        else
            e=mid;
    }
    return s;
}
int main()
{
  freopen("2.in","r",stdin);

  freopen("3.out","w",stdout);
  int tc;
  scanf("%d ",&tc);
  for(long long i=1;i<=MAX;i++)
  {
      v.push_back(i*i);
  }

  for(int ic=1;ic<=tc;ic++)
  {
      scanf("%lld %lld ",&a,&b);
      //cout<<a<<" "<<b<<endl;
      int in=get_index(a);
      int c=0;
      for(int i=in;v[i]<=b;i++)
      {
          //cout<<v[i]<<" ";
          if(check(v[i]) && check((long long)(sqrt(v[i]))) )
          {
              c++;
          }
      }

      printf("Case #%d: %d\n",ic,c);
  }


}

