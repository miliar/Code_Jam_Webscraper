 # /*Simplicity and Fortitude */
#include <bits/stdc++.h>
#define ff first
#define re return
#define ss second
#define pb push_back
#define mpk make_pair
#define MAXN 1000001
#define MOD 1000000007
#define couts(a) cout<<a<<endl
#define fr(i,a,b) for(ll i=a;i<b;++i)
#define rf(i,a,b) for(ll  i=a;i>=b;--i)
#define coutd(a,b) cout<<a<<" "<<b<<endl
#define ioS ios_base::sync_with_stdio(0);cin.tie(0);
#define coutt(a,b,c)cout<<a<<" "<<b<<" "<<c<<endl;
#define coutar(a,n)  fr(i,0,n)cout<<a[i]<<" ";cout<<endl;
#define coutq(a,b,c,d)cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;

# define PI 3.141592653589793238462643383279502

using namespace std;
typedef long long int ll;
typedef long double ld;
typedef pair<int,int>pi;
typedef long long int ll;
typedef vector<int> vi;

int n,a[MAXN],bo,cp;
string temp="";
vector<string>v;

int check(int x){



    fr(i,0,n){
        if(a[i]>(cp/2)){
            re 1;
        }
    }
    re 0;
}


int main(){

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;

    fr(x,1,t+1){
        v.clear();


        cin>>n;

         cp=0;

        fr(i,0,n)cin>>a[i],cp+=a[i];

   while(cp>0)
  {

        fr(i,0,n)
        {
            fr(j,0,n)
            {
                if(cp<=1)goto hell;
                if(a[i]>0){
                    a[i]--;
                    cp--;
                    bo=0;
                    //coutar(a,n);
                    bo=check(cp);
                    if(bo==1){a[i]++;cp+=1;}
                    else {temp="";temp+=char(i+65);v.pb(temp);continue;}
                }

                if(a[i]>0  && a[j]>0 && cp>=2)
                {
                    a[i]--;a[j]--;
                    cp-=2;
                    bo=0;

                    bo=check(cp);

                    if(bo==1){a[i]++;a[j]++;cp+=2;}
                    else
                    {
                        temp="";
                        temp+=char(65+i);
                        temp+=char(65+j);
                        v.pb(temp);
                    }
                }


            }
        }

  }

hell:;

   if(cp==1){fr(i,0,n)if(a[i]!=0){temp="";temp+=char(65+a[i]);v.pb(temp);}}

        cout<<"Case #"<<x<<": ";
        fr(i,0,v.size())cout<<v[i]<<" ";
        cout<<endl;
    }

}
