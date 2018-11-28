#include<bits/stdc++.h>

//BY anin_217

using namespace std;

#define PI         2.0*acos(0.0)
#define linf       (1ll<<62)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     (A).begin(), (A).end()
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)


template <class T> inline T bigmod(T p,T e,T M)
{
    if(e==0)return 1;
    if(e%2==0){T t=bigmod(p,e/2,M);return (t*t)%M;}
    return (bigmod(p,e-1,M)*p)%M;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}



int main()
 {
 	int t,cnt=1,x,r,c;

 	freopen("abcde.txt","r",stdin);
 	freopen("out4.txt","w",stdout);

    cin>>t;
    while(t--)
    {
         cin>>x>>r>>c;
          if(x==1)
            cout<<"Case #"<<cnt++<<": GABRIEL"<<endl;

          else if(x==2)
           {
             if((r==1  && c==3 ) || (r==3  && c==1 ) || (r==1  && c==1 ) || (r==3  && c==3 ))
              cout<<"Case #"<<cnt++<<": RICHARD"<<endl;

             else
             cout<<"Case #"<<cnt++<<": GABRIEL"<<endl;
           }

           else if(x==3)
           {
            if((r==2  && c==3 ) || (r==3  && c==2 ) || (r==3  && c==3 ) || (r==3  && c==4 ) || (r==4  && c==3 ) )
            cout<<"Case #"<<cnt++<<": GABRIEL"<<endl;

            else
            cout<<"Case #"<<cnt++<<": RICHARD"<<endl;

            int wa=100000;
            }

            else
            {
             if((r==3 && c==4 ) ||  (r==4 && c==3 ) || (r==4 && c==4 ))
               cout<<"Case #"<<cnt++<<": GABRIEL"<<endl;

              else
               cout<<"Case #"<<cnt++<<": RICHARD"<<endl;
            }

            int stricjer=1000;
 	    }
 	    return 0;
 }
