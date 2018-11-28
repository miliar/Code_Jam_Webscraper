#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<iomanip>
#include<fstream>

#include<string>
#include<utility>
#include<vector>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>

#define ii long long int
#define pi 2*acos(0.0)
#define eps 1e-9
#define mem(x,y) memset(x,y,sizeof(x))
#define all(x) x.begin(), x.end()
#define pb push_back
#define sz(a) (int)a.size()
#define inf 2147483640
#define mx 100010

using namespace std;

const int debug= 0;
vector <string> v;
string curr;

ii power(ii base,ii pow) {
    if (!pow) return 1;
    ii res=power(base,pow>>1);
    res*=res;
    if (pow&1) res*=base;
    return res;
}

ii fromAto10(ii a,string n) {
    ii ans=0;
    int sz= sz(n);
    for (int i=sz-1;i>=0;--i) {
        ans+= (n[i]-'0')*power(a,sz-i-1);
    }
    return ans;
}

ii firstDiv(ii n) {
    ii sqr= sqrt(n);
    for (int i=2;i<=sqr;++i) {
        if (n%i==0)
            return i;
    }
    return -1;
}

void gen(int pos) {
    if (!pos){
        v.pb(curr);
        return;
    }
    curr[pos]='0';
    gen(pos-1);
    curr[pos]='1';
    gen(pos-1);
}

int main() {
    //freopen("in.txt","r",stdin);
    if (!debug) freopen("out.txt","w",stdout);

    puts("Case #1:");
    int i,cnt=0;
    for (i=1;i<=16;++i) curr.push_back('1');
    gen(14);
    int sz=sz(v);
    if (debug) sz=sz(v);
    for (i=0;i<sz;++i) {
        if (debug) fprintf(stderr,"%s\n",v[i].c_str());
        string s=v[i];
        vector <ii> divs;
        for (int j=2;j<=10;++j) {
            ii num=fromAto10(j,s);
            ii div=firstDiv(num);
            if (debug) cout<<j<<" - "<<num<<" - "<<div<<endl;
            if (div==-1) break;
            divs.pb(div);
        }
        if (sz(divs)<9) continue;
        cout<<s;
        for (int j=0;j<9;++j) cout<<" "<<divs[j];
        puts("");
        cnt++;
        //fprintf(stderr,"cnt %d\n",cnt);
        if (cnt==50) break;
    }
    //cout<<"cnt: "<<cnt<<endl;

    return 0;
}
