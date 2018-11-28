#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<limits>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second
#define PP system("PAUSE");
#define MOD 1000002013

using namespace std;

typedef struct XD{
    int o, e;
    int ind;
    long long int p;
    bool operator <(XD A) const{
        if(o == A.o) return e < A.e;
        return o < A.o;
    }
    bool operator >(XD A) const{
        if(e == A.e) return o < A.o;
        return e < A.e;
    }
};


int N, M;
XD pass[1010];
XD pass1[20101010];
XD tpass[20101010];
set<int> sta;
priority_queue<XD, vector<XD> > PQ;

void solve(void){
    long long int ans = 0;
    long long int nans = 0;
    scanf("%d%d", &N, &M);
    for(int i = 0; i < M; i++){
        scanf("%d%d%lld", &pass[i].o, &pass[i].e, &pass[i].p);
        pass[i].ind = i;
        long long int temp;
        temp = (2*N*(pass[i].e-pass[i].o));
        temp %= MOD;
        temp -= (pass[i].e-pass[i].o)*(pass[i].e-pass[i].o);
        temp %= MOD;
        temp += pass[i].e-pass[i].o;
        temp %= MOD;
        temp /= 2;
        temp %= MOD;
        temp *= pass[i].p;
        temp %= MOD;
        ans += temp;
        ans %= MOD;
    }
    sort(pass, pass+M);
    for(int i = 0; i < M; i++)
        pass1[i] = pass[i];
    sort(pass1, pass1+M, greater<XD>());
    int A, B;
    A = B = 0;
    while(B < M){
        if(A<M && pass[A].o <= pass1[B].e){
            PQ.push(pass[A]);
            A++;//puts("QQQ");
            continue;
        }
        else{
            int p = PQ.top().p;
            //printf("==%d %d\n", pass1[B].e, PQ.top().o);
            while(p <= pass1[B].p){//puts("S");
                pass1[B].p -= p;

                long long int temp;
                temp = (2*N*(pass1[B].e-PQ.top().o));
                temp %= MOD;
                temp -= (pass1[B].e-PQ.top().o)*(pass1[B].e-PQ.top().o);
                temp %= MOD;
                temp += MOD;
                temp %= MOD;
                temp += pass1[B].e-PQ.top().o;
                temp %= MOD;
                temp += MOD;
                temp %= MOD;
                temp /= 2;
                temp *= p;
                temp %= MOD;
                //printf("%lld\n", temp);
                nans += temp;
                nans %= MOD;
                //printf("%lld===--\n", nans);
                PQ.pop();
                if(!PQ.empty())
                    p = PQ.top().p;
                else break;
            }
            if(pass1[B].p){//puts("CC");
                XD tx = PQ.top();//printf("^^%d\n", tx.o);
                tx.p -= pass1[B].p;//printf("p:%d\n", tx.p);
                long long int temp;
                temp = (2*N*(pass1[B].e-PQ.top().o));
                temp %= MOD;
                temp -= (pass1[B].e-PQ.top().o)*(pass1[B].e-PQ.top().o);
                temp %= MOD;
                temp += MOD;
                temp %= MOD;
                temp += pass1[B].e-PQ.top().o;
                temp %= MOD;
                temp += MOD;
                temp %= MOD;
                temp /= 2;
                temp *= pass1[B].p;
                temp %= MOD;
                nans += temp;
                nans %= MOD;
                pass1[B].p = 0;
                PQ.pop();
                if(tx.p)
                    PQ.push(tx);
            }
        B++;
        }
    //printf("ww%lld\n", nans);
    }
    long long int res = ans-nans;
    res %= MOD;
    res += MOD;
    res %= MOD;
    printf("%lld\n", res);
    return;
}

int main(void){
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
    }
