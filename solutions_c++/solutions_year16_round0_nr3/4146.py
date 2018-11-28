#include<cstdio>
#include<cmath>
int siz,allex,cnt=0,data[150];
long long numbase[150]={},divi[150]={};
bool prime;

long long gupow(long long a , int t){
    int temp = a;
    a=1;
    for(int i=0;i<t;++i){
        a*=temp;
    }
    return a;
}

void loop(int lvl){
    if(cnt == allex)
        return;
    if(lvl == siz){
        for(int j=2;j<=10;j++){
            numbase[j]=0;
            for(int i=siz-1 ;i>=0;--i){
                numbase[j]+= data[i]*gupow(j,siz-1-i);
            }
            //printf("\n %d -> %d\n",j,numbase[j]);
            prime = true;
            for(int i=2;i<sqrt(numbase[j]);++i){
                if(numbase[j]%i == 0){
                   // printf("\n%d\n",i);
                    divi[j] = i;
                    prime = false;
                }
            }
            if(prime == true)
                break;
            if(j == 10){
                cnt++;
                //printf("\ncnt = %d\n",cnt);
                for(int i=0;i<siz;++i)
                    printf("%d",data[i]);
                for(int i=2;i<=10;++i)
                    printf(" %lld",divi[i]);
                printf("\n");
            }
        }
        return;
    }

    if(lvl == 0 || lvl == siz-1 ){
        data[lvl] = 1;
        loop(lvl+1);
        if(cnt == allex)
            return;
    }
    else{
        data[lvl] = 0;
        loop(lvl+1);
        if(cnt == allex)
            return;
        data[lvl] = 1;
        loop(lvl+1);
        if(cnt == allex)
            return;
    }
    return;

}

int main()
{
    //freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out.txt","w",stdout);
    int allt;
    scanf("%d%d%d",&allt,&siz,&allex);
    printf("Case #1:\n");
    loop(0);
    return 0;
}
