#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;

int main(){
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int T,t=0;cin>>T;
    double eps=1e-6;
    while (T--) {
        t++;printf("Case #%d: ",t);
        int n;scanf("%d",&n);
        double db;
        vector<double> x;
        for (int i=0;i<n;i++) {scanf("%lf",&db);x.push_back(db);}
        sort(x.begin(),x.end());
        vector<double> y;
        for (int i=0;i<n;i++) {scanf("%lf",&db);y.push_back(db);}
        sort(y.begin(),y.end());
        vector<double> tx=x;vector<double> ty=y;
        int az=0;
        for (int i=0;i<n;i++) {
            vector<double>::iterator it=upper_bound(ty.begin(),ty.end(),x[i]);
            if (it!=ty.end()) {
                az++;
                ty.erase(it);
            } else break;
        }
        az=n-az;
        int ay=0;
        for (int i=0;i<n;i++) {
            vector<double>::iterator it=upper_bound(tx.begin(),tx.end(),y[i]);
            if (it!=tx.end()) {
                ay++;
                tx.erase(it);
            } else break;
        }
        printf("%d %d\n",ay,az);
    }
    return 0;        
}
