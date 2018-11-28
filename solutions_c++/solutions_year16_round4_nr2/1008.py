#include<stdio.h>
#include<stdlib.h>

#include<algorithm>
using namespace std;
double p[222];
int N,K;
int main(){
    int T;
    scanf("%d",&T);
    for(int ca= 1;ca <=T;ca++){

        scanf("%d %d", &N, &K);
        for(int i=0;i<N;i++){
            scanf("%lf",&p[i]);
        }


        int choose[222];
        for(int i=0;i<N;i++)choose[i] = 0;
        for(int i=N - K;i<N;i++)choose[i] = 1;


        double max_p = 0.0;

        do{
        
            int yes[222];
            for(int i=0;i<K;i++)yes[i] = 0;
            for(int i=K / 2;i<K;i++)yes[i] = 1;
            double sub_p[222];
            int index = 0;
            for(int i=0;i<N;i++){
                if(choose[i] == 1){
                    sub_p[index++] = p[i];
                }
            }
            double sum_p = 0.0;
            do{
                double tmp_p = 1.0;
                for(int i=0;i<K;i++){
                    if(yes[i] == 1)
                        tmp_p *= sub_p[i];
                    else
                        tmp_p *= 1 - sub_p[i];
                }
                sum_p += tmp_p;
            } while ( next_permutation(yes, yes + K) );
            if(max_p < sum_p)max_p = sum_p;

        } while ( next_permutation(choose, choose + N) );


        
        printf("Case #%d: %lf\n", ca, max_p);

    }
    return 0;
}
