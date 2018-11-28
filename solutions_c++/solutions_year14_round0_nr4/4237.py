#include <cstdio>
#include <vector>
#include <set>
using namespace std;
int calc(vector<double> ns,vector<double> ks){
    set<double> kset;
    for(double x : ks) kset.insert(x);
    int ret=0;
    for(double x : ns){
        auto at=kset.upper_bound(x);
        if(at==kset.end()){
            ret++;
            kset.erase(kset.begin());
        }else kset.erase(at);
    }
    return ret;
}
int main(){
    int T;
    scanf("%d",&T);
    for(int ix=0;ix<T;ix++){
        printf("Case #%d: ",ix+1);
        int N;
        scanf("%d",&N);
        vector<double> ns(N),ks(N);
        for(int i=0;i<N;i++){
            scanf("%lf",&ns[i]);
        }
        for(int i=0;i<N;i++){
            scanf("%lf",&ks[i]);
        }
        sort(ns.begin(),ns.end());
        sort(ks.begin(),ks.end());
        int ansa,ansb;
        ansb=calc(ns,ks);
        int ma=0;
        for(int i=N-1;i>=0;i--){
            bool is=true;
            for(int j=0;j<N-i;j++){
                if(ks[j] > ns[j+i]) is=false;
            }
            if(is) ma=N-i;
        }
        ansa=ma;
        printf("%d %d\n",ansa,ansb);
    }
}
