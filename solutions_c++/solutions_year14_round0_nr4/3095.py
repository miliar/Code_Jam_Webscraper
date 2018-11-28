#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<double> DV;

bool comp(double a,double b){
    return (a<b);
}

void print(DV v){
    for(DV::iterator it=v.begin();it!=v.end();it++){
        printf("%lf ",*it);
    }
    printf("\n");
}

int DWar(DV a,DV b){
    int flag=0,count=0;

    for(DV::iterator it1=b.begin();it1!=b.end();){
        flag=0;
        for(DV::iterator it2=a.begin();it2!=a.end();it2++){
            if((*it1) < (*it2)){
                it1=b.erase(it1);
                it2=a.erase(it2);
                flag=1;
                count++;
                break;
            }
        }
        if(flag==0){
            break;
        }
    }
    return (count);
}

int War(DV a,DV b){
    int flag=0;

    for(DV::iterator it1=a.begin();it1!=a.end();){
        flag=0;
        for(DV::iterator it2=b.begin();it2!=b.end();it2++){
            if((*it1) < (*it2)){
                it1=a.erase(it1);
                it2=b.erase(it2);
                flag=1;
                break;
            }
        }
        if(flag==0){
            break;
        }
    }
    return (a.size());
}

int main(){
    int T,N;
    double d;
    DV v[2];

    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        scanf("%d",&N);
        for(int j=0;j<2;j++){
            for(int k=0;k<N;k++){
                scanf("%lf",&d);
                v[j].push_back(d);
            }
        }
        sort(v[0].begin(),v[0].end(),comp);
        sort(v[1].begin(),v[1].end(),comp);
        printf("Case #%d: %d %d\n",i,DWar(v[0],v[1]),War(v[0],v[1]));
        v[0].clear();
        v[1].clear();
    }
}
