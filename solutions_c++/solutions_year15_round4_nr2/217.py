//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define INF 1023456789
#define eps 1e-8

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<int> vi;

int n;
double v,x,R[147], C[147];
double vyrobim;
multiset<pdd> teple;
multiset<pdd> studene;

int extra(){
    scanf("%d%lf%lf", &n, &v, &x);
    vyrobim = 0.0;
    teple.clear();
    studene.clear();

    For(i, n) {
        scanf("%lf%lf", R+i, C+i);
        C[i] -= x;
        if (C[i]<eps && -C[i]<eps) vyrobim += R[i];
        else {
            if (C[i]>0) teple.insert(pdd(C[i], R[i]));
            else studene.insert(pdd(-C[i], R[i]));
        }
    }
    // kolko dobrej vody viem vyrobit za sekundu -- to ulozim do x.
    while(teple.size() && studene.size()) {
        double tt = teple.begin()->first;
        double ts = studene.begin()->first;
        double mnozstvot = min(teple.begin()->second, studene.begin()->second*ts/tt);

        vyrobim += mnozstvot;
        vyrobim += mnozstvot*tt/ts;

        pdd itemt = *teple.begin();
        pdd items = *studene.begin();
        teple.erase(teple.begin());
        studene.erase(studene.begin());

        itemt.second -= mnozstvot;
        items.second -= mnozstvot*tt/ts;

        if (itemt.second > eps) teple.insert(itemt);
        if (items.second > eps) studene.insert(items);
    }

    // vypisem
    if (vyrobim<eps) printf("IMPOSSIBLE\n");
    else printf("%.10lf\n", v/vyrobim);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
