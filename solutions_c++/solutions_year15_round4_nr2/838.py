//
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


#define INF 2147483647
#define PI 3.1415926535897932384626433832795
long double eps = 1e-15;

#define all(cont) cont.begin(),cont.end()
#define tr(c, it) for(auto it = c.begin(); it != c.end(); it++)
#define display(c) cout<<endl;tr(c,it)cout<<*it<<' ';cout<<"\n\n";
#define F first
#define S second
#define mp make_pair

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { return x > 0 ? x : -x; }

//GLOBAL
#define MOD 1000002013

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int test_cases,Testno;


    int n,i;
    long double r[200],x[100],vv,xx,maxx,minn,v1,v2,flow;

    cin>>test_cases;
    for(Testno=1;Testno<=test_cases;Testno++)
    {
        printf("Case #%d: ",Testno);
//___________________________________________
        cin>>n>>vv>>xx;
        maxx=-1;minn=1000000;
        for(i=0;i<n;i++){
            cin>>r[i]>>x[i];
            maxx=max(maxx,x[i]);
            minn=min(minn,x[i]);
        }
        if(xx>maxx || xx<minn){cout<<"IMPOSSIBLE";goto Done;}

        if(n==1){
            cout<<setprecision(20)<<fixed<<vv/r[0];
        }
        else{
            if(xx==x[0] || xx==x[1]){
                flow=0;
                if(xx==x[0])flow+=r[0];
                if(xx==x[1])flow+=r[1];
                cout<<setprecision(20)<<fixed<<vv/flow;
                goto Done;
            }
            if(x[0]>x[1]){
                swap(x[0],x[1]);swap(r[0],r[1]);
            }
            v1=vv*(x[1]-xx)/(x[1]-x[0]);
            v2=vv-v1;
            cout<<setprecision(20)<<fixed<<max(v1/r[0],v2/r[1]);
        }

//___________________________________________
        Done: printf("\n");
    }

return 0;
}
