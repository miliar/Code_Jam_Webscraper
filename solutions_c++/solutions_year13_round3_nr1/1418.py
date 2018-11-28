#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#include <cctype>
#include <list>

#define INF 2000000000
#define ll long long
#define PI 3.1415926535897932384626433832795
#define all(a) a.begin(), a.end()
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define y1 olololo1
#define y0 olololo2
#define m0(a) memset(a,0,sizeof(a))

using namespace std;

int test, n, cnt[1000001];
string t;
bool vowel(char sim){
    return (sim =='a' ||sim =='e' ||sim =='i' ||sim =='o' || sim =='u' );
}
ll ans=0;
ll f(ll cnt){
    return cnt-n+1;
}


int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> test;
    for (int it=0;it<test;++it){
        cin >> t >> n;
        int dl=(int)t.length();
        memset(cnt,0,sizeof(cnt));
        for (int i=0;i<dl;++i){
            if (vowel(t[i])) cnt[i]=0;
            else {
                if (i>0) cnt[i]=cnt[i-1];
                if (!vowel(t[i]))++cnt[i];
            }
        }
        ans=0;
        for (int i=0;i<dl;++i)
            for (int j=i;j<dl;++j){
                bool ok=false;
                int cur=0;
                for (int q=i;q<=j;++q){
                    if (vowel(t[q])) cur=0;
                    else ++cur;
                    if (cur>=n){
                        ok=1;
                        break;
                    }
                }
                ans+=ok;
            }
        cout << "Case #"<<it+1<<": " << ans << endl;
    }
    return 0;
    
}