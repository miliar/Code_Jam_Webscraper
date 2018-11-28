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
#define base '0'

using namespace std;

const int debug= 0;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int x=1;x<=t;++x) {
        int n,clapping=0,need=0,i;
        string s;
        cin>>n>>s;
        clapping=s[0]-base;
        for (i=1;s[i];++i) {
            if (s[i]==base) continue;
            if (clapping<i) need+= i-clapping,clapping+=need;
            clapping+=s[i]-base;
        }
        printf("Case #%d: %d\n",x,need);
    }

    return 0;
}
