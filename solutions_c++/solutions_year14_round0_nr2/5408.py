//                                                  به نام خداوند بخشنده ی مهربان
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <fstream>
#include <complex>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <deque>
#include <cmath>
#include <map>
#include <set>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vint;
const int maxn=1e5+2;
double x,f,c;
double time[2][maxn];
double calc_time(){
    double ans=999999999.00;
    time[0][0]=0.00;
    for(int i=1 ; i<=ceil(x) ; i++){
        time[0][i]=time[0][i-1];
        double per_sec=2.00+(double(i-1)*f);
        double tmp=c/per_sec;
        time[0][i]+=tmp;
    }
    time[1][0]=x/2.00;
    for(int i=1 ; i<=ceil(x) ; i++){
        double per_sec=2.00+(double(i)*f);
        time[1][i]=x/per_sec;
    }
    for(int i=0 ; i<=ceil(x) ; i++)
        ans=min(ans,time[0][i]+time[1][i]);
    return ans;
}
int main(){
    ios_base::sync_with_stdio(false);
    freopen("B-large (1).in","r",stdin);
    freopen("ans.out","w",stdout);
    int T;cin>>T;
    for(int t=1 ; t<=T ; t++){
        cin>>c>>f>>x;
        cout<<"Case #"<<t<<": ";
        cout<<fixed<<setprecision(7)<<calc_time()<<endl;
    }
    return 0;
}
