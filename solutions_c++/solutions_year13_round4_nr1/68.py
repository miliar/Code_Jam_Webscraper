#include <iostream>
#include <map>
#include <set>
using namespace std;
map<int,int> ptref;
set<int> pts;
long long delta[2000];
typedef struct Ride {
    int x,y, num;
};
typedef struct Pt {
    int x;
    bool type;
    bool operator<(const Ride& ride) const {
        return x<ride.x;
    }    
};
Ride rides[1000];

long long MOD = 1000002013LL;
long long locs[2000];
long long add(long long num, int x, int y) {

    long long diff = locs[y]-locs[x];
//    printf("%I64d ppl going distance of %I64d\n",num,diff);    
    diff %= MOD;
    long long diff2 = diff-1;
    if (diff%2==0) diff/=2;
    else diff2/=2;
    
    long long mul = (diff*diff2)%MOD;
    mul = (mul*num)%MOD;
    return mul;
}
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        ptref.clear();
        pts.clear();
        memset(delta,0,2000*sizeof(long long));
        int N,M; scanf("%d %d",&N,&M);
        for (int i=0; i<M; i++) {
            scanf("%d %d %d",&rides[i].x,&rides[i].y,&rides[i].num);
            pts.insert(rides[i].x);
            pts.insert(rides[i].y);            
        }
        int ct = 0;
        for (set<int>::iterator it = pts.begin(); it!=pts.end(); it++) {
            ptref[*it] = ct;
            locs[ct] = *it;
//            printf("Locs[%d]= %d\n",ct,*it);
            ct++;
        }

        long long tot1 = 0;
        long long tot2 = 0;
        
        for (int i=0; i<M; i++) {
            delta[ptref[rides[i].x]] += rides[i].num;
            delta[ptref[rides[i].y]] -= rides[i].num;  
            
            tot1 += add(rides[i].num,ptref[rides[i].x],ptref[rides[i].y]);
            tot1 %= MOD;
        }
        
//        printf("Tot1 = %I64d\n",tot1);

        for (int i=0; i<ct; i++) {
            // start at i
            long long fromi = delta[i];
//            printf("%I64d ppl start at %I64d\n",fromi,locs[i]);
            long long runningtot = fromi;
            for (int j=i+1; j<ct; j++) {
                runningtot += delta[j];
//                printf("AT %d, running tot is %I64d, fromi = %I64d\n",j,runningtot,fromi);            
                if (runningtot<fromi) {
                    tot2 += add(fromi-runningtot,i,j);
                    delta[j] += fromi-runningtot;
                    fromi=runningtot;
                }
            }
        }

        long long ans = ((tot2-tot1)%MOD+MOD)%MOD;
        printf("Case #%d: %I64d\n",t,ans);
        
        
    }
}
