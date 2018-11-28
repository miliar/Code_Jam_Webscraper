#include<iostream>
#include<set>
#include<algorithm>
#include<vector>
#include<queue>
#include<math.h>
#include<ctype.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int cnt[105];
struct XD{
    long long p,c;
    int type;
}data[1005];
bool cmp(XD a,XD b){
    if(a.p == b.p)return a.type < b.type;
    return a.p <b.p;
}
struct Ticket{
    long long in;
    long long c;
    bool operator<(const Ticket &tmp)const{
        return in < tmp.in;
    }
}tmp;
priority_queue<Ticket> pq;
int main (){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int T,n,m,oldm;
    long long a,b,c,MIN;
    long long right,nowc;
    int ca = 0;
    int i,j;
    long long sum,ans;
    scanf("%d",&T);
    while(T--){
        ca++;
        printf("Case #%d: ",ca);
        scanf("%d%d",&n,&m);
        memset(cnt,0,sizeof(cnt));
        sum = 0;
        for(i=0;i<m;i++){
            scanf("%lld%lld%lld",&a,&b,&c);
            sum += c*(1+b-a)*(b-a)/2;
            data[2*i].p = a;
            data[2*i].type = 0;
            data[2*i].c = c;
            data[2*i+1].p = b;
            data[2*i+1].type = 1;
            data[2*i+1].c = c;
        }
        sort(data,data+2*m,cmp);
        ans = 0;
        for(i=0;i<2*m;i++){
            if(data[i].type == 0){
                tmp.in = data[i].p;
                tmp.c = data[i].c;
                pq.push(tmp);
            }else{
                nowc = data[i].c;
                //printf("nowc %lld\n",nowc);
                while(nowc > 0){
                    if(nowc >= pq.top().c){
                        nowc -= pq.top().c;
                        ans += pq.top().c * (1+data[i].p - pq.top().in)*(data[i].p - pq.top().in)/2;
                        //printf("aa num %lld\n",data[i].p - pq.top().in);
                        pq.pop();

                    }else{
                        tmp.in = pq.top().in;
                        tmp.c = pq.top().c - nowc;

                        ans += nowc * (1+data[i].p - pq.top().in)*(data[i].p - pq.top().in)/2;
                        pq.pop();
                        pq.push(tmp);
                        nowc = 0;
                    }
                }
            }
        }

        printf("%lld\n",ans-sum);
    }
    return 0;
}
