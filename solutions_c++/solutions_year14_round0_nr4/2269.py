#include<algorithm>
#include<vector>
#include<stdio.h>
#include<set>
#include<map>
#define pb push_back
using namespace std;
int T,a,x,ind,good,bad,N,ag=0;
vector<double> v1,v2,va,vb;
void cpy(){
    va.clear();vb.clear();
    for(int i=0;i<v1.size();++i){
        va.pb(v1[i]);
        vb.pb(v2[i]);
    }
}
void do_bad(double x){
    if(va[va.size()-1] < x)
    {
     va.erase(va.begin());
     ++bad;

    }else{
        for(int i=0;i<va.size();++i){
            if(va[i] > x){
                va.erase(va.begin() + i);
                ++ag;
                return;
            }
        }
    }
}
void calculate_bad(){
    for(int i=0;i<v1.size();++i)
    {
        do_bad(v1[i]);
    }
}
void tryother(){
    cpy();
    ag=0;
    for(int i=0;i<vb.size();++i)
    {
        do_bad(vb[i]);
    }
    good = max(good,ag);
}
void calculate_good(){
    //printf("%lf %lf\n",v1[0],v2[v2.size()-1]);
    while(v1[0]<v2[v2.size()-1]){
        //printf("!!!");
        tryother();
        v2.erase(v2.begin() + v2.size()-1);
        v1.erase(v1.begin());

        if(v1.size() == 0)
            break;
    }
    good = max(good,(int)v2.size());
}
int main(){
    freopen("codejam.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        v1.clear();v2.clear();va.clear();
        ++ind;
        good=0;
        bad=0;
        scanf("%d",&N);
        for(int i=1;i<=N;++i){
            double x;
            scanf("%lf",&x);
            v1.pb(x);
        }
        for(int i=1;i<=N;++i){
            double x;
            scanf("%lf",&x);
            v2.pb(x);
            va.pb(x);
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        sort(va.begin(),va.end());

        calculate_bad();
        int gf = bad;
        calculate_good();

        printf("Case #%d: %d %d\n",ind,good,gf);
    }
}
