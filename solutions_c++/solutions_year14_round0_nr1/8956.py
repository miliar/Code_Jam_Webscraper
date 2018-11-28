#include <cstdio>
#include <bitset>
using namespace std;

void alg(int casenum){
    int row, k = 0, l = 0, a;
    scanf("%d", &row);
    row--;
    for(int i=0; i<row; i++) scanf("%*d%*d%*d%*d");
    for(int i=0; i<4; i++){
        scanf("%d", &a);
        l |= 1<<a;
    }
    for(int i=row+1; i<4; i++) scanf("%*d%*d%*d%*d");
    //
    //
    //
    scanf("%d", &row);
    row--;
    for(int i=0; i<row; i++) scanf("%*d%*d%*d%*d");
    for(int i=0; i<4; i++){
        scanf("%d", &a);
        k|= 1<<a;
    }
    for(int i=row+1; i<4; i++) scanf("%*d%*d%*d%*d");
    k &= l;
    if(!k){
        printf("CASE #%d: Volunteer cheated!\n", casenum);
        return;
    }

    int cnt = 0;
    int res = 0, result;
    while(k && cnt<2){
        if(k%2){
            cnt++;
            result = res;
        }
        k >>= 1;
        res++;
    }
    if(cnt==1)
        printf("CASE #%d: %d\n", casenum, result);
    else
        printf("CASE #%d: Bad magician!\n", casenum);

}

int main(void){
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        alg(i+1);
    }
    return 0;
}
