#include "stdio.h"
#include "math.h"

int T,N,J;
int jam[16],coin[14];
long long int div[9];

bool Check(){
    for(int i=0;i<9;++i){
        if(div[i]<2)
            return false;
    }
    for(int i=0;i<8;++i){
        for(int j=i+1;j<9;++j){
            if(div[i]==div[j])
                return false;
        }
    }
    return true;
}


void divi(int pos,long long int n){
    long long int sqr = sqrt(n);
    for(long long int i=2;i<sqr;++i){
        if(n%i==0){
            div[pos]=i;
        }
    }
}

long long int num(int b){
    long long int count =0,temp =1;
    for(int i=15;i>=0;--i){
        count+=jam[i]*temp;
        temp*=b;
    }
    return count;
}

void cpy(int n){
    int temp = n;
    for(int i=13;i>=0;--i){
        coin[i]=temp%2;
        temp/=2;
    }
    for(int i=0;i<14;++i){
        jam[i+1]=coin[i];
    }
    for(int i=0;i<9;++i){
        div[i]=0;
    }
}

int main(){
    FILE *out;
    out = fopen("Coin Jam.txt","w");
    jam[0]=1;jam[15]=1;
//    for(int j=0;j<16;++j){printf("%d",jam[j]);}printf("\n");
 //   scanf("%d",&T);
    T=1;
    for(int tc=0;tc<T;tc++){
//        scanf("%d %d",&N,&J);
        printf("Case #%d:\n",tc+1);
        fprintf(out,"Case #%d:\n",tc+1);
        int count =0;
        long long int res;
        for(int i=0;i<16384;++i){
            if(count==50) break;

            cpy(i);
            for(int b=2;b<=10;++b){
                res = num(b);
                divi(b-2,res);
            }
            if(Check()){
                for(int j=0;j<16;++j){
                    printf("%d",jam[j]);
                    fprintf(out,"%d",jam[j]);
                }
                for(int j=0;j<9;++j){
//                    printf(" %d",div[j]);
                    fprintf(out," %lld",div[j]);
                    printf(" %lld:%lld",num(j+2),div[j]);
                }
                printf("\n");
                fprintf(out,"\n");
                ++count;
            }
        }
    }
}
