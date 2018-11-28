/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Aditya Agarwal
 * IT, MNNIT-ALLAHABAD 
 * aditya.mnnit15@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/


#include<bits/stdc++.h>
using namespace std;

#define MP make_pair
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define PER(i,a,b) for(int i=b;i>=a;i--)
#define X first
#define Y second

 //i/o
#define inp(n) scanf("%d",&n)
#define inpl(n) scanf("%lld",&n)
#define inp2(n,m) inp(n), inp(m)
#define inp2l(n,m) inpl(n), inpl(m)


//cost
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 100009
#define INF 999999999
#define mp make_pair
typedef long long ll;
typedef pair< pair<ll,ll>,ll > pairs;


int main(){

    freopen("inp.in","r",stdin);
    freopen("oup.out","w",stdout);

    int t,k=1;
    inp(t);
    while(t--){
        string s;
        cin>>s;
        int len=s.size();
        int cnt=1,pos=-1;
        for(int i=0;i<len;++i){
            if(s[i]=='-')
                pos=i;
        }
        if(pos==-1)
            cnt=0;
        else{
            for(int i=pos;i>0;--i){
                if(s[i]!=s[i-1])
                    cnt++;
            }
        }
        printf("Case #%d: %d\n",k,cnt);
        k++;
    }
return 0;}