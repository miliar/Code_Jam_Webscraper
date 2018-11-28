#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>
using namespace std;
#define MOD 1000002013LL
typedef long long LL;
multiset<pair<LL,LL> > st;
priority_queue< pair<LL,LL> > q;
LL N;
int k;
LL e,o,c;
void solve(int t){
    cout << "Case #" << t << ": ";
    st.clear();
    while(!q.empty()) q.pop();
    scanf("%lld %d", &N,&k);
    //cout << N << " "<< k <<endl;
    LL total = 0;
    for(int i=0; i<k; i++){
        scanf("%lld %lld %lld", &e, &o, &c);
        st.insert(make_pair(e,-c));
        st.insert(make_pair(o,+c));
        total = (total + (o-e)*(2*N+e-o+1)/2%MOD*c)%MOD;
    }
   // cerr << total<< endl;
    LL pr =0;
    multiset< pair<LL,LL> >::iterator it;
    for( it = st.begin(); it!= st.end(); it++){
        int s = it->first;
        int c = it->second;
        if(c>0){
            while(c){
                pair<LL,LL> p = q.top(); q.pop();
                if(c>= p.second){
                    pr = (pr+1LL*p.second*(s-p.first)*(2LL*N-s+p.first+1)/2)%MOD;
                    c-= p.second;
                }
                else{
                    pr = (pr+1LL*c*(s-p.first)*(2*N-s+p.first+1)/2)%MOD;
                    q.push(make_pair(p.first,p.second-c));
                    c=0;
                }
            }
        }
        else{
            q.push(make_pair(s,-c));
        }
    }
    cout << (total - pr +MOD)%MOD << endl;
}

int ntest;
int main(){
    freopen("A-small-attempt2.in","r",stdin);
    //freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d\n",&ntest);
    for(int t=0; t<ntest; t++){
        solve(t+1);
    }
    return 0;
}
