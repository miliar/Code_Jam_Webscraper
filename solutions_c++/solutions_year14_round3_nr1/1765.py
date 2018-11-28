#include<cstdio>
const int MAXN=30;
int pow[MAXN];
int gcd(int a,int b){
    if(a%b==0)return b;
    else return gcd(b,a%b);   
}
int main(){
    int N;
    for(int i=0;i<MAXN;i++){
       pow[i]=(1<<(i+1));     
    }
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        int a,b;
        char c;
        scanf("%d%c%d",&a,&c,&b);
        int g=gcd(a,b);
        a=a/g;
        b=b/g;
        bool ver=0;
        if(b==1)ver=1;
        for(int j=0;j<MAXN;j++){
            if(b==pow[j])ver=1;
        }
        for(int j=0;j<MAXN&&ver;j++){
            if((double(a*pow[j])/double(b)>=1)){
                printf("Case #%d: %d\n",i+1,j+1);
                break;
            }      
        }
        if(!ver)printf("Case #%d: impossible\n",i+1);
    }
    scanf("%.d");
    
}
