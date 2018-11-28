#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

int main()
{   freopen("D-large.in", "r", stdin);
    freopen("result.txt", "w", stdout);
    int T,c1,c2,k;
    scanf("%d",&T);
    int i,j,N;
    for(i=1;i<T+1;i++)
    {
    scanf("%d",&N);
    double tp;
    vector<double>ar1,ar2;
    for(j=0;j<N;j++)
        {scanf("%lf",&tp);
        ar1.push_back(tp);
        }
    for(j=0;j<N;j++)
    {   scanf("%lf",&tp);
        ar2.push_back(tp);
    }sort(ar1.begin(),ar1.end());
      sort(ar2.begin(),ar2.end());
        j=0;
        c2=0;c1=N;k=0;
        while(j<N && k<N)
        {
            if(ar1[j]<ar2[k])
                {c1--;j++;k++;}
            else
                k++;
        }
        j=N-1;k=N-1;
        while(k>=0 && j>=0)
        {
            if(ar1[j]>ar2[k])
            {
                c2++;j--;k--;
            }
            else
            {
                k--;
            }
        }
        printf("Case #%d: %d %d\n",i,c2,c1);
    }

    }
