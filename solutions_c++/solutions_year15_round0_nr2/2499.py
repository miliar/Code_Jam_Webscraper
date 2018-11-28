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
#include <fstream>
#include <cstdio>
typedef long long ll;
typedef double d;
typedef unsigned long long ull;
using namespace std;
ll ans=10e10;
void eat(vector <ll> v, ll x)
{
    ll counter=0;
    for(int i =0;i<v.size();i++)
    {
        if(v[i]>x)
        {
            v.push_back(v[i]-x);
            v[i]=x;
            counter++;
        }
    }
    ans=min(ans,counter+x);
    return;
}
int main()
{
    cin.tie(0);
    std::ios::sync_with_stdio(false);
    //freopen("D-small-attempt2.in","r",stdin);
    //freopen("out.txt","w",stdout);
    ll t;
    cin >> t;
    for(int i =1;i<t;i++)
    {
        ll z,n;
        vector<ll> v;
        ans=10e10;
        cin >> n;
        for(int k=1;k<n;k++)
        {
            cin >> z;
            v.push_back(z);
        }
        for(int k=1;k<1000;k++)
        {
            eat(v,k);
        }
        cout << ans<< endl;
    }
    return 0;
}
