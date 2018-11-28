#include <cstdio>
#include <cstdlib>

int S[1100], SMax, T;

int main(){
    freopen("/Users/Apple/Desktop/Programming/Codes/StandingOvation/StandingOvation/A-large.in", "r", stdin);
    freopen("/Users/Apple/Desktop/Programming/Codes/StandingOvation/StandingOvation/output.out", "w", stdout);
    scanf("%d", &T);
    for(int i=0; i<T; i++){
        int Standing = 0, Invite = 0;
        scanf("%d", &SMax);
        for(int j=0; j<SMax+1; j++)
            scanf("%1d", S+j);
        for(int j=0; j<SMax+1; j++){
            if(Standing < j){
                Invite += j-Standing;
                Standing += j-Standing;
            }
            Standing += S[j];
        }
        printf("Case #%d: %d\n", i+1, Invite);
    }
    return 0;
}
