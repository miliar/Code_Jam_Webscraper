#include <stdio.h>
#include <vector>
#include <algorithm>

int main(){
    int T,t;
    int loe,loe2;
    long long A,N;
    int i,j;
    scanf("%i\n",&T);
    for(t=1;t<=T;t++){
        loe=0;
        scanf("%i %i\n",&A,&N);
        //printf("AA %i %i\n",A,N);
        std::vector<long long> aaa;
        //aaa.clear();
        for(i=0;i<N;i++){
            scanf("%i ",&j);
            aaa.push_back(j);
        }
        scanf("\n");
        std::sort(aaa.begin(),aaa.end());
       /* 
        for(i=0;i<N;i++)
            printf("%i ",aaa[i]);
        printf("\n");
       */ 
        
        if(A==1){
            loe=N;
        }
        else{
        for(i=0;i<N;i++){
            //printf("ii %i %i\n",aaa[i],A);
            if(aaa[i]<A){

            //printf("22ii %i %i\n",aaa[i],A);
                A+=aaa[i];
                continue;
            }
            loe2=loe;
            while(1){
                //printf("--AA %i %i %i\n",A,loe,aaa[i]);
                A=A+A-1;
                loe++;
                if(aaa[i]<A){
                    A+=aaa[i];
                    break;
                }
            }
            if((N-1-i+loe2)<loe && loe!=0){
                loe=loe2+N-i;
                break;
            }
        }
        }
        printf("Case #%i: %i\n",t,loe);
    }
    return 0;
}
