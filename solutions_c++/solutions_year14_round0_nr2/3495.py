#include<iostream>
#include<string>
#include<string.h>
#include<cstdio>
#include<algorithm>
#include<map>
#include<cmath>
#include<vector>

using namespace std;

#define ll long long
#define l long
#define max(a,b) (a>b?a:b)
#define min(a,b) (a>b?b:a)
#define ms(a,b) memset(a,(b),sizeof(a))
#define fr(i,a,n) for(i=a;i<n;i++)
#define gc getchar_unlocked()
#define pc putchar_unlocked
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

int main(){

        int t,y,i,j;
            l double c,f,x,check,next,ans,nextf=0,check1,next1=0,sum;
            get(t);
           fr(y,1,t+1){
               next1=next=ans=f=0;
               //cin>>c>>f>>x;
               scanf("%Lf%Lf%Lf",&c,&f,&x);
              // printf("%.7Lf",c);
              //check=x/2;
              nextf=2;
             // next=c/2;
             // next1=x/nextf;
              int p=5;
             while(1) {
                 check=x/nextf;
                next=c/nextf;
                nextf+=f;
                next1=x/nextf;
                sum=next+next1;
               // printf("%.7Lf ",check);
                //cout<<nextf<<" "<<next<<" "<<next1<<" "<<sum<<" "<<check<<"\n";
                if(check<sum){
                    f=1;
                    break;
                }
                ans+=next;

             }
             if(f)
             ans+=check;

                printf("Case #%d: %.7Lf\n",y,ans);
           }


return 0;
}
