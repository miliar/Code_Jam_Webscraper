#include<bits/stdc++.h>
#define MAX 10000
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define ellapse printf("Time : %0.3lf\n",clock()*1.0/CLOCKS_PER_SEC);
using namespace std;
/*
//E,SE,S,SW,W,NW,N,NE
int dr[8]={0,1,1,1,0,-1,-1,-1};
int dc[8]={1,1,0,-1,-1,-1,0,1};
*/
typedef long long l64d;
typedef unsigned long int ud;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
vector<int> ok;
bool seen[15] = {};
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    //std::ios::sync_with_stdio(false);
    int t;
    l64d res,tmp;
    l64d n;
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        ok.clear();
        memset(seen, 0 , sizeof seen);
        scanf("%lld",&n);
        printf("Case #%d: ", (i+1));
        if(!n) printf("INSOMNIA\n");
        else {
            int ind = 1;
            while(ok.size() != 10) {
                tmp = n * ind;
                res = tmp;
                while(tmp) {
                    int sat = tmp % 10;
                    if(!seen[sat]) {
                        seen[sat] = 1;
                        ok.pb(sat);
                    }
                    tmp /= 10;
                }
                ind++;
            }
            if(ok.size() == 10) {
                printf("%lld\n", res);
            }
        }
    }

    #ifdef Xanxiver
    ellapse;
    #endif // Xanxiver
}
