#include<iostream>
#include<vector>
#include<cmath>
#include<utility>
#include<string>
#include<map>
#include<fstream>
#include<set>
#include<algorithm>

using namespace std;

typedef long long ll;
typedef vector<ll> vi;
typedef vector< vi > vvi;
typedef vector< vvi > vvvi;
typedef pair<ll,ll> ii;
typedef vector<ii> vii;
typedef set<ll> si;
typedef map<string,ll> msi;

#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container),element) != container.end())

    #define INF 20000000
    #define pb push_back
    #define mp make_pair
    #define ff first
    #define ss second
    #define sz size()
    #define ln length()
    #define rep(i,n) for(ll i=0;i<n;i++)
    #define fu(i,a,n) for(ll i=a;i<=n;i++)
    #define fd(i,n,a) for(ll i=n;i>=a;i--)
    #define all(a)  a.begin(),a.end()

int main()
{
    fstream in("A-large.in");
    fstream out("output.txt");
    int t; in>>t;
    fu(kl,1,t)
    {
        int Smax;in>>Smax;
        string odience;
        in>>odience;
        vi A(Smax+1); fu(i,0,Smax)A[i]=odience[i]-'0';

        int frnds=0;
        if(A[0]<1){frnds++;A[0]++; }

        int fcount=A[0]+A[1];

        fu(i,2,Smax)
        {
            if( A[i]>0 && fcount<i) {int s=(i-fcount); fcount+=s;frnds+=s;}

            fcount+=A[i];
        }
        out<<"Case #"<<kl<<": "<<frnds<<"\n";
    }
    return 0;
}
