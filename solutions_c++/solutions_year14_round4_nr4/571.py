
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cstring>
#include <cassert>
using namespace std;

void prework();
void work();

int main(int argc, char *argv[])
{
#if 1
auto t1 = freopen("input.in","r",stdin);
if (t1== nullptr) {
    cerr <<"no file"<<endl;
    return 0;
}
auto t2 = freopen("output.txt","w",stdout);
#endif

    prework();

    int n;
    cin>>n;
    for (int i=0; i<n; i++) {
        cout<<"Case #"<<i+1<<": ";
        work();
        cout<<endl;
    }

    cerr<<"end!!!!!!!!!!"<<endl;

}

void prework() {

}

int calc(vector<string> vs) {
    set<string> sets;
    for (int i=0; i<vs.size(); i++) {
        string s= vs[i];
        for (int j=1; j<= s.size(); j++) {
            sets.insert(s.substr(0,j));
        }
    }
    return sets.size()+1;
}

string ss[100];
int z[100];
void work() {
    int result = 0, total = 0;
    int m,n;
    cin>>m>>n;
    int bbb = 1;
    for (int i=0; i<m; i++) {
        cin>>ss[i];
        bbb*=n;
    }
    cerr<<bbb;
    for (int i=0; i<n; i++) {
    }
    for (int fff = 0; fff<bbb; fff++) {
        vector<string> vs[4];
        int temp = fff;
        for (int i=0; i<m; i++) {
            z[i] = fff % n;
            vs[z[i]].push_back(ss[i]);
            fff/=n;
        }
        fff = temp;
        bool ok = true;
        int re =0;
        for (int i=0; i<n; i++) {
            if (vs[i].size()==0) ok=false;
            re += calc(vs[i]);
        }
        if (!ok) continue;

        if (re == result) {
            total++;
        }
        else if (re > result) {
            result = re; total = 1;
        }
    }
    cout<<result<<' '<<total;

}
