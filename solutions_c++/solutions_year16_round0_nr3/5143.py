#include <bits/stdc++.h>
using namespace std;
#define dprint(v) cerr << #v"=" << v << endl //;)
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define pb push_back
#define fst first
#define snd second
#define mkp make_pair
typedef unsigned long long ll;
typedef pair<ll,ll> pll;


#define MAXP 100000	//no necesariamente primo
int criba[MAXP+1];
void crearcriba(){
	int w[] = {4,2,4,2,4,6,2,6};
	for(int p=25;p<=MAXP;p+=10) criba[p]=5;
	for(int p=9;p<=MAXP;p+=6) criba[p]=3; 
	for(int p=4;p<=MAXP;p+=2) criba[p]=2;
	for(int p=7,cur=0;p*p<=MAXP;p+=w[cur++&7]) if (!criba[p]) 
		for(int j=p*p;j<=MAXP;j+=(p<<1)) if(!criba[j]) criba[j]=p;
}

vector<int> primos;
void buscarprimos(){
	crearcriba();
	forr (i,2,MAXP+1) if (!criba[i]) primos.push_back(i);
}

ll arr[15];
ll n,t,j;

ll debase(ll x, ll base)
{
    ll rta=0;
    ll fact=1;
    while(x){
        rta += (x%2)*fact;
        fact *= base;
        x /= 2;
    }
    return rta;
}

bool check(ll x)
{
    for(ll base = 2; base<=10; base++){
        ll aver = debase(x,base); //cout<<aver<<endl;
        bool primo=true;
    	forall(p, primos){
    	    if(*p >= aver) continue;
		    if(aver%*p == 0) {arr[base] = *p; primo=false;}
	    }
        if(primo) return false;
    }
    
    //print num
    for(ll i=n; i>0; i--){
        if(x & (1<<(i-1))) cout<<1;
        else cout<<0;
    }
    
    for(ll base = 2; base<=10; base++) cout<<" "<<arr[base];
    cout<<endl;
    return true;
}


int main() {
    buscarprimos();
   
    cin>>t;
    cin>>n;
    cin>>j;
    cout<<"Case #1: "<<endl;
    
    ll x,top;
    if(n==6) {x = 33; }
    if(n==16) {x = 32769; top = 65535; }
    if(n==32) {x = 2147483649; top = 4294967295; }
    ll count=0;
    
    for(; count<j; x+=2){
        if(check(x)) { count++; }
    }
    
    return 0;
}
