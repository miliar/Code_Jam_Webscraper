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
int ip(long long int a)
{
    int f = 1;
    int v[20];
    int n = 0;
    while(a !=0)
    {
        v[n]=(a%10);
        a = a/10;
        n++;
    }

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
    int t,k=1,n=0;
    freopen("s.in","r",stdin);
    freopen("c.txt","w",stdout);
    cin>>t;
    long long int ar[1000],p;
    for( long long int i = 1;i*i <= 100000000000000; i++)
        {
            p = i*i;
                if(ip(i)&&ip(p)){
                    ar[n] = p;
                    n++;
                }
        }
    while(k <= t)
    {
        long long int a,b;
        int c=0;
        cin>>a>>b;
        for(int i = 0; i < n; i++)
        {
            if(ar[i] > b)break;
            if(ar[i]>= a)c++;
        }
        //i = (long long int)sqrt(a);
        //if(i*i != a)i++;

        printf("Case #%d: %d\n",k,c);
        k++;
    }
}
