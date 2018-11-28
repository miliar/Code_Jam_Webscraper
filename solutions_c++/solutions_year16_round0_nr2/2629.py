#include <iostream>
#include<stdio.h>
#include<cstring>
#include<vector>
using namespace std;
#define nmax 11
int fact, t, nrm, nrp, putere, co[1<<nmax], put, inc, sf, rez, n, pozm, p2, y, x, nr, dist[1<<nmax], el;
char s[nmax], sir1[nmax], ss[nmax];
vector <int> ma[1<<nmax];
vector <int> ::iterator it;

int flip(int nr, int poz){
    rez++;
    put=1<<(n-1);
    for (int i=1;i<=n;i++){
        if ((nr&put)>0)
            ss[i]='+';
        else
            ss[i]='-';
        put/=2;
    }
    p2=poz;
    for (int i=1;i<=poz;i++){
        if (ss[i]=='+')
            sir1[p2]='-';
        else
            sir1[p2]='+';
        p2--;
    }
    for (int i=poz+1;i<=n;i++)
        sir1[i]=ss[i];
    x=0;
    for (int i=1;i<=n;i++)
        x=x*2+ (sir1[i]=='+');
    return x;
}

void bfs(){
    nr=0;
    for (int i=1;i<=n;i++)
        nr=nr*2+(s[i]=='+');
    for (int i=0;i<=(1<<n);i++)
        dist[i]=-1;
    dist[nr]=0;
    co[1]=nr;
    inc=sf=1;
    while (inc<=sf){
        el=co[inc]; inc++;
        for (it=ma[el].begin();it!=ma[el].end();it++){
            y=*it;
            if ((dist[y]>dist[el]+1) || (dist[y]==-1)){
                dist[y]=dist[el]+1;
                co[++sf]=y;
            }
        }
    }
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++){
        scanf("%s",s+1);
        n=strlen(s+1);
        putere=(1<<n)-1;
        for (int i=0;i<=putere;i++)
            for (int j=1;j<=n;j++){
                x=flip(i,j);
                ma[i].push_back(x);
            }
        bfs();
        rez=dist[(1<<n)-1];
        printf("Case #%d: %d\n",ii,rez);
        for (int i=1;i<=(1<<n);i++)
            ma[i].clear();
    }
    return 0;
}

