#include<iostream>
#include<string>
#include<string.h>
#include<cstdio>
#include<algorithm>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<cassert>
 
using namespace std;
 
#define ll long long
#define l long
#define max(a,b) (a>b?a:b)
#define min(a,b) (a>b?b:a)
#define ms(a,b) memset(a,(b),sizeof(a))
#define fr(i,a,n) for(i=a;i<n;i++)
#define gc getchar()
#define pc putchar
#define ull unsigned ll
 
 
inline ll gcd(ll a,ll b){if(b==0)return a;else return gcd(b,a%b);}
inline ll lcm(ll a,ll b){return (a*b)/gcd(a,b);}
 
inline void get(l &x){register l c=gc;x=0;l neg=0;for(;((c<48||c>57)&&c!='-');c=gc);if(c=='-'){neg = 1;c=gc;}for(;c>47&&c<58;c=gc){x=(x<<1)+(x<<3)+c-48;}if(neg)x=-x;}
 
inline void get(int &x){register int c=gc;x=0;int neg=0;for(;((c<48||c>57)&&c!='-');c=gc);if(c=='-'){neg = 1;c=gc;}for(;c>47&&c<58;c=gc){x=(x<<1)+(x<<3)+c-48;}if(neg)x=-x;}
 
inline void get(ll &x){register ll c=gc;x=0;ll neg=0;for(;((c<48||c>57)&&c!='-');c=gc);if(c=='-'){neg = 1;c=gc;}for(;c>47&&c<58;c=gc){x=(x<<1)+(x<<3)+c-48;}if(neg)x=-x;}
 
inline void get(ull &x){register ull c=gc;x=0;ull neg=0;for(;((c<48||c>57)&&c!='-');c=gc);if(c=='-'){neg = 1;c=gc;}for(;c>47&&c<58;c=gc){x=(x<<1)+(x<<3)+c-48;}if(neg)x=-x;}
 
inline void put(int n){int i=0;char ch[20];if(n==0)pc('0');while(n>0)ch[i]=(n%10)+'0',n=n/10,i++;while(i>0)pc(ch[i-1]),i--;} 
 
inline void put(l n){l i=0;char ch[20];if(n==0)pc('0');while(n>0)ch[i]=(n%10)+'0',n=n/10,i++;while(i>0)pc(ch[i-1]),i--;}
 
inline void put(ll n){ll i=0;char ch[20];if(n==0)pc('0');while(n>0)ch[i]=(n%10)+'0',n=n/10,i++;while(i>0)pc(ch[i-1]),i--;}
 
inline void put(ull n){ull i=0;char ch[20];if(n==0)pc('0');while(n>0)ch[i]=(n%10)+'0',n=n/10,i++;while(i>0)pc(ch[i-1]),i--;}
 
// Q1
int main()
{
   #ifndef ONLINE_JUDGE
   freopen("inp_random.txt","r",stdin);
   freopen("out_random.txt","w",stdout);
 
   #endif
   int t,x;
   get(t);
   for(x=1;x<=t;x++){
      cout<<"Case #"<<x<<": ";
      ll n;
      get(n);
      if(n== 0){
         cout<<"INSOMNIA\n";
      }
      else{
         ll hash[10],cnt=0,mul,temp = n,i=1,t2=n;
         ms(hash,0);
         while(cnt<10){
            i++;
            n = temp;
           //cout<<n<<"\n";
            while(n>0){
               int d = n%10;
               if(hash[d]==0){
                  hash[d] = 1;
                  cnt++;
               }
               n/=10;
            }
            temp = t2*i;
         }
         cout<<temp-t2<<"\n";
      }
   }
   return 0;
         
}