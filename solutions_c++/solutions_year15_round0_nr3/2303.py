#include<stdio.h>

int T,L;
long long int X;

int S[10010];
int Set;
bool Sign;

int Rest;
bool Rsign;

int Qua[5][5]={{},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

int make_REST(int c)
{
    Rest=1;

    int i;
    for(i=c;i<=L;i++){
        Rest=Qua[Rest][S[i]];

        if(Rest>0) continue;

        Rest=-Rest;
        Rsign=1-Rsign;
    }
    return 0;
}

long long int check()
{
    Rest=1;
    Rsign=0;

    long long int i;
    int j;
    int c=0,now=2;
    for(i=1;i<=X;i++){
        for(j=1;j<=L;j++){
            if(c>=L*4) return 0;
            if(now==5){
                make_REST(j);
                return i;
            }

            Rest=Qua[Rest][S[j]];
            c++;
            if(Rest<0){
                Rest=-Rest;
                Rsign=1-Rsign;
            }

            if(Rest!=now) continue;
            now++;
            Rest=1;
            c=0;
        }
    }

    if(now!=5) return 0;
    else return X;
}

int make_SET()
{
    Set=S[1];
    Sign=0;

    int i;
    for(i=2;i<=L;i++){
        Set=Qua[Set][S[i]];

        if(Set>0) continue;

        Set=-Set;
        Sign=1-Sign;
    }
    return 0;
}

int Process()
{
    long long int i;
    int a=1;
    bool b=0;

    make_SET();
    if((i=check())==0) return 1;

    X-=i;
    for(i=1;i<=X%4;i++){
        a=Qua[a][Set];
        b=(b+Sign)%2;

        if(a>0) continue;

        a=-a;
        b=1-b;
    }

    Rest=Qua[Rest][a];
    Rsign=(Rsign+b)%2;

    if(Rest<0){
        Rest=-Rest;
        Rsign=1-Rsign;
    }

    if(Rest==1 && Rsign==0) return 0;
    else return 1;
}

int Input()
{
    char a;
    int i;
    scanf("%d %lld",&L,&X);

    for(i=1;i<=L;i++){
        scanf(" %c",&a);

        if(a=='i') S[i]=2;
        else if(a=='j') S[i]=3;
        else S[i]=4;
    }
    return 0;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    scanf("%d",&T);

    int i;
    for(i=1;i<=T;i++){
        Input();
        if(Process()==1) printf("Case #%d: NO\n",i);
        else printf("Case #%d: YES\n",i);
    }
    return 0;
}
