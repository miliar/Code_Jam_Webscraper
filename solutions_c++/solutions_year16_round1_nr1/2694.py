#include <bits/stdc++.h>
using namespace std;
#define LL long long int
#define SI short int
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pbc pair<bool,char>
#define pcc pair<char,char>
#define vi vector<int>
#define vii vector<vector<int> >
#define vb vector<bool>
#define FOR(i,st,end) for(int (i)=(st);i<(end);i++)
#define FORD(i,st,end) for(int (i)=(st);i>=(end);i--)
#define FASTIO ios::sync_with_stdio(false);
#define ABS(i) ((i)>0)?(i):(-(i))
#define sci(m) scanf(" %d",&m)
#define SORT(x) sort(x.begin(),x.end())
#define MOD 1000000007

int main(void){
    int T;
    sci(T);
    FOR(t,0,T){
        string s,w;
        cin>>s;
        deque<char> dq;
        dq.pb(s[0]);
        FOR(i,1,s.length()){
            if(s[i]>=dq.front())
                dq.push_front(s[i]);
            else dq.pb(s[i]);
        }
        FOR(i,0,s.length()){
            w += dq[i];
        }
        cout<<"Case #"<<(t+1)<<": "<<w<<"\n";
    }
    return 0;
}
