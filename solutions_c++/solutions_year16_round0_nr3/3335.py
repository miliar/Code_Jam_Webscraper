#include <stdio.h>
#include <math.h>

int A[33], cnt = 0, N,J;
long checkprime (long long x){
    long i;
    for (i=2;i<=sqrt(double(x));i++){
        if(x%i == 0)
            return i;
    }
    return -1;
}

long long convert(int k){
    long long m[32];
    int i;
    m[N-1] = 1;
    for(i=N-2;i>=0;i--){
        m[i] = m[i+1]*k;
    }
    //for (i=0;i<N;i++)
        //printf("%d ",m[i]);
    //printf("\n");
    long long sum = 0;
    for(i=0;i<N;i++) {
        sum += A[i] * m[i];
    }
    //printf("%d %ld\n",k,sum);
    return sum;
}

void dfs(int i){

    long ans[10];
    int k,j;
    long check;

    if(i==N-1){
        /*printf("at n-1: ");
        for(j=0;j<N;j++)
            printf("%d",A[j]);
        printf("\n");*/

        for(k=2; k<=10; k++){
        check = checkprime(convert(k));
        if(check == -1)
            break;
        else
            ans[k-2] = check;
        }
        if (k == 11){
            cnt += 1;
            for(j=0;j<N;j++)
                printf("%d",A[j]);
            printf(" ");
            for(j=0;j<9;j++){
                printf("%d ",ans[j]);
            }
            printf("\n");
        }
        return;
    }

    else {
        if(cnt == J)
            return;
        A[i] = 0;
        dfs(i+1);

        //printf("%d change to 1\n",i);
        if(cnt == J)
            return;
        A[i] = 1;
        dfs(i+1);
    }
    /*
    if(cnt == J)
        return;
    else if (i!=N-2)
        dfs(i+1);

    if(cnt == J)
        return;
    A[i]=0;


    //for(j=0;j<N;j++)
        //printf("%d",A[j]);
    //printf("\n");

    for(k=2; k<=10; k++){
        check = checkprime(convert(k));
        if(check == -1)
            break;
        else
            ans[k-2] = check;
    }
    if (k == 11){
        cnt += 1;
        for(j=0;j<N;j++)
            printf("%d",A[j]);
        printf(" ");
        for(j=0;j<9;j++){
            printf("%d ",ans[j]);
        }
    }

    if(cnt == J)
        return;
    else if(i!= N-2)
        dfs(i+1);

    if(cnt == J)
        return;
    A[i]=1;
    for(k=2; k<=10; k++){
        check = checkprime(convert(k));
        if(check == -1)
            break;
        else
            ans[k-2] = check;
    }
    if (k == 11){
        cnt += 1;
        for(j=0;j<N;j++)
            printf("%d",A[j]);
        printf(" ");
        for(j=0;j<9;j++){
            printf("%d ",ans[j]);
        }
    }*/

}
int main()
{
    int T,i;
    scanf("%d\n%d %d",&T,&N,&J);
    //N = 3; J = 1;
    A[0] = 1;
    A[N-1] = 1;
    for (i=1;i<N-1;i++){
        A[i] = 0;
    }
    //A[0] = 1; A[1] = 2; A[2] = 3;
    //printf("%ld",convert(10));
    printf("Case #1:\n");
    dfs(1);
    return 0;
}
