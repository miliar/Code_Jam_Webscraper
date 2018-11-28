#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int main() {
    int T; cin>>T;
    for(int case_id = 1;case_id<=T;case_id++){
        int N; double V, X; cin>>N>>V>>X;
        double R[N], C[N];
        for(int i=0;i<N;i++) cin>>R[i]>>C[i];
        if (N==1){
            if (C[0]==X){
                printf("Case #%d: %f\n", case_id, V/R[0]);
            }
            else printf("Case #%d: IMPOSSIBLE\n", case_id);
            continue;
        }
        if (C[0]==X && C[1]==X){
            printf("Case #%d: %f\n", case_id, V/(R[0]+R[1]));
            continue;
        }
        if (C[0]==X){
            printf("Case #%d: %f\n", case_id, V/(R[0]));
            continue;
        }
        if (C[1]==X){
            printf("Case #%d: %f\n", case_id, V/(R[1]));
            continue;
        }
        if ((C[0]>X)==(C[1]>X)) {
            printf("Case #%d: IMPOSSIBLE\n", case_id);
            continue;
        }
        double T0 = (V-(X*V)/C[1])/(R[0]-R[0]*C[0]/C[1]);
        double T1 = (V-T0*R[0])/R[1];
        printf("Case #%d: %f\n", case_id, max(T0, T1));
        
    }
}