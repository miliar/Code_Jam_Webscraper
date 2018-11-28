#include<bits/stdc++.h> 
using namespace std;
#define f first
#define s second
#define PB push_back
typedef long long ll;
typedef long double ld;
#define FOR(x,y) for(int x=0;x<(y);x++)
#define ROF(x,y) for(int x=(y);x>=0;x--)
#define FORR(x,y,z) for(int x=(z);x<(y);x++)
#define INT(x) int x;scanf("%d",&x)
#define LL(x) ll x;scanf("%lld",&x)
const ll hsz=996662137;
const ll X=42;
const int N=26;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pii> piii;
bool t[15];
int main(){
    INT(T);
    int d=1;
    while(T--){
        printf("Case #%d: ",d);
        d++;
        INT(n);
        int a=n;
        FOR(i,12)t[i]=false;
        if(n==0){printf("INSOMNIA\n");continue;}
        int q=0;
        while(q<10){
            int c=a;
            while(c!=0){
                t[c-(c/10)*10]=true;
                c/=10;
            }
            a+=n;
            q=0;
            FOR(i,11)q+=t[i];
        }
        printf("%d\n",a-n);
    }
}
            
        
