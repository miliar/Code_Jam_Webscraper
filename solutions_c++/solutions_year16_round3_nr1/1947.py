#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define fora(x,y,z) for(int x=y;x<=(z);x++)
#define PNL printf("\n")
#define FL(a,n,x) fill(a,a+n,x)
#define pii pair<int,int>
#define F first
#define S second
#define mp make_pair
#define MOD 1000000007
#define debug(x) cout<<"here"<<x<<endl;

int main(){
   freopen("Input.in","r",stdin);
   freopen("Output.txt","w",stdout);
   int te;
   si(te);
   int ts=0;
   while(te--){
        ts++;
    int cnt[26];
    memset(cnt,0,sizeof(cnt));
    int n,tn=0;
    si(n);
    fora(i,0,n-1){
    si(cnt[i]);
    tn+=cnt[i];
    }
    multiset<pii ,greater<pii> > s;
    fora(i,0,n-1)
    s.insert(mp(cnt[i],i));
    cout<<"Case #"<<ts<<": ";
    while(tn>0){
        multiset<pii>::iterator it;
        it=s.begin();
        s.erase(it);
        int f=it->S,s2=it->F;
        s2--; tn--;
        char ch='A'+f;
        cout<<ch;
        it=s.begin();
        if(tn!=0 && (it->F > (tn/2))){
            int f1=it->S,s1=it->F;
            s.erase(it);
            s1--; tn--;
            ch='A'+f1;
            cout<<ch;
            s.insert(mp(s1,f1));
        }
        s.insert(mp(s2,f));
        cout<<" ";
    }
    cout<<endl;
   }
   return 0;
}
