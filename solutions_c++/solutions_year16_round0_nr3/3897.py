/*  
   Mayank Pratap Singh
   MNNIT, 2nd year IT
         
   AC ho.
*/
#include<bits/stdc++.h>
using namespace std;
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

#define MOD 1000000007

typedef long long ll;
typedef long double ld;

const int INF=(int)(1e9);
const ll INF64=(ll)(1e18);
const ld EPS=1e-9;
const ld PI=3.1415926535897932384626433832795;


typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef vector<list<int> > vl;
typedef map<int,int> mi;
typedef map<string,int> ms;
typedef set<int> si;

//bool prime[100000000];

//map<int,int>prime;
/*
void sieve(){

   int n=100000;

   for(int i=0;i<=n;++i){

       prime[i]=true;

   }

   prime[0]=false;
   prime[1]=false;

   for(int i=2;i*i<=n;++i){

        if(prime[i]){

            for(int j=i*i;j<=n;j+=i)
               prime[j]=false;
        }

   }
}   */
   
ll toDecimal(ll n,int b){

   ll result=0;
   ll multiplier=1;

   while(n>0){

      result+=n%10*multiplier;
      multiplier*=b;
      n/=10;
   }

   return result;

}

ll fromDecimal(ll n,int b){

   ll result=0;
   ll multiplier=1;

   while(n>0){

       result+=(n%b)*multiplier;
       multiplier*=10;
       n/=b;

   }
   return result;
}

ll isPrime(ll n){    

    for(ll i=2;i*i<=n;++i){
 
        if(n%i==0)
            return i;

       // printf("lulla\n");  
    }

    return 0;
}


int main(){

    int t;

  //  sieve();

    scanf("%d",&t);

    for(int k=1;k<=t;++k){

  //   printf("Case #%d:\n",k);

       int n,m,flag=0;

       scanf("%d %d",&n,&m);
 
       printf("Case #%d:\n",k);


      // printf("Hello\n");

       int ans1=1<<14;
       int ans2=1<<15;

       for(int j=0;j<ans1;++j){
           
          // printf("Hello\n");
           ll num=ans2+j*2+1;
          // printf("%lld\n",num);
           ll res=fromDecimal(num,2);

          // printf("%lld\n",res);

           int count=0;
          // printf("Hello\n");
           vector<ll>nonTrivials;  // Store non trivial divisors

           for(int b=2;b<=10;++b){

                ll temp=toDecimal(res,b);
                //printf("%d\n",temp);
                //  printf("%lld\n",temp);
        
                ll calc=isPrime(temp);

                if(calc!=0){
                    ++count;
                    nonTrivials.pb(calc);
                } 

        
           }

           if(count==9){
               printf("%lld ",res);
              for(int i=0;i<nonTrivials.size();++i){
                 printf("%lld ",nonTrivials[i]);

              }
              printf("\n");
              ++flag;
           }   

            if(flag==m){

                break;
           }
       }


    }






  return 0;
}