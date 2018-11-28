#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<time.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
ll BigMod(ll B,ll P,ll M){  ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define ull unsigned long long

map<vector<int>,int>MP;
int dfs(vector<int>V){
    if(V.size()==0)return 0;
    int x=V[V.size()-1];
    if(x==1)return 1;
    if(MP.find(V)!=MP.end())return MP[V];
    int mn=x;
    for(int i=1;i<=x/2;i++){
        int akta=i;
        int arekta=x-i;
        vector<int>N=V;
        N.pop_back();
        N.push_back(akta);
        N.push_back(arekta);
        sort(N.begin(),N.end());
        int val=1+dfs(N);
        mn=min(mn,val);
    }
    return MP[V]=mn;
}

int main()
{
    in("in.txt");
    out("out.txt");
    int T,caseno=1;
    cin>>T;

    while(T--){
        MP.clear();
        int D;
        cin>>D;
        vector<int>V;
        int mx=0;
        for(int i=0;i<D;i++){
            int x;
            cin>>x;
            V.push_back(x);
        }
        sort(V.begin(),V.end());
        mx=dfs(V);
        cout<<"Case #"<<caseno++<<": "<<mx<<endl;
    }
    return 0;
}
