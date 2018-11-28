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

int N,S;
int x[1000],y[1000],z[1000],vx[1000],vy[1000],vz[1000];

void solveSmall(){
    int dist[1000];
    fill_n(dist,N,1001001001);
    dist[0]=0;
    priority_queue<pint,vector<pint>,greater<pint>>que;
    que.push(pint(0,0));

    while(que.size()){
        int d,v;
        tie(d,v)=que.top();
        que.pop();
        if(dist[v]<d)continue;

        rep(i,N){
            int dd=max((x[i]-x[v])*(x[i]-x[v])+(y[i]-y[v])*(y[i]-y[v])+(z[i]-z[v])*(z[i]-z[v]),d);
            if(dist[i]<=dd)continue;
            dist[i]=dd;
            que.push(pint(dd,i));
        }
    }

    printf("%.20f\n",sqrt((double)dist[1]));
}

void solveLarge(){

}

signed main(){
    int T;
    cin>>T;
    rep(i,T){
        cout<<"Case #"<<i+1<<": ";
        cin>>N>>S;
        rep(i,N)cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];

        solveSmall();
        //solveLarge();
    }
    return 0;
}
