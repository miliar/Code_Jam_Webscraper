
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

void work() {
    int n;
    int z[2000];
    int z1[2000];
    int l[2000],r[2000];
    cin>>n;
    for (int i=0; i<n; i++) {
        cin>>z[i];
    }
    memcpy(z1,z,sizeof(z));
    memset(l,0,sizeof(l));
    memset(r,0,sizeof(l));
    sort(z1,z1+n);

    int re = 0;
    for (int i=0; i<n; i++) {
        int x = 0;
        for (x=0; x<n; x++) if (z[x] == z1[n-i-1]) break;
        if (l[x]<r[x]) re+=l[x];
        else re+=r[x];
        int y;
        y= x+1;
        while (y<n) {
            l[y]++;
            y++;
        }
        y= x-1;
        while (y>=0) {
            r[y]++;
            y--;
        }
    }
    cout<<re;
    cerr<<re;
}
