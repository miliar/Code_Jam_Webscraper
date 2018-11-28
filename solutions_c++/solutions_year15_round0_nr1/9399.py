#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<stack>
#include<queue>
#include<deque>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<ctime>
#include<limits>
#include<iomanip>
#include<cstdlib>
#include<list>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>

#define MAXIMUM ( 1 << 31 ) - 1
#define MINIMUM ( 1 << 31 )
#define pb push_back
#define endl '\n'

typedef long long ll;
using namespace std;

int main()
{
    int t;
    cin>>t;
    for (int tt=1;tt<=t;tt++)
    {
        int n;
        string a;
        cin>>n>>a;
        int ab=0,ans=0;
        for(int i=0;i<a.length();i++)
        {
            if (ab>=i and a[i]>'0')
            {
                ab=ab+a[i]-'0';
            }
            else if (a[i]>'0')
            {
                ans=ans+i-ab;
                ab=i+a[i]-'0';
            }
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
        
    return 0;
}
