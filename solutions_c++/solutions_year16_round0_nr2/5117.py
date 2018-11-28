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
#define pos 0
#define neg 1

using namespace std;

const int debug= 0;
bool a[mx];

int call(int i,bool prev) {
    if (i<0) return 0;
    int ans= (a[i]==prev)?0:1;
    return call(i-1,a[i])+ans;
}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int x=1;x<=t;++x) {
        char s[mx];
        scanf("%s",s);
        int n= strlen(s);
        for (int i=0;i<n;++i) {
            if (s[i]=='+') a[i]=pos;
            else a[i]=neg;
        }
        printf("Case #%d: %d\n",x,call(n-1,pos));
    }

    return 0;
}
