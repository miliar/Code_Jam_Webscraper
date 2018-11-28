#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T=0;
    int K,N;
    int KK[401];
    int NN[200][401];
    int NType[200];
    int NK[200];
    int NSts[200];
    int MOVE[200];
    int KeyNeed[401];
    
    int x;

    cin >> T;
    for (int t=0; t< T; t++){
        cin >> K >> N;
        for (int i=0; i <= 400;i++) { KK[i]=0; KeyNeed[i]=0;}
        for (int i=0; i < K; i++) { cin >> x; KK[x]++; KeyNeed[x] ++;}
        for (int i=0; i < N; i++) {
            cin >> NType[i] >> NK[i];
            KeyNeed[NType[i]] --;
            for (int j=0; j < NK[i]; j ++) {cin >> NN[i][j]; KeyNeed[NN[i][j]] ++;}             
            NSts[i] = 0;
        }
        
        int MOVE_i = 0;
        int found = 0;
        int stillneed = 0;
        for (int j=0; j <=400; j++) {if (KeyNeed[j]<0) found = 1; };
        
        for (int i=0;i<=N;i++) MOVE[i]=-1;
        
        if (found==0) {
        while ((MOVE_i < N) && (MOVE_i >=0)){

        found = 0; 
        for (int i=(MOVE[MOVE_i]+1); i<N;i++) {
            if ((NSts[i]==0) && (KK[NType[i]]>0) ) {
                 MOVE[MOVE_i] = i;
                 KK[NType[i]] --;
                 for (int j=0; j < NK[i];j++){
                     KK[NN[i][j]] ++;
                 }
                 NSts[i]= 1;
                 
                 stillneed = 0;
                 if (KK[NType[i]]==0) {
                    for (int j=0; j < N;j++){
                        if ((NSts[j]==0) && (NType[j]==NType[i])) {
                             stillneed = 1;
                             j=N;       
                        }
                    }
                    for (int j=0; j <N;j++){
                        if ((NSts[j]==0) && (NType[j]!=NType[i])) {
                             for (int k=0; k < NK[j]; k++){
                                 if (NN[j][k] == NType[i]) {
                             stillneed = 0;
                             k = NK[j];       
                             j=N;
                                 }
                             }
                        }
                    }
                 }
                 MOVE_i ++;
                 MOVE[MOVE_i] = -1;
                 found = 1;
                 if (stillneed == 1) found=0;
                 i=N; 
            }
        }
        
        if (found ==0) {
            MOVE_i--;
            if (MOVE_i >= 0) {
            for (int j=0; j < NK[MOVE[MOVE_i]];j++){
                KK[NN[MOVE[MOVE_i]][j]] --;
            }
            NSts[MOVE[MOVE_i]] = 0;
            KK[NType[MOVE[MOVE_i]]] ++;
            }
        }

        }
        
        if (MOVE_i<0) cout << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;
        else {
             cout << "Case #" << (t+1) << ":";
             for (int i=0; i < N; i++){
                 cout << " " << (MOVE[i]+1);
             }
             cout << endl;
             }
             } else {
                 cout << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;   
             }
        
    }

    return EXIT_SUCCESS;
}
