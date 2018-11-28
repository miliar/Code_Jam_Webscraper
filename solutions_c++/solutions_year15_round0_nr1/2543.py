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

int main()
{
    cin.tie(0);
    std::ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,n;
    string s;
    cin >> t;
    for(int i =0;i<t;i++)
    {
        cin >>n >> s;
        ll sum=0,ans=0;
        for(int k =0;k<s.size();k++)
        {
            if(sum>=k)
            {
                sum+=(s[k]-'0');
            }
            else if(s[k]!=0)
            {
                ans+=(k-sum);
                sum+=(k-sum);
                sum+=(s[k]-'0');
            }
        }
        cout << "Case #"<< i+1<<": "<<ans << endl;
    }
    return 0;
}
