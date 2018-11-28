#include<stdio.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<set>
#include<iostream>
#define mmax 103
using namespace std;
char v[25010][105];
int l[25010],N,rez,d[25010],M;
string s[10101];
int maxi,maxp,T,ind;
long long bestRez=0;
long long nrRez;
int comp(int a,int b)
{
   // printf("%s %s %d\n",v[l[a]],v[l[b]],strcmp(v[l[a]],v[l[b]]));
    if(strcmp(v[a],v[b])<0)
        return 1;
        return 0;
}

int calcTrie(int N){
    rez = 0;
    for(int i=0;i<=N*2;++i){
        l[i]=0;
        d[i]=0;
    }
    for(int i=1;i<=N;++i)
    {

    int k=1;
    l[i]=i;
    while(v[i][k]!=NULL)
        {
            d[i]=k;
            ++k;
        }
        d[i]++;

    }
    sort(l+1,l+N+1,comp);
    for(int i=1;i<=N;++i)
    {
    int j=0;
    if(i==1)
    {
    rez+=d[l[i]]+1;
    }
    else
    {
    for(j=0;v[l[i]][j]==v[l[i-1]][j]&&j<min(d[l[i-1]],d[l[i]]);++j);
    rez+=d[l[i]]-j;
    }

    }
    return rez;
}
int loc[10];

void make(){


    int ret = 0;
    for(int k=0;k<M;++k){
    int nr=0;
    for(int i=1;i<=N;++i){
        if(loc[i] == k){
        ++nr;
        for(int j=0;j<s[i].size();++j){
            v[nr][j]=s[i][j];
        }
        v[nr][s[i].size()] = NULL;
        }
    }

    ret += calcTrie(nr);
    }
    //printf("%d ",ret);
    if(ret > bestRez){
        bestRez = ret;
        nrRez = 0;
    }
    if(ret == bestRez){
        ++nrRez;
    }

}

void back(int k){
    if(k == N+1){
        make();
    }else{
        for(int i=0;i<M;++i){
            loc[k]=i;
            back(k+1);
            loc[k]=0;
        }
    }
}

int main(){
    freopen("test2.in","r",stdin);
    freopen("test2.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        ++ind;
        bestRez = -1;
        nrRez = 0;
        scanf("%d%d",&N,&M);
        for(int i=1;i<=N;++i){
            cin>>s[i];
        }
        back(1);
        printf("Case #%d: %lld %lld\n",ind,bestRez,nrRez);
    }
}
