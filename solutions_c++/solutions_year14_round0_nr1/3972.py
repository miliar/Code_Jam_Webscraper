#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stack>
#include <queue>
#include <vector>
#include <utility>
#include <string>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
#include <memory.h>
#include <functional>
#include <numeric>
#include<time.h>
using namespace std;


//For Define
#define forstl(i,s) for(__typeof((s).end()) i=(s).begin(); i != (s).end(); i++)

#define ff first
#define se second
#define mkp make_pair
#define pb push_back
#define sz(a) ((int)a.size())
#define ms(a,n) memset(a, n, sizeof(a))
#define ms0(a) ms(a,0)
#define all(a) a.begin(), a.end()
#define Abs(x) (((x)<0)?-(x):(x))

#define pi 2*acos(0.0)
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))

#define dbg(x) cout<<#x<<'='<<x<<endl;
#define dbgarr(i,a) cout<<#a<<"["<<i<<"] = "<<a[i]<<" "<<endl;
#define IOS ios_base::sync_with_stdio(0);
//typedef
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<pair<int,int>,int > piii;
// Number theory
ll big_mod(ll b,ll p,ll m) {ll res=1;while(p){if(p & 1){res=((res%m)*(b%m))%m;}b=((b%m)*(b%m))%m;p>>=1;}return res;}
ll Pow(ll b,ll p) {ll res=1;while(p){if(p & 1){res=res*b;}b=b*b;p>>=1;}return res;}
ll modinv(ll n,ll m){return big_mod(n,m-2,m);}

////MAIN CODE HERE


int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cno=0;
    scanf("%d",&t);
    while(t--){
        int fq,sq,fa[6][6],sa[6][6];

        scanf("%d",&fq);

        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                scanf("%d",&fa[i][j]);
            }
        }

        scanf("%d",&sq);

        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                scanf("%d",&sa[i][j]);
            }
        }

        bool flag=0;
        int num,cnt=0;
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                if(fa[fq][i]==sa[sq][j]){
                    flag=1;
                    cnt++;
                    num=fa[fq][i];
                }
            }
        }

        if(flag){
            if(cnt==1){
                printf("Case #%d: %d\n",++cno,num);
            }
            else{
                printf("Case #%d: Bad magician!\n",++cno);
            }
        }
        else{
            printf("Case #%d: Volunteer cheated!\n",++cno);
        }

    }
    return 0;
}
