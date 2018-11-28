#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,R,N,M,K;
    int kk[13];
    int k_i;
    int nresult;
    cin >> T;
    cin >> R >> N >> M >> K;
    long RRR[100000];
    string Result[8000];
    int rrr_i;
    rrr_i=0;
    string res,res2;
    res = "";
    for (int j=0;j<N;j++){
        res = res + '2';
    }

    for (int i=0;i<R;i++){
    for (int j=0;j<K;j++){
        cin >> RRR[rrr_i];
        rrr_i++;
        Result[i] = res; 
    }
    }
    long KK[13];
    long XX;
    
    cout << "Case #1:" << endl;
    
    nresult = 0;
    for (int i=0;i<13;i++) kk[i]=2;
    int doloop;
    k_i=0;
    while ((k_i < N) && (nresult< 60)) {
    doloop = 1;
    k_i=0;
    while ((k_i < N) && (doloop)){
        if (kk[k_i]<M) {kk[k_i]++; doloop=0;}
        else {
             kk[k_i] = 2;
             k_i++; doloop=1;
             }
             
    }
    
    
    for (int i=0;i<R;i++){
        if (Result[i] == res) {
        for (int j=0; j<K;j++){
            KK[j] = RRR[i*K+j];
        }
        for (int z=0; z <N;z++){
        for (int j=z; j <N;j++){
            if (j==z) XX = kk[z]; else XX = XX * kk[j];
            
            for (int a=0; a < K; a++){
                if (XX == KK[a]) KK[a] = 1;
            }
            
        }
        }


        XX=1;
        for (int a=0; a < K; a++){
            if (KK[a]!=1) XX=0;
        }
        if (XX==1) {
        res2 = "";
        for (int a=0; a < N; a++){
            res2 = res2 + char(kk[a]+48);
        }
        if (res2 != res) nresult++;
        Result[i] = res2;
        }
        }
    }
    
    
    
    }

    for (int i=0;i<R;i++) cout << Result[i] << endl;


    return EXIT_SUCCESS;
}
