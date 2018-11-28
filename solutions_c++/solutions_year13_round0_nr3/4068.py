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
#define sz(X) ((int)X.size())
#define FOR(i,x,y) for(int i=x; i<y; ++i)
#define EPS 1e-10
using namespace std;

bool pal(long long n)
{
    stringstream ss;
    ss<<n;
    string s = ss.str();
    string rs = s;
    reverse(rs.begin(), rs.end());
    if(sz(s)==sz(rs))
    return s == rs;
    return false;
}
int main()
{
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");

    vector<long long> sp;
    int T;
    cin>>T;
    long long tA=1,tB=1e7;
    for(long long n = tA; n<=tB; ++n)
        if(pal(n) && pal(n*n))sp.push_back(n*n);
    
    FOR(i,1,T+1)
    {
        long long A,B;
        cin>>A>>B;

        int ans = 0;

        FOR(i,0,sz(sp))
        if(sp[i]>=A && sp[i]<=B)++ans;
        
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}