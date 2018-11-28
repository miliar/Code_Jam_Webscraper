#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
#define mp make_pair
#define fs first
#define sc second
using namespace std;
int N,v[100010],aux[101000],Q[101000],p[101000],vec[101010];
long long rez;
int loc[10101];
int merge(int st,int dr)
{

int m=(st+dr)/2;
if(st>=dr)
return 0;
else
{
merge(st,m);
merge(m+1,dr);
}
for(int i=st,j=m+1,k=st;i<=m||j<=dr;)
    {
         if(j>dr||(i<=m&&v[i]<=v[j]))
            {

            aux[k++]=v[i++];
            }
            else
            {
            p[k]=1;
            Q[k]=1;
            aux[k++]=v[j++];
            }
    }


    for(int i=st;i<=dr;++i)
    {
        Q[i]+=Q[i-1];
            if(p[i]==0)
        rez+=Q[i];
    }
     for(int i=st;i<=dr;++i)
   {
    v[i]=aux[i];
   Q[i]=0;
   p[i]=0;
   }
    return 0;
}
int maxi,maxp,T,ind;
long long bestRez=0;

void make()
{
vector<pair<int,int> > first,second;
first.clear();
second.clear();
    for(int i=1;i<=N;++i){
        if(loc[i]==0)
            first.push_back(mp(vec[i],i));
        else{
            second.push_back(mp(vec[i],i));
        }
    }
    //printf("%d %d %d\n",first.size(),second.size(),N);
    sort(first.begin(),first.end());
    sort(second.begin(),second.end());
    reverse(second.begin(),second.end());
    int start=0;
    for(int i=1;i<=first.size();++i){
        v[++start]=first[i-1].second;
    }
    for(int i=0;i<second.size();++i){
        v[++start]=second[i].second;
    }
    rez=0;

    merge(1,start);
    if(rez < bestRez){
        bestRez=rez;
    }
}

void back(int k){
    if(k == N+1){
        make();
    }
    else if(vec[k]==maxi){
        back(k+1);
    }else{
        loc[k]=0;
        back(k+1);
        loc[k]=1;
        back(k+1);
        loc[k]=0;
    }
}
int main(){
    freopen("test.in","r",stdin);
    freopen("test3.out","w",stdout);
    scanf("%d",&T);
    while(T--){

        maxi=0;
        ++ind;
        scanf("%d",&N);
        bestRez = N*N*10;
        for(int i=1;i<=N;++i){
            scanf("%d",&vec[i]);
        }
        for(int i=1;i<=N;++i){
            if(vec[i] > maxi){
                maxi=vec[i];
                maxp=i;
            }
        }
        back(1);
        printf("Case #%d: %lld\n",ind,bestRez);
        if(bestRez == 0){
            for(int i=1;i<=N;++i){
               // printf("%d ",vec[i]);
            }
           // printf("\n");
        }
    }
}
