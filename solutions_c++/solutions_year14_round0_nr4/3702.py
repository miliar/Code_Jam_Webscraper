#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;


int T,n;

main(){
    scanf("%d",&T);
    for(int num=1;num<=T;++num){
        scanf("%d",&n);
        double t;
        vector <double> Naomi,Ken;
        for(int i=0;i<n;++i){
            scanf("%lf",&t);
            Naomi.push_back(t);
        }
        for(int i=0;i<n;++i){
            scanf("%lf",&t);
            Ken.push_back(t);
        }
        sort(Naomi.begin(),Naomi.end());
        sort(Ken.begin(),Ken.end());
        int z=0,ku=n-1;
        for(int i=n-1;i>=0;--i){
            if(Naomi[i]>Ken[ku])
                ++z;
            else
                --ku;
        }
        int y=0,ks=0;
        for(int i=0;i<n;++i){
            if(Naomi[i]>Ken[ks]){
                ++y;
                ++ks;
            }
        }

        printf("Case #%d: %d %d\n",num,y,z);



    }

}
