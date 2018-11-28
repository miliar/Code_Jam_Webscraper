#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<iostream>
#include<map>
#include<queue>
#include<bitset>
#include<string>
#include<stdlib.h>
#include<sstream>
#define pb push_back
using namespace std;
int cs;
long long X[37];
double an=0;
bool valid(long long v,long long B){
    int i;
    for(i=0;i<37;i++){
        if(v<=X[i])return 1;
        if(B<v-X[i])return 0;
        B-=v-X[i];
    }
    return 1;
}
void go(long long v,long long B){
    int i,j,cnt=0;
    long long res=0;
    vector<long long>d;
    for(i=0;i<37;i++){
        if(X[i]<=v){
            cnt++;
            res+=v-X[i];
            d.pb(v-X[i]);
        }
    }
    if(res>B)return;
    if(cnt==0||res==0)return;
    sort(d.begin(),d.end());
    reverse(d.begin(),d.end());
    for(i=1;i<=(int)d.size();i++){
        if(res+(int)d.size()-i>B)continue;
        double tmp=0;
        for(j=0;j<i;j++){
            tmp+=(d[j]*36.-res-((int)d.size()-i))/i;
        }
        an=max(an,tmp);
    }
}
int main(){
    int T,i,j,k,N;
    long long B;
    scanf("%d",&T);
    while(T--){
        an=0;
        scanf("%lld%d",&B,&N);
        memset(X,0,sizeof(X));
        for(i=0;i<N;i++)scanf("%lld",&X[i]);
        sort(X,X+37);
        for(i=0;i<37;i++){
            for(j=0;j<50;j++){
                if(X[i]-j>=1)go(X[i]-j,B);
            }
        }
        long long ll=0,rr=100000000000000ll;
        while(ll<rr){
            long long mm=(ll+rr+1)/2;
            if(valid(mm,B))ll=mm;
            else rr=mm-1;
        }
        for(i=0;i<50;i++){
            if(ll-i>0)go(ll-i,B);
        }
        printf("Case #%d: %.12lf\n",++cs,an);
    }
    return 0;
}

