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
typedef long long ll;
using namespace std;

int main(){
    //freopen("pd.in","r",stdin);
    //freopen("pd.out","w",stdout);
    int i,j,k,t,tt;
    cin >> tt;
    xrep(t,1,tt+1){
    	//cout << "Case " << t << ":";
        int n, cap, back, ans(0);
        vector<int> in;
        cin >> n >> cap;
        rep(i,n) {
            int temp;
            cin >> temp;
            in.push_back(temp);
        }
        vector<int> used(n);
        sort(in.begin(),in.end());
        back = n;
        rep(i,in.size()) {
            if (!used[i]) {
                used[i] = 1;
                int xx = cap - in[i];
                back--;
                while ( back > i && in[back] > xx) {
                    back--;
                }
                if ( back > i && !used[back]) {
                    used[back] = 1;
                }
                ans++;
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
}

