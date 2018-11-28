#include <stdio.h>
#include <stdlib.h>
int T,M;
long long N,a,b,c;
long long p[1001][3];
int byout[1001];
int byin[1001];
long long numIn[1001],numOut[1001];
long long x1,x2;

int compareOut(const void *a , const void *b){
    return p[*(int*)a][1] - p[*(int*)b][1];
}

int compareIn(const void *a , const void *b){
    return p[*(int*)b][0] - p[*(int*)a][0];
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&T);
    for (int _T = 1;  _T <= T ; _T++){
        scanf("%lld",&N);
        scanf("%d",&M);
        for (int i  = 0 ; i < M ; i++){
            scanf("%lld %lld %lld",&p[i][0],&p[i][1],&numIn[i]);
            numOut[i] = numIn[i];
            byin[i]=i;
            byout[i] = i;
        }
        
        qsort(byout,M,sizeof(int),compareOut);
        qsort(byin,M,sizeof(int),compareIn);
        long long ans = 0;
        for (int i = 0 ; i < M ; i++){
            int bo = byout[i];
            //printf("%d[%lld]:",bo,numOut[bo]);
            for (int j = 0 ; j < M && numOut[bo] > 0; j++ ){
                int bi = byin[j];
                //printf(" %d[",bi);
                if (p[bi][0] <= p[bo][1] && numIn[bi] > 0) {
                    c = (numIn[bi] < numOut[bo])? numIn[bi] : numOut[bo];
                    numIn[bi]-= c;
                    numOut[bo]-= c;
                    x1 = 0;
                    if (bi != bo) {
                        a = p[bi][1] - p[bi][0];
                        b = p[bo][1] - p[bi][0];
                        x1 = ((a*(N+N-a+1) - b*(N+N-b+1))/2)%1000002013;
                        if (x1 < 0) x1 += 1000002013;
                        c%=1000002013;
                        ans += (x1*c)%1000002013;
                        ans %= 1000002013;
                    }
                    
                    //printf("%lld,%lld,%lld]",x1,numOut[bo],numIn[bi]);
                } else {
                    //printf("%d,0]");
                }
            }
            //printf("\n");
        }
        printf("Case #%d: %lld\n",_T,ans);
    }

}
