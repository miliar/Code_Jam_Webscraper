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
    int t,p=1;
    inp(t);
    while(t--){
        string s;
        int k;
        cin>>s>>k;
        int n=s.length();
        int h[10005]={0};
        for(int i=0;i<n;i++){
            if(s[i]=='+')
                h[i]=1;
        }
        int cnt=0;
        for(int i=0;i<=n-k;i++){
            if(h[i]==0){
                cnt++;
                for(int j=0;j<k;j++)
                    h[i+j]=!h[i+j];
            }
        }
        int flag=1;
        for(int i=0;i<n;i++){
            if(h[i]==0){
                //cout<<i<<endl;
                flag=0;
                break;
            }
        }
        if(flag)
            printf("Case #%d: %d\n",p++,cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n",p++);
    }

    return 0;
}
