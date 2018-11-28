#include <bits/stdc++.h>
using namespace std;

//long long mod = 1000000007;
//
//long long mypow(long long a,int b){
//    if(b==0)return 1;
//    long long tmp = mypow(a,b/2);
//    tmp = (tmp*tmp)%mod;
//    return (b&1)? ((tmp*a)%mod):tmp;
//}

int main() {
    int T;
    int N;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%d",&N);
        vector<double> bob(N);
        vector<double> al(N);
        for(int i=0;i<N;i++){
            scanf("%lf",&al[i]);
        }
        for(int i=0;i<N;i++){
            scanf("%lf",&bob[i]);
        }
        sort(bob.begin(),bob.end());
        sort(al.begin(),al.end());
        int cont = 0;
        int cont2 = 0;
        int bi = 0;int ai = 0;
        while(bi<N && ai<N){
            while(bi<N && bob[bi]<al[ai])bi++;
            if(bi<N)cont2++;
            ai++;
            bi++;
        }
        for(int i=0;i<N;i++){
            if(bob[0]<al[0]){
                cont++;
                bob.erase(bob.begin()+0);
                al.erase(al.begin()+0);
            }
            else{
                bob.pop_back();
                al.erase(al.begin()+0);
            }
        }
        printf("Case #%d: %d %d\n",t,cont,N-cont2);

    }
    return 0;
}
