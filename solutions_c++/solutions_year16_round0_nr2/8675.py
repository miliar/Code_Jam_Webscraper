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
int main(){
    INT(T);
    int d=1;
    while(T--){
        printf("Case #%d: ",d);
        int wyn=0;
        d++;
        string x;
        cin >> x;
        if(x[0]=='-')wyn++;
        FORR(i,x.size(),1)if(x[i]=='-'&&x[i-1]=='+')wyn+=2;
        printf("%d\n",wyn);
    }
}

        
            
        
