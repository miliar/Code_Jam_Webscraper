
/*===============*\
|  ID: TMANDZU    |
|    LANG: C++    |
\*===============*/
//Tornike Mandzulashvili
//std::ios_base::sync_with_stdio (false);

#include <bits/stdc++.h>

#define endl '\n'
#define EPS (1e-9)
#define Pi 3.14159265358979
#define INF 1000000500
#define pb push_back
#define mp make_pair
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < int , int >
#define VI vector < int >
#define DID (long long)
#define ll long long
#define AL(a) (a).begin(),(a).end()

using namespace std;

int N;
double v,x;
ll V,X,R0,V0,R1,V1;
double r0,v0,r1,v1;

void doit(double ans,int t){
 //   printf("%f\n",(R0*ans + R1*ans));
    cout<<"Case #"<<t<<": ";
    printf("%.8f\n",ans);
}

int main(){
    freopen("kiddie.in","r",stdin);
    freopen("kiddie.out","w",stdout);
    int tests;
    cin>>tests;
    for (int t = 1; t <= tests; t++){
        scanf("%d %lf %lf",&N,&v,&x);
        if (N == 1){

            scanf("%lf %lf",&r0,&v0);
            R0 = round(10000*r0);
            V0 = round(10000*v0);
            V = round(10000*v);
            X = round(10000*x);

          //  cout<<"KI"<<" "<<X<<" "<<V<<" "<<V0<<endl;

            if (V0 != X){
                cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
                continue;
            }else{
                doit(1.0*V/R0, t);
                continue;
            }


            continue;
        }
        scanf("%lf %lf",&r0,&v0);
        scanf("%lf %lf",&r1,&v1);
        R1 = round(10000*r1);
        R0 = round(10000*r0);
        V1 = round(10000*v1);
        V0 = round(10000*v0);
        V = round(10000*v);
        X = round(10000*x);
        if (V0 > V1){
            swap(R0, R1);
            swap(V0, V1);
        }
        if (V0 == X || V1 == X){
            ll flow = 0;
            if (V0 == X)
                flow += R0;
            if (V1 == X)
                flow += R1;
            doit(1.0*V/flow, t);
            continue;
        }
        if (V0 > X || V1 < X){
            cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
            continue;
        }
        double moc2 = 1.0*V*(V0 - X)/(V0 - V1);
        double moc1 = V - moc2;
        double ans = max( moc1 / R0 , moc2 / R1 );
        doit(ans, t);
    }
}







