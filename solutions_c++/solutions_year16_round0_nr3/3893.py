#include<bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define res resize
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
vector<int>pierw;
bool sito[1666];
int n,j;
void prep(){
    for(int i=2;i*i<1666;i++)
        if(!sito[i])
            for(int j=i*i;j<1666;j+=i)
                sito[j]=true;
    for(int i=2;i<1666;i++)
        if(!sito[i])
            pierw.pb(i);
}
vector<int>odp;
ll zamien(int mask,int p){
    ll x=0; ll pot=1;
    for(int i=0;i<n;i++,pot*=p)
        if( (1<<i) & mask)
            x+=pot;
    return x;
}
int dziel(ll x){
    for(int i=0;i<pierw.size();i++)
        if(x>pierw[i] && x%pierw[i]==0)
            return pierw[i];
    return 0;
}
bool solve(int mask){
    odp.clear(); odp.pb(mask);
    for(int i=2;i<=10;i++){
        ll x=zamien(mask,i);
        //printf("%lld ",x);
        int d=dziel(x);

        if(d)odp.pb(d);
        else return false;
    }
    return true;
}
void wypisz(){
    for(int i=n-1;i>=0;i--)
        if( (1<<i)&odp[0])printf("1");
        else printf("0");
    printf(" ");
    for(int i=1;i<odp.size();i++)
        printf("%d ",odp[i]);
    puts("");
}
int main(){
    prep();
    puts("Case #1:");
    n=16,j=50;
    for(int mask=0;mask<(1<<(n-2));mask++){
        if(solve(1+2*mask+(1<<(n-1)))){
            wypisz();
            j--;
            if(j==0)return 0;
        }
    }
	return 0;
}
