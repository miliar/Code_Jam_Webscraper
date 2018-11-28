#include <bits/stdc++.h>
#define X first
#define Y second
#define psb push_back
#define pob pop_back
#define mp make_pair
#define ll long long
#define scand(n) scanf("%d",&n)
#define scanld(n) scanf("%lld",&n)
#define printd(n) printf("%d\n",n)
#define printld(n) printf("%lld\n",n)
#define all(x) x.begin(),x.end()
#define SET( arr, val) memset(arr,val,sizeof(arr))
#define ITR iterator
#define SZ(arr) arr.size()
#define FOR( i, L, U ) for(int i=(int)L ; i<(int)U ; ++i )
#define FORI( i, L, U ) for(int i=(int)L ; i<=(int)U ; ++i )
#define FORD( i, U, L ) for(int i=(int)U ; i>=(int)L ; --i )
#define Tcases(t) int t;cin>>t;while(t--)

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;

//int n=16,J=50;
int cnt=0;

int divi[51][11];

int l=1<<15;
int r=1<<16;

string s[51];

//int sie[100000];

int chk(ll num){
    ll lim=sqrt(num) +5;
    FORI(i,2,lim)
        if(num%i==0)
            return i;
    return -1;
}
/*
void comp(){
 //   fill(sie,sie+100000,1);
    FOR(i,2,100000){
        if(sie[i]==1){
            sie[i]=i;
            for(int j=i+i;j<100000;j+=i)
                sie[j]=i;
        }
    }
}
*/
ll conv(ll inp,int base){
    ll ret=1;
    ll mul=1;
    FOR(i,1,16){
        mul*=base;
        if((inp>>i)&1)
            ret+=mul;
    }
    return ret;
}

void addAns(ll num){
    string str;
    FOR(i,0,16)
        str+='0'+((num>>i)&1?1:0);
    reverse(all(str));
    s[cnt++]=str;
}

void solve(ll num){
    int d=chk(num);
    if(d==-1)
        return;
    bool ok=1;
    divi[cnt][2]=d;
    FORI(b,3,10){
        ll id=conv(num,b);
        d=chk(id);
        if(d==-1){
            ok=0;
            break;
        }
        divi[cnt][b]=d;
    }
    if(ok)
        addAns(num);
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("output.txt","w",stdout);
//	comp();
	cnt=0;
	for(int i=l+1;i<r &&cnt<50;i+=2)
        solve(i);

    cout<<"Case #1:\n";

    FOR(i,0,50){
        cout<<s[i]<<" ";
        FORI(j,2,10)
            cout<<divi[i][j]<<" ";
        cout<<endl;
    }

	return 0;
}
