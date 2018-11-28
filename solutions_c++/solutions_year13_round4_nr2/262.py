#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <map>
using namespace std;


long long ex(int N,long long p)
{
    if(N==0)
        return 0ll;
    long long b = ex(N-1,p/2);
    if(p%2==0)
        return b+b;
    return b+(1ll<<(N-1));
}

long long larg(int N,long long p)
{
    if(p==0)
        return 0;
    if(N==0)
        return 0;

    if(p%2==0)
        return max(larg(N,p-1),ex(N,p));

    long long ans = larg(N-1,p/2);
    return max(ans+ans,ans+(1ll<<(N-1)));
}

int main()
{
    int T;
    cin >> T;
    for(int it=1;it<=T;it++)
    {
        int N;
        long long p;
        cin >> N >> p;
        p--;

        if(p==(1ll<<N)-1)
            cout << "Case #" << it << ": " << p << ' ' << p << endl;
        else
        cout << "Case #" << it << ": " << ((1ll<<N)-1-larg(N,(1ll<<N)-2-p)-1) << ' ' << larg(N,p) << endl;

    }
}
