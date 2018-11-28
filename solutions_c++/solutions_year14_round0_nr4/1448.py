#include "stdio.h"
#include <algorithm>
using namespace std;
double A[1001];
double B[1001];
bool used[1001];
int main(int argc, char *argv[]){
    int T;
    scanf("%d", &T);
    for(int c=1;c<=T;++c){
        memset(used, 0, sizeof(used));
        int N;
        scanf("%d", &N);
        for(int i=0;i<N;++i){
            scanf("%lf", &A[i]);
        }
        for(int i=0;i<N;++i){
            scanf("%lf", &B[i]);
        }
        sort(A, A+N);
        sort(B, B+N);
        int dw=0;
        for(int i=0, j=0;i<N;++i){
            if(A[i]>B[j]){
                ++dw;
                ++j;
            }
        }

        int w=0;
        for(int i=N-1;i>=0;--i){
            bool lost=false;
            for(int j=0;j<N;++j){
                if((!used[j])&&(B[j]>A[i])){
                    used[j]=true;
                    lost = true;
                    break;
                }
            }
            if(!lost){
                ++w;
                for(int j=0;j<N;++j){
                    if(!used[j]){
                        used[j]=true;
                        break;
                    }
                }
            }
        }

        printf("Case #%d: %d %d\n", c, dw, w);
    }
	return 0;
}