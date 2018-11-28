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

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    int n,i;
    int a[20];
    char nums[20];
    printf("Case #%d: ", qq);
    scanf("%d %s",&n,nums);
    for(i=0;i<=n;i++)
    {
        a[i]=nums[i]-48;
    }
    int s,r=0;
    int t=0;
    for(s=0;s<=n;s++)
    {
        if(a[s]!=0)
        {
            if(s<=t)
             t=t+a[s];
            else{
            r++;
            a[s-1]=a[s-1]+1;
            t++;
            t=t+a[s];
            }
        }
        else
        {
            if(s>t)
            {
            r++;
            a[s-1]=a[s-1]+1;
            t++;
            }


        }


    }



        printf("%d\n",r);
    }




  return 0;
}
