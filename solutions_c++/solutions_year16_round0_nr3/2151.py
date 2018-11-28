#include <iostream>
#include<stdio.h>

using namespace std;
#define vmax 1320000
long long div[vmax], z=10, g, J, t,  baz, nr[1000], rez, n, sol[500], v[500], nrpr, pr[10000];

void ciur(){
    for (int d=2;d*d<=vmax;d++)
        if (div[d]==0){
            //printf("%d\n",d);
            for (int j=2;d*j<vmax;j++)
                div[d*j]=d;
            pr[++nrpr]=d;
        }
}

void inmultire(long long a){
    long long t=0, k=0;
    for (int i=1;i<=nr[0];i++){
        k=a*nr[i]+t;
        nr[i]=k%z;
        t=k/z;
    }
    while (t){
        nr[++nr[0]]=t%z;
        t/=z;
    }
}

void adunare(long long a){
    long long t=a, k=0;
    for (int i=1;i<=nr[0];i++){
        k=nr[i]+t;
        nr[i]=k%z;
        t=k/z;
    }
    while (t){
        nr[++nr[0]]=t%z;
        t/=z;
    }
}

long long rest(long long a){
    long long r=0;
    for (int i=nr[0];i>=1;i--){
        r=(r*z+nr[i])%a;
    }
    return r;
}

void verificare(){
    bool ok=1;
    for (baz=2;baz<=10;baz++){
        for (int i=1;i<=100;i++)
            nr[i]=0;
        nr[0]=1;    nr[1]=0;
        for (int i=1;i<=n;i++){
            inmultire(baz);
            adunare(sol[i]);
        }

        g=0;
        for (int i=1;i<=nrpr;i++)
            if (rest(pr[i])==0){
                g=1;
                v[baz]=pr[i];
                break;
            }
        if (!g){
            ok=0;
            break;
        }

    }
    if (ok){
        for (int i=1;i<=n;i++)
            printf("%d",sol[i]);
        for (int baz=2;baz<=10;baz++)
            printf(" %d",v[baz]);
        printf("\n");
        rez++;
    }
}

bool gen(int poz){
    if (poz==n)
        verificare();
    else{
        sol[poz]=0;
        if (rez<J)
            gen(poz+1);
        sol[poz]=1;
        if (rez<J)
            gen(poz+1);
    }
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    ciur();

    scanf("%d",&t);
    scanf("%d %d",&n,&J);
    sol[1]=1;   sol[n]=1;
    printf("Case #1:\n");
    gen(2);
    return 0;
}
