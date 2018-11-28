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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

long long rev(long long i)
{
    long long inv; inv = 0;
    while (i>0)
    {
        inv = inv * 10 + (i%10);
        i = i / 10;
    }

    return inv;
}

bool isPal(long long i)
{
    if(i == rev(i))
        return true;
    return false;
}

#define small 1000
#define firstlarge 100000000000000L

int main()
{
    int T;
    cin>>T;
    vector<long long> v;
    long long i = 1;
    while(true)
    {
        long long ii = i*i;
        if(ii>firstlarge)
            break;
        if(isPal(i) && isPal(ii))
            v.push_back(ii);
        i++;
    }
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        long long A, B;
        cin>>A>>B;
        int r = 0;
        for(int idx = 0;idx<v.size();idx++)
        {
            if(v[idx]>=A && v[idx]<=B)
                r++;
        }
        cout<<r<<endl;
    }
    return 0;
}
