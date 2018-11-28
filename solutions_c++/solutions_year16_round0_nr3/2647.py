#include<cstdio>
#include<cstdlib>

using namespace std;

int n,b[100];
long long su[100];

int is_prime(long long x){
    long long i,j;

    if(x==2) return 1;
    if(x%2==0) return 0;

    for(i=3;i*i<=x;i+=2){
        if(x%i==0) return 0;
    }
    return 1;
}

int is_ok(void){
    long long i,j,x;


    for(i=2;i<=10;i++){
        su[i]=0;
        x=1;
        for(j=15;j>=0;j--){
            su[i] +=b[j]*x;
            x *=i;
        }

        if(is_prime(su[i])==1) return 0;
    }

    for(i=0;i<16;i++) printf("%d",b[i]);

    for(i=2;i<=10;i++){
        for(j=2;j*j<=su[i];j++){
            if(su[i]%j==0){
                printf(" %lld",j);
                break;
            }
        }
    }
    printf("\n");

    return 1;
}


void shin(int c){
    if(c>=15){

        if(is_ok()==1) n++;
        if(n>=50) exit(0);

        return;
    }

    b[c]=0;
    shin(c+1);

    b[c]=1;
    shin(c+1);

}

int main(void){
    int i,j,x,y,t,z;
    long long tt;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    b[0]=b[15]=1;

    scanf("%d",&t);
    printf("Case #1:\n");

    scanf("%d %d",&x,&y);

    shin(1);



    return 0;
}
