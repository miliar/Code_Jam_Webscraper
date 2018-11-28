#include<cstdio>
#include<iostream>
#include<algorithm>
#include<utility>
using namespace std;
int n;
int t,tc;
double v,x;
pair<double,double>rc[100];
bool cmp(pair<double,double>a,pair<double,double>b){
    return a.second<b.second;
}
int main(){
    scanf("%d",&tc);
    for(int ct=0;ct<tc;++ct){
        //cin>>n>>v>>x;
        scanf("%d %lf %lf",&n,&v,&x);
        //printf("-- %d %f %f\n",n,v,x);
        double avgt=0,vol=0;
        for(int i=0;i<n;++i){
            scanf("%lf%lf",&rc[i].first,&rc[i].second);
            //printf("!!! %f %f\n",rc[i].first,rc[i].second);
        }
        sort(rc,rc+n,cmp);
        if(rc[0].second>x||rc[n-1].second<x){
            printf("Case #%d: IMPOSSIBLE\n",ct+1);
            continue;
        }
        for(int i=0;i<n;++i){
            vol+=rc[i].first;
            avgt+=rc[i].first*rc[i].second;
        }
        avgt/=vol;
        // to sort first and check impossible
        if(avgt>x){
            //printf("#%d\n",ct);
            avgt=0;
            vol=0;
            for(int i=0;i<n;++i){
                if(i==0||((avgt+rc[i].first*rc[i].second)/(vol+rc[i].first)<=x+0.000000001&&i<n-1)){
                    vol+=rc[i].first;
                    avgt+=rc[i].first*rc[i].second;
                }
                else{
                    double k=(x*vol-avgt)/(rc[i].second-x);
                    if(k>rc[i].first||k<-0.1)k=rc[i].first;
                    //printf("!1 %d %d %f %f %f %f %f\n",i,n,k,vol,x,avgt,rc[i].second);
                    vol+=k;
                    break;
                }
            }
            printf("Case #%d: %.9f\n",ct+1,v/vol);
        }
        else{
            avgt=0;
            vol=0;
            for(int i=n-1;i>=0;--i){
                if(i==n-1||((avgt+rc[i].first*rc[i].second)/(vol+rc[i].first)>=x-0.000000001&&i>0)){
                    vol+=rc[i].first;
                    avgt+=rc[i].first*rc[i].second;
                }
                else{
                    double k=(x*vol-avgt)/(rc[i].second-x);
                    if(k>rc[i].first||k<-0.1)k=rc[i].first;
                    //printf("!2 %d %d %f %f %f %f %f\n",i,n,k,vol,x,avgt,rc[i].second);
                    vol+=k;
                    break;
                }
            }
            printf("Case #%d: %.9f\n",ct+1,v/vol);
        }
    }
}
