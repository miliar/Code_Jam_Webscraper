#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cstdarg>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;

#if __cplusplus > 199711L
    void read(){}
    template<typename... T>
    void read(int& head, T&... tail) {scanf("%d",&head); read(tail...);}

    #define DB(args...) { cerr << __LINE__<< ": "; vector<string> _v = split(#args, ','); err(_v.begin(), args); }
    vector<string> split(const string& s, char c) {
        vector<string> v;stringstream ss(s);string x;
        while (getline(ss, x, c)) v.push_back(x);
        return move(v);
    }
    void err(vector<string>::iterator it) {cerr<<endl;}
    template<typename T, typename... Args>
    void err(vector<string>::iterator it, T a, Args... args) {
        cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << "  "; err(++it, args...);
    }
#else
    #define DB(e) cerr << __LINE__ << ": " << #e << " = " << e << endl;
    void read(int& head) {scanf("%d",&head);}
#endif

#define ll long long int
#define pb push_back
#define fr(i,n)     for(int i=0;i<n;i++)
#define init(mem,v) memset(mem,v,sizeof(mem))
typedef pair<int,int> pii;

#define inf 10000
#define mx 11

bool ended(const string& s){fr(i,s.size()) if(s[i]=='-') return false; return true;}

void flip(string& s, int ps){
    fr(i,ps) s[i]=(s[i]=='-')?'+':'-';
    fr(i,ps/2) swap(s[i],s[ps-1-i]);
}

int solve(string s){
    int ans=0;
    int last=s.length();
    while(last>0 and s[last-1]=='+') last--;

    while(1){
        if(last==0) return ans;

        if(s[0]=='-'){
            flip(s,last);
            ans++;
            while(last>0 and s[last-1]=='+') last--;
        }
        else{
            int pcnt=0;
            while(s[pcnt]=='+') pcnt++;
            flip(s,pcnt);
            ans++;
        }
    }
}

int main(){
    int t;
    read(t);

    fr(ii,t){
        string s;
        cin>>s;

        printf("Case #%d: %d\n",ii+1,solve(s));
    }
}
