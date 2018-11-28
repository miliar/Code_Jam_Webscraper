#include<bits/stdc++.h>
//#include<iostream>
//#include<stdio.h>


using namespace std;

#define ll int
#define lll long long int
#define s(a) scanf("%d",&a)
#define slll(a) scanf("%lld",&a)
#define fr(i,n) for(i=0;i<n;i++)
#define fra(i,a,n) for(i=a;i<n;i++)
//#define N 100010
#define inf lll_MAX
#define MOD 1000000007
#define MAX 1000000
#define SET(v,i) memset(v, i, sizeof(v))

/*#define gc getchar_unlocked

void scanlll(lll &x)
{
    register lll c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

ll gcd(ll a,ll b)
{
   //cout<<a<<" "<<b<<endl;
   if(b==0)
   return a;
   return gcd(b,a%b);
}*/
/*
struct node
{
  ll rank0,rank1,pos;
};

bool cmp(node a,node b)
{
  if(a.rank0==b.rank0)
    return a.rank1<b.rank1;

  return a.rank0<b.rank0;
}*/
/*int cmpqsort (const void * a, const void * b)
{
  if(((node*)a)->rank0==((node*)b)->rank0)
    return ( ((node*)a)->rank1 - ((node*)b)->rank1 );

    return ( ((node*)a)->rank0 - ((node*)b)->rank0 );


}*/
/*
struct comp
{
    bool operator()(const node a, const node b)
    {
        return a.r >b.r;
    }
};*/
/*
#define INF (1<<20)
#define pii pair< int, int >
#define pb(x) push_back(x)
#define MAX 100001
struct comp {
    bool operator() (const pii &a, const pii &b) {
        return a.second > b.second;
    }
};*/

/*
ll poww(ll a, ll b)
{

  ll x = 1, y = a;
    while(b > 0) {
        if(b%2 == 1) {
            x=(x*y);
           // if(x>MOD) x%=MOD;
        }
        y = (y*y);
        //if(y>MOD) y%=MOD;
        b /= 2;
    }
    return x;
}
*/

/*
bool v[MAX];
lll len, sp[MAX];

void Sieve(){
    // prime v=0;
	memset(v,0,sizeof(v));

	for (lll i = 2; i < MAX; i += 2)
     {
         sp[i] = 2;
         v[i]=1;
     }
     v[2]=0;
    //even numbers have smallest prime factor 2

	for (lll i = 3; i < MAX; i += 2){
		if (!v[i]){
			sp[i] = i;
			for (lll j = i; (j*i) < MAX; j += 2){
				if (!v[j*i])	v[j*i] = true, sp[j*i] = i;
			}
		}
	}

}*/

int main(){
	//Sieve();
   ll k,c,s,t,tc,i;

   s(t);
   fra(tc,1,t+1)
   {
       s(k); s(c); s(s);
       cout<<"Case #"<<tc<<": ";
       fr(i,k)
       {
           cout<<i+1<<" ";
       }
       cout<<endl;
   }

}
