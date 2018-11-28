#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<stack>
#include<cmath>
#include<iostream>
using namespace std;

double C,F,X,M;
int ok(){
    double tp=(C/M)+(X/(M+F));
    if(X/M>tp) return 1;
    return 0;
}
int main(){
    int t,cas=1;
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    cin>>t;
    while(t--){
        cin>>C>>F>>X;
        M=2.0;
        double ans=0.0;
        while(ok()){
            ans+=C/M;
            M+=F;
        }
        ans+=X/M;
        printf("Case #%d: %lf\n",cas++,ans);
    }
}
