#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,M,N,AMax;
    int MM[10001];
    
    cin >> T;
    for (int t=0; t<T; t++){
    cin >>N>>M;
    AMax =0;
    for (int i=0; i< N;i++){
        for (int j=0;j<M;j++){
            cin >> MM[i*M+j];
            if (MM[i*M+j] > AMax) AMax =MM[i*M+j];
        }
    }
    
    int X;
    int Cannot = 0;
    for (int a=0; a<= AMax;a++) {

    for (int i=0; i< N;i++){
        X=0;
        for (int j=0;j<M;j++){
            if (MM[i*M+j] == a) X++;
        }
        if ((X==M) ) {
            for (int j=0; j<M; j++){
                MM[i*M+j] = -1;
            }
        }
    }
        
    for (int i=0; i< M;i++){
        X=0;
        for (int j=0;j<N;j++){
            if ((MM[i+j*M] == a) || (MM[i+j*M] == -1)) X++;
        }
        if ((X==N) ) {
            for (int j=0; j<N; j++){
                MM[i+j*M] = -1;
            }
        } 
    }

    for (int i=0; i< N;i++){
        for (int j=0;j<M;j++){
            if (MM[i*M+j] == a) {
               Cannot = 1;
               i = N;
               j = M;
               a = AMax+1;
                          }
            if (MM[i*M+j] == -1) MM[i*M+j] = a+1;
        }
    }

        
    }
    
    if (Cannot==0) cout << "Case #" << (t+1) << ": YES" << endl;
     else cout << "Case #" << (t+1) << ": NO" << endl;
    
    }
    return EXIT_SUCCESS;
}
