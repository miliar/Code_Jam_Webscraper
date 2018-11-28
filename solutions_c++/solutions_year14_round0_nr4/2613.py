
#include <bits/stdc++.h>
#define N 1<<10
#define INF 100000
using namespace std;

int n , c[N][N],dp[N][N] , caso ;
double naomi[1111] , ken[1111];
int solve(int naomimask,int kenmask){
    if(naomimask==(1<<n) - 1) return 0;
    if(c[naomimask][kenmask] == caso) return dp[naomimask][kenmask];
    c[naomimask][kenmask] = caso;

    int ans = -INF;
    for(int i = 0; i < n; ++i)
        if( (naomimask&(1<<i)) == 0)
        {   int pos = upper_bound(ken,ken+n,naomi[i]) - ken - 1;

            for(; pos < n; ++pos)
            {   int val = -1;
                for(int k = pos+1; k < n; ++k)
                    if( (kenmask&(1<<k)) == 0){
                        val = k;
                    break;
                    }

                if(val == -1){
                    for(int k = 0; k < n; ++k)
                            if( (kenmask&(1<<k)) == 0){
                               val = k;
                                break;
                            }
                }
                if( val > pos){ // mandara para ganar
                    if(ken[val] > naomi[i])
                    ans = max(ans,solve(naomimask|(1<<i),kenmask|(1<<val)));
                }else{
                    if(ken[val] < naomi[i])
                    ans = max(ans,1 + solve(naomimask|(1<<i),kenmask|(1<<val)));
                }
            }
        }
    return dp[naomimask][kenmask] = ans;
}

bool used[N];
int greedy(){

    for(int i = 0; i < n; ++i) used[i] = 0;

    int res = 0;
    for(int i = 0; i < n; ++i){
        int pos = -1;
        for(int k = 0; k < n; ++k)
        if(!used[k] && ken[k] > naomi[i]){
            pos = k;
            break;
        }
        int costo = pos == -1 ? 1:0;

        if(pos == -1){
            for(int k = 0; k < n; ++k)
                if(!used[k]){
                    pos = k;
                    break;
                }
        }
    res += costo;
    used[pos] = 1;
    }
    return res;
}

void greedystep(){

        int left = 0;
        for(int i = 0; i < n; ++i)
           if(naomi[i] < ken[0])
            left++;

        int k = 0 , res = 0; // kent
        for(int i = left; i < n; ++i){
            if(naomi[i] > ken[k]) ++res , k++;
        }
        cout << res << " "<< greedy()<<endl;
}

void dpstep(){
    ++caso;
    cout << solve(0,0) << " "<<greedy()<<endl;
}

int main(){
    freopen("in.c","r",stdin);
    freopen("on.c","w",stdout);

    int tc , nc = 1;
    cin>>tc;

    while(tc--){
        cin >> n;
        for(int i = 0; i < n; ++i)
        cin >> naomi[i];
        for(int i = 0; i < n; ++i)
        cin >> ken[i];

        sort(naomi,naomi+n);
        sort(ken,ken+n);

        printf("Case #%d: ",nc++);
        //dpstep();
        greedystep();
    }


    return 0;
}

