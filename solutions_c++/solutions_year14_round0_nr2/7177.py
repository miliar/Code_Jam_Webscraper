#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
#define MOD 1000000009


template <typename X> X gcd(X a, X b){if(!b)return a; else return gcd(b, a%b);}

int main()
{
    int t,i=1;
    //freopen("C:/Users/UMANG JALAN/Desktop/CODE/inp.txt","r",stdin);
    //freopen("C:/Users/UMANG JALAN/Desktop/CODE/out.txt","w",stdout);
    scanf("%d",&t);
    double c,f,x;
   // setprecision();
    while(t--)
    {
       scanf("%lf %lf %lf",&c,&f,&x);
       //double time=0.0; double temp_cookie=0.0;
       double temp=2.0,ans=0.0,z,y;bool flag=false;
       while(1)
       {   z=(double)(x/temp);
           y=((double)(c/temp) +((double)(x/(temp+f)))) ;
           //cout<<z<<"\n"<<y<<"\n";
           if(z >= y ) { ans+=(c/temp); temp+=f; }
           else {ans+=x/(temp);break;}
       }
       printf("Case #%d: %.7lf\n",i,ans);i++;
    }
}
