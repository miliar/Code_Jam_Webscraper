#include<bits/stdc++.h>
using namespace std;

#define int long long
typedef pair<int,int>pint;
typedef vector<int>vint;
typedef vector<pint>vpint;
#define pb push_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define all(v) (v).begin(),(v).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
template<class T,class U>inline void chmin(T &t,U f){if(t>f)t=f;}
template<class T,class U>inline void chmax(T &t,U f){if(t<f)t=f;}

int solve(string S){
    stack<char>s;
    int ans=0;
    rep(i,S.size()){
        if(s.size()&&s.top()==S[i]){
            ans+=10;
            s.pop();
        }
        else{
            s.push(S[i]);
        }
    }

    return ans+(s.size()/2*5);
}


/*
int test(string S){
    int ma=0;
    rep(i,1<<S.size()){
        int val=0;
        stack<char>s;
        bool ng=false;
        rep(j,S.size()){
            if(i>>j&1){
                s.push(S[j]);
            }
            else{
                if(s.size()==0){
                    ng=true;
                    break;
                }
                if(s.top()==S[j])val+=10;
                else val+=5;
                s.pop();
            }
        }
        if(ng)continue;
        chmax(ma,val);
    }
    return ma;
}
*/
signed main(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    /*
    srand((unsigned)time(NULL));

    while(true){
        int t;
        cin>>t;
        if(t==-1)break;
        string S;
        rep(i,16){
            if(rand()%2)S+="1";
            else S+="0";
        }
        cout<<S<<" "<<solve(S)<<" "<<test(S)<<endl;
    }
    */

    int N;
    cin>>N;
    rep(i,N){
        string S;
        cin>>S;
        cout<<"Case #"<<i+1<<": "<<solve(S)<<endl;
    }
    return 0;
}
