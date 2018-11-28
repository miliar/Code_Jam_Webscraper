#include <bits/stdc++.h>
#define gcd         __gcd
#define bitcount    __builtin_popcountll
#define rep(i,j,n)  for(i=j;i<n;i++)
#define tr(it,c)    for(auto it=(c).begin();it!=(c).end();it++)
#define pb          push_back
#define mp          make_pair
#define hell        1000000007
#define uset        unordered_set
#define umap        unordered_map
#define ft          first
#define sc          second
using namespace std;
typedef pair<int,int> pi;
typedef long long ll;

template <class T> T& get(T &n) {
    cin>>n;
    return n;
}

#ifdef TRACE
template<class T> ostream& printContainer(ostream &o,const T &c){
    o<<"[";
    tr(it,c){
        o<<*it<<",";
    }
    if(!c.empty())
        o<<"\b";
    o<<"]";
    return o;
}

template<class T> ostream& operator<<(ostream &o,const vector<T> &c){return printContainer(o,c);}
template<class T> ostream& operator<<(ostream &o,const deque<T> &c){return printContainer(o,c);}
template<class T> ostream& operator<<(ostream &o,const list<T> &c){return printContainer(o,c);}
template<class T> ostream& operator<<(ostream &o,const set<T> &c){return printContainer(o,c);}
template<class T> ostream& operator<<(ostream &o,const uset<T> &c){return printContainer(o,c);}
template<class T> ostream& operator<<(ostream &o,const multiset<T> &c){return printContainer(o,c);}
template<class T,class V> ostream& operator<<(ostream &o,const map<T,V> &c){return printContainer(o,c);}
template<class T,class V> ostream& operator<<(ostream &o,const umap<T,V> &c){return printContainer(o,c);}
template<class T,class V> ostream& operator<<(ostream &o,const pair<T,V> &c){return (o<<"("<<c.ft<<","<<c.sc<<")");}

#define trace(x)                 cerr << #x << ": " << x << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
#else
#define trace(x)
#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)
#endif

vector<string> chars = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void func(vector<int> &ans_vec, map<char,int> &m, char c, int N){
    while(m[c]){
        tr(it,chars[N]){
            m[*it]--;
        }
        ans_vec[N]++;
    }
}

int main() {
    int T,N,i,j;
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    get(T);
    for(int case_no=1;case_no<=T;case_no++) {
        ll ans=0;
        
        string x;
        cin>>x;N=x.size();
        map<char,int> m;
        rep(i,0,N){
            m[x[i]]++;
        }
        vector<int> ans_vec(10);
        func(ans_vec,m,'Z',0);
        func(ans_vec,m,'W',2);
        func(ans_vec,m,'X',6);
        func(ans_vec,m,'S',7);
        func(ans_vec,m,'V',5);
        func(ans_vec,m,'F',4);
        func(ans_vec,m,'R',3);
        func(ans_vec,m,'T',8);
        func(ans_vec,m,'I',9);
        func(ans_vec,m,'O',1);
        
        printf("Case #%d: ",case_no);
        rep(i,0,10){
            while(ans_vec[i]){
                printf("%d",i);
                ans_vec[i]--;
            }
        }
        printf("\n");
    }
    return 0;
}

