#include <iostream>
#include<stdio.h>
using namespace std;
#define nmax 13

char sol[1<<nmax], v[3][1<<nmax];
int an, ac, g, ok, r, p, s, t, put[nmax], nr['Z'], n, poz;

bool comparare(int a, int b, int lg){
    for (int i=0;i<lg;i++)
        if (sol[a+i]!=sol[b+i])
            return (sol[a+i]>sol[b+i]);
}

void schimba (int a, int b, int lg){
    char aux;
    for (int i=0;i<lg;i++){
        aux=sol[a+i];
        sol[a+i]=sol[b+i];
        sol[b+i]=aux;
    }
}

void sortare(){
    for (int putere=1;putere<=put[n-1];putere*=2){
        for (poz=1;poz<=put[n];poz+=2*putere){
            if (comparare(poz,poz+putere,putere))
                schimba(poz,poz+putere,putere);
        }
    }
}

int main()
{
   // freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    scanf("%d",&t);
    put[0]=1;
    for (int i=1;i<=nmax;i++)
        put[i]=put[i-1]*2;
    int iii=0;
    while (t--){
            iii++;
        scanf("%d %d %d %d",&n,&r,&p,&s);


        g=0;
        for (int ii=1;ii<=3;ii++){
            if (ii==1)
                v[1][1]='R';
            if (ii==2)
                v[1][1]='P';
            if (ii==3)
                v[1][1]='S';
            an=1;   ac=0;
            for (int i=1;i<=n;i++){
                poz=1;
                for (int j=1;j<=put[i-1];j++){
                    if (v[an][j]=='R'){
                        v[ac][poz]='R';
                        v[ac][poz+1]='S';
                    }
                    if (v[an][j]=='S'){
                        v[ac][poz]='P';
                        v[ac][poz+1]='S';
                    }
                    if (v[an][j]=='P'){
                        v[ac][poz]='P';
                        v[ac][poz+1]='R';
                    }
                    poz+=2;
                }
                ac=1-ac;    an=1-an;
            }
            nr['R']=nr['P']=nr['S']=0;
            for (int i=1;i<=put[n];i++){
                nr[v[an][i]]++;
            }
            if ((nr['R']==r)&&(nr['S']==s)&&(nr['P']==p)){
                if (!g){
                    for (int i=1;i<=put[n];i++)
                        sol[i]=v[an][i];
                    g=1;
                }else{
                    ok=1;
                    for (int i=1;i<=put[n];i++)
                        if (sol[i]!=v[an][i])
                            ok=(sol[i]>v[an][i]);
                    if (ok){
                        for (int i=1;i<=put[n];i++)
                            sol[i]=v[an][i];
                        g=1;
                    }
                }
            }

        }
        printf("Case #%d: ",iii);
        if (g)
            sortare();
        if (g)
            for (int i=1;i<=put[n];i++)
                printf("%c",sol[i]);
        else
            printf("IMPOSSIBLE");
        printf("\n");
    }
    return 0;
}
