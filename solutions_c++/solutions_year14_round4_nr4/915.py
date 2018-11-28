/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;
#include "../bidhan.h"

#define inf (1<<28)
#define eps 1e-9

#define mx 0

unordered_map<i64,int> Hash[10];
vs S;

#define mod 1000000007

int maxi=0;
int way=0;
int m,n;

void call(int pos){
    if(pos==m){
        int cnt=0;
        rep(i,n) {
            cnt+=sz(Hash[i]);
            //cout<<i<<"="<<sz(Hash[i])<<endl;
        }
        if(cnt>maxi) maxi=cnt, way=1;
        else if(cnt==maxi) way++;
        if(way>=mod) way-=mod;
        return ;
    }
    unordered_set<i64> ase;
    i64 hv=0;
    ase.ins(hv);
    rep(i,sz(S[pos])){
        hv*=31;
        hv+=S[pos][i];
        ase.ins(hv);
    }
    //cout<<"pos="<<pos<<"=>"<<sz(ase)<<endl;
    rep(machine,n){
        /*if(S[pos]=="AAA" || S[pos]=="B") {
            if(machine) continue;
        }
        else if(!machine) continue;*/

        foreach(it,ase) Hash[machine][*it]++;
        call(pos+1);
        foreach(it,ase) {
            Hash[machine][*it]--;
            if(!Hash[machine][*it]) Hash[machine].erase(*it);
        }
    }
}

int main(){
    read("in.txt");
    rite("out.txt");
    ios_base::sync_with_stdio(0);
    int TEST;
    cin>>TEST;
    while( TEST-- ){

        cin>>m>>n;
        //cout<<m<<" "<<n<<endl;
        rep(i,n) Hash[i].clr;
        S.clr;
        rep(i,m){
            st tmp;
            cin>>tmp;
            S.pb(tmp);
        }
        maxi=way=0;
        call(0);
        COUT_TEST;
        cout<<maxi<<" "<<way<<endl;
        //return 0;
    }
    PRINT_TIME;
    return 0;
}
