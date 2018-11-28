#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <utility>
#include <functional>
#include <string>
#include <algorithm>

#include <cstring>
#include <cstdio>
#include <memory.h>
#include <ctime>
#include <cassert>
#include <cmath>
#include <iomanip>

#define eps e-8

using namespace std;
#define forn(i,n) for(int i = 0; i < int(n); i++)
#define ll long long int
//#define INF 1000000000
int cnt =0;
void solve() {
    int t;
    cin>>t;
    forn(i, t) {
        cnt=0;
        cout<<"Case #"<<i+1<<":"<<" ";
        string im("INSOMNIA");
        int n, m=0;
        cin>>n;
        set<int> st;
        do {
            m+=n;
            int cm = m;
            while(cm!=0) {
                st.insert(cm%10);
                cm=cm/10;
            }
            cnt++;
            if(cnt>500){
                m=-1;
                break;
            }
        } while(st.size()!=10);
        if(m==-1)
            cout<<im<<endl;
        else
            cout<<m<<endl;
    }
    
}

int main()
{
    /*ll t =1000000000000111L;
    cout<<t<<" "<<t%11<<endl;
    cout<<t%7<<endl;
    ll p = numeric_limits<ll>::max();
    cout<<p<<endl;*/
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
#ifdef diametralis
    freopen("/Users/diametralis/Documents/projects/IO/input.txt", "rt", stdin);
    freopen("/Users/diametralis/Documents/projects/IO/output.txt", "wt", stdout);
#endif
    solve();
#ifdef diametralis
    cerr << "Time == " << clock() << endl;
#endif
}