#include <vector>
#include <stdio.h>
#include <string.h>
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
typedef long long ll;
//typedef long double d;
using namespace std;

int main()
{
    //std::cin.tie(0);
    //std::ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ll t;
    cin >> t;
    for(int q=0; q<t; q++)
    {
        ll n,sum=0;
        set<ll> se;
        cin >> n;
        bool ok=0;
        for(int i =0; i<1e6; i++)
        {
            sum+=n;
            ll temp=sum;
            while(temp)
            {
                se.insert(temp%10);
                temp/=10;
            }
            if(se.size()==10)
            {
                cout << "Case #"<<q+1<<": "<<sum << endl;
                ok=1;
                break;
            }
        }
        if(!ok)
            cout << "Case #"<<q+1<<": "<<"INSOMNIA"<< endl;
    }
    return 0;
}
