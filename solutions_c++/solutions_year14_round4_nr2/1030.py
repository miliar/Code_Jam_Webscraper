#include<iostream>
#include<sstream>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<queue>
#include<stack>
#define INF (1<<29)
#define EPS (1e-10)
#define two(a) (1<<(a))
#define rep(a,b) for(a=0 ; a<b ; ++a)
#define xrep(a,b,c) for(a=b ; a<c ; ++a)
#define sca(t) scanf("%d",&t)
#define scal(t) scanf("%lld",&t)
#define min(a,b) ((a) < (b) ? (a) : (b))
typedef long long ll;
using namespace std;


int main(){
    //freopen("pd.in","r",stdin);
    //freopen("pd.out","w",stdout);
    int i,j,k,t,tt,n;
    cin >> tt;
    xrep(t,1,tt+1){
    	//cout << "Case #" << t << ":";
        cin >> n;
        int ans = (0);
        vector<int> in(n);
        rep(i,n) cin >> in[i];
        vector<int> temp(n);
        rep(i,n) temp[i] = in[i];
        sort(temp.begin(),temp.end());
        rep(i,n) {
            int now = temp[i];
            int index(INF);
            rep(j,n) {
                if (in[j] == now) {
                    index = j;
                    break;
                }
            }
            ans += min(j, in.size() - j - 1);
            in.erase(in.begin() + j);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
}

