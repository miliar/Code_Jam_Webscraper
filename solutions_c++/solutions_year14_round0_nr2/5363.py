#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cstring>
#include <functional>
#include <cmath>
#include <iomanip>
#define CLR(a) memset(a,0,sizeof(a))
typedef long long ll;
using namespace std;
double solve(double c,double f,double x){
    double ans = 9e9;
    double tmp=0;
    for(int i=0;i<1000000;i++){
        double a = x/(2+i*f)+tmp;
        ans = min(ans,a);
        //cout<<a<<" "<<" "<<2+i*f<<tmp<<endl;
        tmp+=c/(2+i*f);
    }
    return ans;
}
int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    ios::sync_with_stdio(0);
    int t,cs=1;
    cin>>t;
    double c,f,x;
    while(cs<=t){
        cin>>c>>f>>x;
        double ans = solve(c,f,x);
        cout<<"Case #"<<cs<<": "<<fixed<<setprecision(7)<<ans<<endl;
        cs++;
    }
}