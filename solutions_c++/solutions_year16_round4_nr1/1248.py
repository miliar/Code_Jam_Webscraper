#include   <bits/stdc++.h>
#define    sf               scanf
#define    pf               printf
#define    eof              feof(stdin)
#define    gl(a)            getline(cin,a)
#define    f(a,b,c)         for(intt a=b;a<=c;a++)
#define    r(a,b,c)         for(intt a=b;a>=c;a--)
#define    it(a,b)          for(intt a=0;a<b.size();a++)
#define    s(a)             sf(inttScan,&a);
#define    s2(a,b)          s(a) s(b)
#define    s3(a,b,c)        s(a) s2(b,c)
#define    s4(a,b,c,d)      s(a) s3(b,c,d)
#define    s5(a,b,c,d,e)    s(a) s4(b,c,d,e)
#define    p(a)             pf(inttPrint,a);
#define    p2(a,b)          p(a) p(b)
#define    p3(a,b,c)        p(a) p2(b,c)
#define    p4(a,b,c,d)      p(a) p3(b,c,d)
#define    p5(a,b,c,d,e)    p(a) p4(b,c,d,e)
#define    c(a)             cerr << "{ " << #a << "=" << a << " }";
#define    c2(a,b)          c(a) c(b)
#define    c3(a,b,d)        c(a) c2(b,d)
#define    c4(a,b,d,e)      c(a) c3(b,d,e)
#define    c5(a,b,d,e,f)    c(a) c4(b,d,e,f)
#define    el               pf("\n");
#define    cel              cerr << "\n";
#define    cline            cerr << "--------------------\n";
#define    ll               long long
#define    db               double
#define    ld               long double
#define    mset(a,b)        memset(a,b,sizeof(a));
#define    allocArr(a,b)    a=(intt*)calloc(b,sizeof(intt));
#define    allocMat(a,b,c)  a=(intt**)calloc(b,sizeof(intt*));f(i,0,b-1){allocArr(a[i],c)}
#define    bo               bool operator
#define    mp               make_pair
#define    pii              pair<intt,intt>
#define    pushb            push_back
#define    pushf            push_front
#define    popb             pop_back()
#define    popf             pop_front()
#define    lowb             lower_bound
#define    upb              upper_bound
#define    fi               first
#define    se               second
#define    seed             srand(time(NULL));
#define    randl            ((ll)rand()*32768ll+(ll)rand())
#define    maxpq(T)         priority_queue<T>
#define    minpq(T)         priority_queue<T,vector<T>,greater<T>>
#define    read(a)          freopen(a,"r",stdin);
#define    write(a)         freopen(a,"w",stdout);
#define    base             257ll
#define    mod              1000000007ll
#define    mod2             1000000009ll
#define    inf              2000000000ll
#define    pi               3.141592653589793
template<typename A, typename B> inline bool mins(A &x,B y){return (x>y)?(x=y,1):0;}
template<typename A, typename B> inline bool maxs(A &x,B y){return (x<y)?(x=y,1):0;}
using namespace std;

#define usell   1

#if usell
    #define     intt        long long
    #define     inttScan    "%lld"
    #define     inttPrint   "%lld "
#else
    #define     intt        int
    #define     inttScan    "%d"
    #define     inttPrint   "%d "
#endif

void clrmem();
void prep();

intt n,r,s,p,dr[20][3],dp[20][3],ds[20][3];
string bans;

string ans(int x,string c){
    if(x==n){
        return c;
    }
    else{
        if(c=="R"){
            string a=ans(x+1,"R");
            string b=ans(x+1,"S");
            return min(a,b)+max(a,b);
        }
        if(c=="S"){
            string a=ans(x+1,"S");
            string b=ans(x+1,"P");
            return min(a,b)+max(a,b);
        }
        if(c=="P"){
            string a=ans(x+1,"P");
            string b=ans(x+1,"R");
            return min(a,b)+max(a,b);
        }
    }
}

void solve(){
    s4(n,r,p,s)
    bans="z";
    if(r>=dr[n][0] and s>=dr[n][1] and p>=dr[n][2]){
        mins(bans,ans(0,"R"));
    }
    if(r>=ds[n][0] and s>=ds[n][1] and p>=ds[n][2]){
        mins(bans,ans(0,"S"));
    }
    if(r>=dp[n][0] and s>=dp[n][1] and p>=dp[n][2]){
        mins(bans,ans(0,"P"));
    }
    if(bans=="z"){
        pf("IMPOSSIBLE\n");
    }
    else{
        cout << bans << endl;
    }
    return;
}

void clrmem(){

    return;
}

void prep(){
    dr[0][0]=1;
    ds[0][1]=1;
    dp[0][2]=1;
    f(i,1,12){
        dr[i][0]=dr[i-1][2]+dr[i-1][0];
        dr[i][1]=dr[i-1][0]+dr[i-1][1];
        dr[i][2]=dr[i-1][1]+dr[i-1][2];
        ds[i][0]=ds[i-1][2]+ds[i-1][0];
        ds[i][1]=ds[i-1][0]+ds[i-1][1];
        ds[i][2]=ds[i-1][1]+ds[i-1][2];
        dp[i][0]=dp[i-1][2]+dp[i-1][0];
        dp[i][1]=dp[i-1][0]+dp[i-1][1];
        dp[i][2]=dp[i-1][1]+dp[i-1][2];
    }
    return;
}

int main(){
    #define mode 2
    if(mode==1){
        read("A-small-attempt0.in")
        write("A-small-attempt0.out")
    }
    else if(mode==2){
        read("A-large.in")
        write("A-large.out")
    }
    prep();
    intt testN;
    s(testN)
    for(int testC=1;testC<=testN;testC++){
        cerr << "\n>>>>> Test " << testC << " <<<<<\n";
        pf("Case #%d: ",testC);
        clrmem();
        solve();
        clrmem();
    }
    return 0;
}
