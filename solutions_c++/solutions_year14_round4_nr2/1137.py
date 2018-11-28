/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;
#include "../bidhan.h"

#define inf (1<<28)
#define eps 1e-9

#define mx 1010

void compress(vi &vec){
    mii ase;
    int k=0;
    foreach(it,vec) ase[ *it];
    foreach(it,ase) it->yy=++k;
    rep(i,sz(vec)) vec[i]=ase[ vec[i] ];
}

int call(vi &my,vi &match){
    int ase[40];
    rep(i,sz(match)) ase[ match[i] ]=i+1;
    binaryIndexedTree bit( sz(my)+1 );
    int ret=0;
    int n=sz(my);
    rep(i,sz(my)){
        int v=ase[ my[i] ];
        ret+=bit.get(n)-bit.get(v-1);
        bit.upd(v);
    }
    return ret;
}

bool valid(vi &now){
    rep(i,sz(now)-1){
        if(now[i]>now[i+1]){
            for(int j=i; j<sz(now)-1; j++){
                if(now[j]<now[j+1]) return false;
            }
            break;
        }
    }
    return true;
}

int main(){
    read("in.txt");
    rite("out.txt");
    ios_base::sync_with_stdio(0);
    int TEST;
    cin>>TEST;
    while( TEST-- ){
        int n;
        cin>>n;
        vi vec;
        rep(i,n){
            int temp;
            cin>>temp;
            vec.pb(temp);
        }
        compress(vec);
        //rep(i,sz(vec)) cout<<" "<<vec[i];
        //cout<<endl;
        i64 ans=1ll<<55;
        if(1){
            vi now;
            for(int i=1; i<=n; i++) now.pb( i );
            //reverse( now.begin()+m-1, now.end());
            do{
                if(valid(now))
            ans=min(ans,call(vec,now)*1ll);
            }while( next_permutation(all(now)) );
            //cout<<"m="<<m<<endl;
            //foreach(it,now) cout<<" "<<*it;
            //cout<<endl;
        }
        COUT_TEST;
        cout<<ans<<endl;
    }
    PRINT_TIME;
    return 0;
}
