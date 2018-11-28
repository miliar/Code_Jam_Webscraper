#include<bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define MASK(i) (1<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define fi   first
#define se   second
using namespace std;
const int INF=(int)1e9+7;
map<string,pair<int,int> > word;
int n;
vector<string> readLine(void) {
    string inp,tmp;
    getline(cin,inp);
    //cerr<<"READ: "<<inp<<endl;
    stringstream ss(inp);
    vector<string> res;
    while (ss>>tmp) res.push_back(tmp);
    return (res);
}
void init(void) {
    cin>>n;
    string xxx;
    getline(cin,xxx);
    word.clear();
    REP(i,2) {
        vector<string> sen=readLine();
        FORE(it,sen) word[*it].se|=MASK(i);
    }
    REP(i,n-2) {
        vector<string> sen=readLine();
        FORE(it,sen) word[*it].fi|=MASK(i);
    }
}
int calc(int mask) {
    int tmp=(MASK(n-2)-1)^mask;
    int res=0;
    FORE(it,word) {
        //printf("Cur %s: %d %d\n",it->fi.c_str(),it->se.fi,it->se.se);
        bool isEng=BIT(it->se.se,0) || ((it->se.fi&tmp)>0);
        bool isFre=BIT(it->se.se,1) || ((it->se.fi&mask)>0);
        if (isEng && isFre) res++;
    }
    //printf("mask %d is %d\n",mask,res);
    return (res);
}
void process(int tc) {
    int res=INF;
    REP(i,MASK(n-2)) res=min(res,calc(i));
    printf("Case #%d: %d\n",tc,res);
}
int main(void) {
    //freopen("tmp.txt","r",stdin);
    int t;
    scanf("%d",&t);
    FOR(i,1,t) {
        cerr<<i<<endl;
        init();
        process(i);
    }
    return 0;
}
