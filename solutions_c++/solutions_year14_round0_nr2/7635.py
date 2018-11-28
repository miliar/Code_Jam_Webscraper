#include<bits/stdc++.h>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 long long
#define u64 unsigned i64

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
  double C,F,X;
  int t,cs = 1;
    cin>>t;
    while(t--){
        cin>>C>>F>>X;
        double sp = 2;
        double sum = 0;
        double last = X/sp;
        while(1){
            double P = C / sp;
            sum+=P;
            sp+=F;
            double now = sum + X/sp;
            if(now + eps < last){
                last = now;
            }
            else break;
        }
        printf("Case #%d: %.7lf\n",cs++,last+eps);
    }
	return 0;
}
