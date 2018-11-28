#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>

#define REP(i,n) for(int i=0;i<(n);i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int tot, a[5];
vector<string> f[5], s, sq;
set<string> mp;

void gao(int lst, int d, int D) {
    if (d==D) {
        a[d]=25;
        string tmp="";
        REP(i,d) {
            tmp+="1";
            REP(j,a[i+1]-a[i]-1) tmp+="0";
        }
        f[d].PB(tmp);
        //cout<<tmp<<endl;
        return;
    }
    for (int i=lst+1; i<25; ++i) {
        a[d]=i;
        gao(i, d+1, D);
    }
}

void add(string st, string c) {
    string x=st;
    reverse(ALL(x));
    st+=c;
    st+=x;
    s.PB(st);
}

bool cmp(string sa, string sb) {
    if (sa.length() == sb.length()) return sa < sb;
    else return sa.length() < sb.length();
}

string sqr(string st) {
    int x[300]={0}, l=st.length()*2-1;
    REP(i,st.length()) REP(j,st.length()) x[i+j]+=(int)(st[i]-'0')*(st[j]-'0');
    REP(i,l) if (x[i]>9) {
        x[i+1]+=x[i]/10;
        x[i]%=10;
    }
    while (x[l]>0) {
        x[l+1]+=x[l]/10;
        x[l]%=10;
        ++l;
    }
    string ret="";
    for (int i=l-1; i>=0; --i) ret+=x[i]+'0';
    return ret;
}

bool check(string st) {
    int l=st.length();
    REP(i,l/2) if (st[i]!=st[l-1-i]) return false;
    return true;
}

void gen() {
    s.PB("1");
    s.PB("2");
    s.PB("3");
    string tmp="";
    REP(i,49) {
        string x="2";
        x+=tmp;
        x+="2";
        tmp+="0";
        s.PB(x);
    }
    for (int i=1; i<=4; ++i) {
        gao(-1, 0, i);
    }
    for (int i=1; i<=4; ++i) {
        for (int j=0; j<f[i].size(); ++j) {
            add(f[i][j], "");
            add(f[i][j], "0");
            add(f[i][j], "1");
            if (i<=2) add(f[i][j], "2");
        }
    }
    sort(ALL(s), cmp);
    TR(it,s) {
        string x=sqr(*it);
        sq.PB(x);
        mp.insert(x);
    }
/*
    freopen("C_list.txt", "w", stdout);
    REP(i, s.size()) {
        cout<<s[i]<<" "<<sq[i]<<endl;
    }
    REP(i, s.size()) {
        assert(check(s[i])&&check(sq[i]));
    }*/
}

int calc(string x) {
    int st=0, ed=sq.size()-1;
    while (st<=ed) {
        int mid=st+ed>>1;
        if (cmp(sq[mid],x) || sq[mid]==x) {
            st=mid+1;
        } else ed=mid-1;
    }
    return st;
}

void solve() {
    string A, B;
    cin>>A>>B;
    int ans=calc(B)-calc(A);
    if (mp.count(A)) ++ans;
    cout<<ans<<endl;
}

int main() {
    gen();
//	freopen("C.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
    int cas;
	cin>>cas;
    for (int i=1; i<=cas; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
