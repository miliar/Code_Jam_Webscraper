#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

class road{
public:
    int i,a,b,p; 
    bool operator<(road r)const{
        return b>r.b;
    }
}s[2000];
int cmp(road a, road b){
    return a.a<b.a;
}
//int p[101][10001];

int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        int n,m;
        scanf("%d%d",&n,&m);
        long long cost=0;
        for(int i=0;i<m;i++){
            scanf("%d%d%d",&s[i].a,&s[i].b,&s[i].p);
        }
        s[m].a=2000000000;
        s[m].b=2000000000;
        s[m].p=2000000000;
        m++;
        sort(s,s+m,cmp);
        for(int i=0;i<m;i++)
            s[i].i=i;
        //puts("------------------------");
        
        long long ans =0;
        priority_queue<road> q;
        for(int i=0;i<m;i++){
            //printf("step %d: %d %d %d\n",i,s[i].a,s[i].b,s[i].p);
            while(!q.empty() && q.top().b < s[i].a){
                //printf("top1: %d %d %d\n",q.top().a,q.top().b,q.top().p);
                while(q.top().p>0){
                    int x=q.top().i;
                    road y = q.top();
                    int k=-1;
                    for(int j=0;j<i;j++)
                        if(s[j].p>0 && s[j].a<=y.b && (s[j].a>s[k].a || k<0))
                            k=j;
                    
                    long long gg = min(s[k].p,y.p);
                    
                    long long la = y.b-y.a;
                    long long lb = y.b-s[k].a;
                    if(la>lb){
                        ans -= (la+lb-1)*(la-lb)/2*gg;
                    }
                    else{
                        ans += (lb+la-1)*(lb-la)/2*gg;
                    }
                    
                    //ans -= gg*(s[k].a-s[x].a)*(s[k].b-s[x].b);

/*
                    printf("L: %lld %lld ",la,lb);
                    printf("X: %d %d %d ",y.a,y.b,y.p);
                    printf("K: %d %d %d ",s[k].a,s[k].b,s[k].p);
                    printf("GG: %lld ", gg);
                    printf("ans: %lld\n",ans);
*/

                    s[k].p -= gg;
                    y.p -= gg;
                    q.pop();
                    q.push(y);
                }
                q.pop();
                //if(!q.empty())
                //printf("top2: %d %d %d\n",q.top().a,q.top().b,q.top().p);
            }
            q.push(s[i]);
        }
        
        printf("Case #%d: %lld\n", tt, ans);
    }
    return 0;
}

/*
3
6 2
1 3 1
3 6 1
6 2
1 3 2
4 6 1
10 2
1 7 2
6 9 1
*/
