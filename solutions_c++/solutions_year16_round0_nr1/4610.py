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

int main(){

     int t;

     scanf("%d",&t);

     for(int k=1;k<=t;++k){

         int n;

         scanf("%d",&n);

         int counter[10];

         for(int i=0;i<=9;++i){

         	 counter[i]=0;
         }

         if(n==0){

             printf("Case #%d: INSOMNIA\n",k);

         }

         else{

            int multiplier=1;

            ll ans;

            while(1){

               ll num=n*multiplier;

               while(num){

                  int b=num%10;

                  counter[b]++;

                  num=num/10;

               }

               int flag=0;

               for(int i=0;i<=9;++i){

                  if(counter[i]==0){

                      flag=1;
                      break;
                  }
               }

               if(flag==0){
  
                   ans=n*multiplier;
               	   break;
               }

               multiplier++;
            }

            printf("Case #%d: %lld\n",k,ans);

         }

     }

	return 0;
}