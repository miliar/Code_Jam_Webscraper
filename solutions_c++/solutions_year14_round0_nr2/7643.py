#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<map>
#include<set>
#include<vector>

using namespace std;

typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef vector<int> vi;

#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define DFOR(i,a,b) for(int i=a;i>=b;i--)
#define mp(x,y) make_pair((int)x,(int)y)
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(x,a,b) {cout << #x << " = "; FOR(i,a,b) cout << x[i] << ' '; cout << endl;}
#define ll long long
#define DEBUG 1

int test;
double c,f,x;
double ans;
double res;
int main(){
    if (DEBUG==1){
        freopen("B-large.in","r",stdin);
        freopen("output.txt","w",stdout);
    }
    cin>>test;
    FOR(cstest,1,test){
        cin>>c>>f>>x;

        int d= (int)(x/c);
        ans=0;
        res= x/2;
        //cout<<d<<endl;
        FOR(i,0,d-1){
            ans+=c/(2+f*i);
            res= min(res,ans+ x/(2+f*(i+1)));
            //cout<<"___"<<c/(2+f*i)<<endl;
        }
        //cout<<ans<<endl;
        double mo= x-c*d;
        //cout<<mo<<endl;
        //ans+= mo/(2+f*d);
        printf("Case #%d: %.7f\n",cstest,res);
    }
    return 0;
}
