#include <bits/stdc++.h>

using namespace std;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    double dyn[205][205];
double arras[205];

    int testCases;
    cin >> testCases;
    int testCase=1;
    while(testCases--){

       double mentos=0;
       int n,k;
       cin >> n >> k;
       for(int i=1;i<=n;++i)
        cin >> arras[i];
       sort(arras+1,arras+n+1);
       vector<double> vecs;

       for(int i=0;i<=k;++i){vecs.clear();
        for(int j=1;j<=i;++j){
            vecs.push_back(arras[j]);
        }
        for(int j=n;j>n-k+i;--j){
            vecs.push_back(arras[j]);
        }
        dyn[0][0]=1.0;
        for(int j=1;j<=k;++j){dyn[j][0]=0;
            double vars1=vecs[j-1];
            for(int l=0;l<=min(j,k/2);++l){
                dyn[j][l+1]=vars1*dyn[j-1][l];
                dyn[j][l]+=(1-vars1)*dyn[j-1][l];
            }
        }
        mentos=max(dyn[k][k/2],mentos);
       }

      printf("Case #%d: %.10f\n",testCase,mentos);
      ++testCase;

    }

    return 0;
}
