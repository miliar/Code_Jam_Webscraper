/*
                              _,add8ba,
                            ,d888888888b,
                           d8888888888888b                        _,ad8ba,_
                          d888888888888888)                     ,d888888888b,
                          I8888888888888888 _________          ,8888888888888b
                __________`Y88888888888888P"""""""""""baaa,__ ,888888888888888,
            ,adP"""""""""""9888888888P""^                 ^""Y8888888888888888I
         ,a8"^           ,d888P"888P^                           ^"Y8888888888P'
       ,a8^            ,d8888'                                     ^Y8888888P'
      a88'           ,d8888P'                                        I88P"^
    ,d88'           d88888P'                                          "b,
   ,d88'           d888888'                                            `b,
  ,d88'           d888888I                                              `b,
  d88I           ,8888888'            ___                                `b,
 ,888'           d8888888          ,d88888b,              ____            `b,
 d888           ,8888888I         d88888888b,           ,d8888b,           `b
,8888           I8888888I        d8888888888I          ,88888888b           8,
I8888           88888888b       d88888888888'          8888888888b          8I
d8886           888888888       Y888888888P'           Y8888888888,        ,8b
88888b          I88888888b      `Y8888888^             `Y888888888I        d88,
Y88888b         `888888888b,      `""""^                `Y8888888P'       d888I
`888888b         88888888888b,                           `Y8888P^        d88888
 Y888888b       ,8888888888888ba,_          _______        `""^        ,d888888
 I8888888b,    ,888888888888888888ba,_     d88888888b               ,ad8888888I
 `888888888b,  I8888888888888888888888b,    ^"Y888P"^      ____.,ad88888888888I
  88888888888b,`888888888888888888888888b,     ""      ad888888888888888888888'
  8888888888888698888888888888888888888888b_,ad88ba,_,d88888888888888888888888
  88888888888888888888888888888888888888888b,`"""^ d8888888888888888888888888I
  8888888888888888888888888888888888888888888baaad888888888888888888888888888'
  Y8888888888888888888888888888888888888888888888888888888888888888888888888P
  I888888888888888888888888888888888888888888888P^  ^Y8888888888888888888888'
  `Y88888888888888888P88888888888888888888888888'     ^88888888888888888888I
   `Y8888888888888888 `8888888888888888888888888       8888888888888888888P'
    `Y888888888888888  `888888888888888888888888,     ,888888888888888888P'
     `Y88888888888888b  `88888888888888888888888I     I888888888888888888'
       "Y8888888888888b  `8888888888888888888888I     I88888888888888888'
         "Y88888888888P   `888888888888888888888b     d8888888888888888'
            ^""""""""^     `Y88888888888888888888,    888888888888888P'
                             "8888888888888888888b,   Y888888888888P^
                              `Y888888888888888888b   `Y8888888P"^
                                "Y8888888888888888P     `""""^
                                  `"YY88888888888P'
                                       ^""""""""'
*/
#include <bits/stdc++.h>
using namespace std ;

#define ft first
#define sd second
#define pb push_back
#define all(x) x.begin(),x.end()

#define ull unsigned long long int
#define ui unsigned int
#define ll long long int
#define vi vector<int>
#define vii vector<pair<int,int> >
#define pii pair<int,int>
#define vl vector<ll>
#define vll vector<pair<ll,ll> >
#define pll pair<ll,ll>
#define mp make_pair

#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z)

#define scll1(x) scanf("%lld",&x)
#define scll2(x,y) scanf("%lld%lld",&x,&y)
#define scll3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)

#define pr1(x) printf("%d\n",x)
#define pr2(x,y) printf("%d %d\n",x,y)
#define pr3(x,y,z) printf("%d %d %d\n",x,y,z)

#define prll1(x) printf("%lld\n",x)
#define prll2(x,y) printf("%lld %lld\n",x,y)
#define prll3(x,y,z) printf("%lld %lld %lld\n",x,y,z)

#define pr_vec(v) for(int i=0;i<v.size();i++) cout << v[i] << " " ;

#define f_in(st) freopen(st,"r",stdin)
#define f_out(st) freopen(st,"w",stdout)

#define loop(i, a, b) for(i=a; i<b; i++)
#define pool(i, a, b) for(i=a; i>b; i--)
int main(){
ios_base::sync_with_stdio ( false );
        ll t,n,m,i,j,k,l,g,h,c,i1,s,d,v1,q,w,e,r,y,u=0,MOD=200560490130;
        cin>>t;
        while(t--){
            u++;
            cin>>n>>m;
            ll a[n];
            a[0]=1;
            a[n-1]=1;
            l=-1;
            vector<ll>v;
            while(v.size()<m){
                k=n-2;
                l++;
                j=l;
                while(j>0){
                   g=j%2;
                   a[k]=g;
                   k--;
                   j=j/2;
                }
                for(i=k;i>=1;i--){
                    a[i]=0;
                }
                c=0;
                for(i1=2;i1<=10;i1++){
                   s=0;
                   d=1;
                   for(i=n-1;i>=0;i--){
                    s+=a[i]*d;
                    d=d*i1;
                   }
                   v1=__gcd(s,MOD);
                   if(v1!=1){
                    c++;
                   }
                }
                if(c==9){
                    v.push_back(s);
                }
            }
            cout<<"Case #"<<u<<":"<<endl;
            for(i=0;i<v.size();i++){
                cout<<v[i]<<" ";
                for(i1=2;i1<=10;i1++){
                  q=v[i];
                  e=1;
                  r=0;
                  while(q>0){
                    w=q%10;
                    r+=e*w;
                    e=e*i1;
                    q=q/10;
                  }
                  for(y=2;y<=sqrt(r);y++){
                    if(r%y==0){
                        cout<<y<<" ";
                        break;
                    }
                  }
                }
                cout<<endl;
            }
        }
return 0;
}

