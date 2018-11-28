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

#define ll long long int
#define pb push_back
#define fr(i,n)     for(int i=0;i<n;i++)
#define init(mem,v) memset(mem,v,sizeof(mem))
typedef pair<int,int> pii;

void read(){}
template<typename... T>
void read(int& head, T&... tail) {scanf("%d",&head); read(tail...);}

#if __cplusplus > 199711L
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
    #define DB(args...)
#endif

int main(){
    int t;
    read(t);
    fr(ii,t){
        int d;
        read(d);
        
        vector<int> am;
        int tmp;
        fr(i,d){
            read(tmp);
            am.push_back(tmp);
        }

        int ans=*max_element(am.begin(),am.end());

        for(int i=2;i<=ans;i++){
            int cst=i;
            for(auto e : am){
                cst+=(e-1)/i;
            }
            ans=min(ans,cst);
        }
        printf("Case #%d: %d\n",ii+1,ans);
    }
}
