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

int main()
{
    int t,k=1;
    freopen("a.in","r",stdin);
    freopen("bb.txt","w",stdout);
    cin>>t;
    while(k <= t)
    {

        long long int r,n,i;
        cin>>r>>n;
        long long int p=0,sm=0;
        for(i = r+1;sm <= n;i = i+2 )
        {
            sm += i*i-(i-1)*(i-1);
            if(sm <= n)p++;
        }
        printf("Case #%d: %d\n",k,p);
        k++;
    }
}

