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
#include "fstream"

#define sz(X) ((int)X.size())
#define FOR(i,x,y) for(int i=x; i<y; ++i)
#define FORE(i,x,y) for(int i=x; i<=y; ++i)
char buf[50]; std::string itos(int x) {sprintf(buf,"%d",x); return buf;}

using namespace std;

bool contain(int n, vector<int> &v)
{
    FORE(i, 0, sz(v)) if(n == v[i]) return true;
    return false;
}

int main()
{
    ofstream cout ("output.txt");
    ifstream cin ("input.txt");

    int T;
    cin>>T;

    FOR(i,1,T+1)
    {
        int a1; cin>>a1;
        int n;
        vector<int> v1;
        FORE(i,1,4) FORE(j, 1, 4)
        {
            cin>>n;
            if(i==a1)v1.push_back(n);
        }

        int a2; cin>>a2;
        vector<vector<int> > v2(5, vector<int>());

        FORE(i,1,4) FORE(j, 1, 4)
        {
            cin>>n;
            if(contain(n, v1)) v2[i].push_back(n);
        }

        string ans;
        if(sz(v2[a2]) == 1) ans = itos(v2[a2][0]);
        else if(sz(v2[a2]) == 0) ans = "Volunteer cheated!";
        else ans = "Bad magician!";

        cout<<"Case #"<<i<<": "<<ans<<endl;
    }

    return 0;
}