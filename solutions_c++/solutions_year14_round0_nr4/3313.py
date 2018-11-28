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
    int t,n,y,i,j,ans1,ans2,pos,ctr,pos1,pos2,f,ctr1;
    get(t);
    fr(y,1,t+1){
        f=0;
        ans1=ans2=ctr=pos1=pos2=ctr1=0;
        get(n);
        l double a[n],b[n];
        fr(i,0,n)
            scanf("%Lf",&a[i]);

           fr(i,0,n)
                scanf("%Lf",&b[i]);

        sort(a,a+n);        sort(b,b+n);

             /*   fr(i,0,n)
                  cout<<a[i]<<" ";
					cout<<"\n";

			fr(i,0,n)
				cout<<b[i]<<" ";
				cout<<"\n";
*/
               pos=0;
        fr(i,0,n){
            fr(j,pos,n){
                if(b[j]>a[i]){
                    pos=j+1;
                    ctr++;
                    break;
                }
            }
            if(pos>n-1)
                break;
        }
       // cout<<pos<<" "<<j;
        ans1=n-ctr;

        ans2=ans1;

        if(n>1){
        pos1=0;
        for(i=0;i<n;i++){
            for(j=pos1;j<n;j++){

               // cout<<i<<" "<<j<<" "<<pos1<<"\n";
                if(a[j]>b[i]){
                   // cout<<"yo";
                    pos1=j+1;
						ctr1++;
                    break;
                }

            }
            if(pos1>n-1||j>n-1)
                break;

        }
			//cout<<j;

       //cout<<pos1<<" "<<i;
    		if(pos1>0)
        ans2=ctr1;
        }
        printf("Case #%d: %d %d\n",y,ans2,ans1);

    }

return 0;
}
