#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define FOR(a,b,c) for(int (a)=(b);(a)<(c);(a)++)
#define sor(a) sort((a).begin(),(a).end())
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(),(a).end()

bool pal(long long a){
    stringstream ss;
    ss << a;
    string ret = ss.str();
    for(int i=0;i<sz(ret)/2;i++)
        if(ret[i] != ret[sz(ret)-1-i])
            return false;
    return true;
}

void bruteforce(vector<string> &s , string x){
    //cout << sz(x) << endl;
    if(sz(x) >= 8 ){
        s.pb(x);
        return;
    }
    bruteforce(s,x+"0");
    bruteforce(s,x+"1");
    bruteforce(s,x+"2");
}
long long parse(string x){
    long long ret = 0LL;
    FOR(i,0,sz(x))
        ret = ret*10LL + (x[i]-'0');
    return ret;
}
void precompute(vector<long long> &v){
    vector<string> strings;
    bruteforce(strings , "");
    FOR(i,0,sz(strings)){
        long long val = parse(strings[i]);
        if(pal(val) && pal(val*val))
            v.pb(val*val);
    }

}
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);

    int t;

    vector<long long> values;
    precompute(values);
    values.pb(9);
    cin >> t;

    FOR(tc,1,t+1){
        long long a,b;
        cin >> a >> b;
        cout << "Case #" << tc << ": ";

        int ret=0;
        FOR(i,0,sz(values))
            if(values[i] >= a && values[i] <= b)
                ret++;
        cout << ret << endl;
    }
}
