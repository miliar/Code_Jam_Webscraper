#include <bits/stdc++.h>
#define REP(i,n) for(int i=0; i<int(n); i++)
#define ALL(v) (v).begin(),(v).end()
#define DBG(x) cerr<<__LINE__<<": " #x " = "<<x<<endl
#define endl '\n'
using namespace std;


int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T; cin>>T;
    REP(_t, T) {
        cout<<"Case #"<<_t+1<<": ";
        int N; cin>>N;
        string S; cin>>S;
        
        int standup=0, mustadd=0;
        REP(i, N+1) {
            if(S[i]>'0') {
                mustadd += max(0, i-standup);
                standup += S[i]-'0' + max(0, i-standup);
            }
            //cerr<<i<<" add="<<mustadd<<" stup="<<standup<<endl;
        }
        
        cout<<mustadd<<endl;
    }
}
