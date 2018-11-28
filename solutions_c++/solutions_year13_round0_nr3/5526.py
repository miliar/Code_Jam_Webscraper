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
//#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int ip(int a)
{
    int f = 1;
    vector<int>v;
    while(a !=0)
    {
        v.push_back(a%10);
        a = a/10;
    }
    int n = v.size();
    for(int i = 0; i < n/2; i++)
    {
        if(v[i] != v[n-i-1]){
            f = 0;
            break;
        }
    }
    return f;
}
int main()
{
    int t,k=1;
    freopen("a.in","r",stdin);
    freopen("b.txt","w",stdout);
    cin>>t;
    while(k <= t)
    {

        int n = 0;
        int a,b,p;
        cin>>a>>b;
        for(int i = a; i <= b; i++)
        {
            p = (int)sqrt(i);
            if(p*p == i)
            {
                if(ip(p)&&ip(i))
                    n++;
            }
        }
        printf("Case #%d: %d\n",k,n);
        k++;
    }
}
