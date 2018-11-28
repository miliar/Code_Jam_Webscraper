/*when pink tuns blue*/

#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<cmath>
#include<ctime>

#define FO(i,s,e,p) for( int i=(s);i<int(e);i+=p)
#define FOD(i,s,e,p) for( int i=(s);i>int(e);i-=p)


#define FOR(i,s,e) FO(i,s,e,1)
#define FORE(i,s,e) FOR(i,s,e+1)
#define FORD(i,s,e) FOD(i,s,e,1)
#define FORDE(i,s,e) FORD(i,s,e-1)

#define ALL(i,s) for(__typeof((s).begin()) i=(s).begin();i!=(s).end();i++)

#define MEM(tab,fill) memset(tab,fill,sizeof(tab))

#include<iostream>
#include<set>
#include<vector>
#include<string>
#include<sstream>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
#include<bitset>
#include<map>
#include<cassert>
#include<limits.h>
#define pb push_back


using namespace std;
#define EPS 0.0000001

#define mp make_pair
#define fi first
#define se second
#define inf ((1<<30)-1)
#define deb(a) cout<<#a<<' '<<a<<endl

#define llu unsigned ll

#define AL(a) (a).begin(),(a).end()

#define PI pair<int,int>
#define PII pair<PI,PI>

#define MIN(a,b) (((a)<(b))?(a):(b))





vector<vector<char> > solve(int n,int m,int r){

    vector<vector<char> > ret(n,vector<char>(m,'*'));
    ret[0][0]='x';
    int t=-1;
    if(r==1){
        ret[0][0]='c';
        return ret;
    }
    bool a=1;
    FORE(i,1,m){
            a=1;
            int div=r/i;
            if(div>n) continue;
            if(div==1 && n!=1) continue;
            if(i==1 && m!=1) continue;
            int na=r%i;

            if(div*i!=r){

                if( (div==n || na>m)  ) continue;
                a&=(div==n || na>m);

            }
            if(na==1){
                if(div==1) continue;
                if(i<=3) continue;
                if( (div>=n || na+1>m) ) continue;
                a&=(div>=n || na+1>m);


            }
            t=i;
            break;

    }
    if(t==-1) return ret;

    ret[0][0]='c';
    int ze=r%t;
    bool ki=ze==1;


    FOR(i,0,r/t)
    FOR(j,0,t){
        if(ki && i+1==r/t && j+1==t) continue;
        if(i || j) ret[i][j]='.';
    }
    int div=r/t;
    ze+=ki;

    if(!a){
        FOR(x,0,ze)
            ret[r/t][x]='.';
    }


    return ret;

}
bool isnormal(vector<vector<int> > &vv,int x,int y){
    FORE(i,-1,1)
    FORE(j,-1,1){
        if(i || j){
            int ta=x+i,tb=y+j;
            if(ta<0 || tb<0 || ta>=vv.size() || tb>=vv[0].size()) continue;
            if(vv[ta][tb]==1) return 0;
        }
    }
    return 1;
}
int last;
bool isposib(int n,int m,int r){
    if(r==1) {last=1;return 1;}
    for(int msk=0;msk<(1<<(n*m));msk++){
            last=msk;
        if(__builtin_popcount(msk)!=r) continue;
        vector<vector<int> > in(n,vector<int>(m,0));
        int k=0;
        FOR(x,0,n)
        FOR(y,0,m) in[x][y]=(msk&(1<<(k++)))==0;
        queue<pair<int,int> > qq;
        FOR(x,0,n)FOR(y,0,m){
            if(in[x][y]==0 && isnormal(in,x,y)){
                qq.push(mp(x,y));

                goto    nxt;
            }
        }
        nxt:
        int sul=0;
        while(qq.size()){
            int x=qq.front().fi,y=qq.front().se;qq.pop();
            sul++;
            if(sul==r) return 1;
            in[x][y]=-1;
            if(!isnormal(in,x,y)) continue;


            FORE(i,-1,1)
            FORE(j,-1,1)
                if(i || j){
                    int ta=x+i,tb=y+j;
                    if(ta<0 || tb<0 || ta>=in.size() || tb>=in[0].size()) continue;
                    if(in[ta][tb]==0){
                        in[ta][tb]=-1;
                        qq.push(mp(ta,tb));
                    }
                }


        }

    }
    return 0;
}


void solve(){
    int n,m,r;
    cin>>n>>m>>r;
    r=n*m-r;

    vector<vector<char> > ret=solve(n,m,r);
    if(ret[0][0]!='c') ret=solve(m,n,r);
    if(ret[0][0]!='c') {
       // if(isposib(n,m,r)) cout<<last<<endl;
       // assert(!isposib(n,m,r));
        cout<<"Impossible"<<endl;

        return;
    }

    if(ret.size()!=n || ret[0].size()!=m){
        FOR(i,0,n){
        FOR(j,0,m) cout<<ret[j][i];
            cout<<endl;
        }
    }else{
        FOR(i,0,n){
        FOR(j,0,m) cout<<ret[i][j];
            cout<<endl;
        }
    }
    //assert(isposib(n,m,r));

}



int main()
{
    freopen("C:\\a","r",stdin);
    freopen("C:\\w","w",stdout);
    int t;cin>>t;
    FORE(i,1,t){
        cout<<"Case #"<<i<<": "<<endl;
        solve();

    }


    return 0;
}
