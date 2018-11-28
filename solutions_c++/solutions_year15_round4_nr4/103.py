#include<bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define MASK(i) (1<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define MASK_FOUR(i) (1<<(2*(i)))
#define BIT_FOUR(x,i) (((x)>>(2*(i)))&3)
#define fi   first
#define se   second
using namespace std;
const int mod=(int)1e9+7;
int r,c;
vector<int> validMask;
vector<pair<int,int> > goesTo[4141][66];
set<vector<int> > cnt;
vector<int> cur;
void init(void) {
    scanf("%d%d",&r,&c);
    validMask.clear();
    REP(i,MASK_FOUR(c)) REP(j,MASK(c)) goesTo[i][j].clear();
    cnt.clear();
    cur.assign(c,0);
}
bool isValid(int mask) {
    REP(i,c) {
        int t=BIT_FOUR(mask,i);
        int cnt=0;
        if (BIT_FOUR(mask,(i+1)%c)==t) cnt++;
        if (BIT_FOUR(mask,(i-1+c)%c)==t) cnt++;
        if (cnt>t+1) return (false);
    }
    return (true);
}
int curNeed(int prevMask,int prevNeed,int curMask) {
    REP(i,c) {
        if (BIT(prevNeed,i) && BIT_FOUR(prevMask,i)!=BIT_FOUR(curMask,i)) return (-1);
        if (!BIT(prevNeed,i) && BIT_FOUR(prevMask,i)==BIT_FOUR(curMask,i)) return (-1);
    }
    int res=0;
    REP(i,c) {
        int t=BIT_FOUR(curMask,i);
        int cnt=0;
        if (BIT_FOUR(prevMask,i)==t) cnt++;
        if (BIT_FOUR(curMask,(i+1)%c)==t) cnt++;
        if (BIT_FOUR(curMask,(i-1+c)%c)==t) cnt++;
        if (t+1-cnt!=0 && t+1-cnt!=1) return (-1);
        if (t+1-cnt==1) res|=MASK(i);
    }
    return (res);
}
void prepare(void) {
    REP(i,MASK_FOUR(c)) if (isValid(i)) validMask.push_back(i);
    REP(i,validMask.size()) REP(j,MASK(c)) REP(k,validMask.size()) {
        int tmp=curNeed(validMask[i],j,validMask[k]);
        if (tmp>=0) goesTo[validMask[i]][j].push_back(make_pair(validMask[k],tmp));
    }
}
void update(void) {
    vector<int> minRotate=cur;
    FOR(i,1,c-1) assert(cur[i]>=cur[0]);
    FOR(i,1,c-1) if (cur[i]<=cur[0]) {
        vector<int> tmp;
        REP(j,c) tmp.push_back(cur[(i+j)%c]);
        minRotate=min(minRotate,tmp);
    }
    cnt.insert(minRotate);
}
int firstNeed(int mask) {
    int res=0;
    REP(i,c) {
        int t=BIT_FOUR(mask,i);
        int cnt=0;
        if (BIT_FOUR(mask,(i+1)%c)==t) cnt++;
        if (BIT_FOUR(mask,(i-1+c)%c)==t) cnt++;
        if (t+1-cnt!=0 && t+1-cnt!=1) return (-1);
        if (t+1-cnt==1) res|=MASK(i);
    }
    return (res);
}
void backtrack(int row,int prevMask,int prevNeed) {
    FOR(i,1,c-1) if (cur[i]<cur[0]) return;
    if (row>r) {
        if (prevNeed==0) update();
        return;
    }
    if (row==1) {
        FORE(it,validMask) {
            int tmp=firstNeed(*it);
            if (tmp>=0) {
                REP(i,c) cur[i]=cur[i]*4+BIT_FOUR(*it,i);
                backtrack(row+1,*it,tmp);
                REP(i,c) cur[i]/=4;
            }
        }
    } else {
        FORE(it,goesTo[prevMask][prevNeed]) {
            int curMask=it->fi;
            int curNeed=it->se;
            REP(i,c) cur[i]=cur[i]*4+BIT_FOUR(curMask,i);
            backtrack(row+1,curMask,curNeed);
            REP(i,c) cur[i]/=4;
        }
    }
}
void process(int tc) {
    backtrack(1,0,0);
    printf("Case #%d: %d\n",tc,(int)cnt.size()%mod);
}
int main(void) {
    int t;
    scanf("%d",&t);
    FOR(i,1,t) {
        init();
        prepare();
        process(i);
    }
    return 0;
}
