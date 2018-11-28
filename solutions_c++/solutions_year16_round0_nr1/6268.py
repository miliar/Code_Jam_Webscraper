#include <bits/stdc++.h>
using namespace std;

FILE *in;
FILE *out;

int T;
long long N, resp, act;
char snum[100];
bool arr[10], encontrado;

int suma(){
    int sum =0;
    for(int i=0; i<10; i++)
        sum+=arr[i];
    return sum;
}

void digitos(){
    int some;
    for(int i=0; i<strlen(snum); i++){
        some = snum[i] - '0';
        arr[some]=1;
    }
}

int main(){
    in = fopen("in.in","r");
    out = fopen("out.txt","w");

    fscanf(in,"%d",&T);
    for(int t=1; t<=T; t++){
        fscanf(in,"%lld",&N);
        //itoa(N,snum,10);
        encontrado = 0;
        memset(arr,0,sizeof(arr));
        resp=0;
        for(int j=1; j<=100; j++){
            act = N*j;
            sprintf(snum, "%lld", act);
            digitos();
            int sum = suma();
            //printf("[%d]\n",sum);
            if(sum==10 && encontrado==0){
                resp=act;
                encontrado=1;
            }

        }
        if(encontrado==1)
            fprintf(out,"Case #%d: %lld\n",t,resp);
        else
            fprintf(out,"Case #%d: INSOMNIA\n",t);
    }
    return 0;
}
