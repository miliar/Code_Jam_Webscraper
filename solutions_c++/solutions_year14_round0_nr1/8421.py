/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;
#include <bits/stdc++.h>

#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define sgn(x,y) ((x)+eps<(y)?-1:((x)>eps+(y)?1:0))
#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define mx 0

si intersection( si &a, si &b){
    si ret;
    foreach(it,a){
        if( b.find( *it ) != b.end() ) ret.ins( *it );
    }
    return ret;
}

int main(){
    read("ain.txt");
    rite("aout.txt");
    ios_base::sync_with_stdio(0);
    int test,kas=0;
    cin>> test;
    while( test-- ){
        int row;
        cin>>row;
        si p1, p2;
        for(int i=1; i<=4; i++){
            for(int j=1; j<=4; j++){
                int temp;
                cin>> temp;
                if(i==row) p1.ins(temp);
            }
        }
        cin>>row;
        for(int i=1; i<=4; i++){
            for(int j=1; j<=4; j++){
                int temp;
                cin>> temp;
                if(i==row) p2.ins(temp);
            }
        }
        si ans=intersection(p1,p2);
        cout<<"Case #"<<++kas<<": ";
        if( sz( ans ) == 1 ) cout<< *ans.begin() <<endl;
        else if( sz( ans ) > 1 ) cout<<"Bad magician!"<<endl;
        else if( sz( ans ) == 0 ) cout<< "Volunteer cheated!" <<endl;
    }
    return 0;
}
