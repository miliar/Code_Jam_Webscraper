#include <cstdio>
#include <set>
#include <cassert>
#include <algorithm>
using namespace std;

int V[10009];
int N,C;

bool f(int K){
    multiset<int> st;

    int n = N  - K;
    if(n%2 == 1)n--;
    for(int i=n-1;i>=0;i--){
        st.insert(V[i]);
    }

    assert((st.size() % 2) == 0);
    
    int target,x;
    set<int>::iterator it;
    while(!st.empty()){
        x =  *st.rbegin();
        st.erase(--st.end());

        target = C - x;

        it = st.upper_bound(target);

        if(it == st.begin())return false;
        it--;
        assert(x + target <= C);

        st.erase(it);
    }
    return true;
}

int calc(int used){
    //printf("used = %d N = %d\n",used,N);
    return used + (N - used + 1)/2;
}

int solve(){
    scanf("%d %d",&N,&C);

    for(int i=0;i<N;i++){
        scanf("%d",&V[i]);
    }
    sort(V,V+N);

    if(f(0))return calc(0);

    int a = 0,b=N,m;
    while(a + 1 < b){
        m = (a + b) / 2;

        if(f(m)){
            b = m;
        }else{
            a = m;
        }
    }
    return calc(b);
}

int main(){
    int NC;scanf("%d",&NC);
    int ans = 0;
    for(int i=1;i<=NC;i++){
        ans = solve();
        printf("Case #%d: %d\n",i,ans);
    }
}