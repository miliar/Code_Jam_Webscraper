#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define INF INT_MAX/3
#define LINF LLONG_MAX/3
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

bool ok(string s){
    for(int i=0;i<s.size();i++){
        if(s[i]=='-') return false;
    }
    return true;
}

string calc(string s,int n){
    string ss = s.substr(0,n);
    reverse(ss.begin(),ss.end());
    for(int i=0;i<n;i++){
        if(ss[i]=='+') ss[i]='-';
        else ss[i]='+';
    }
    for(int i=0;i<n;i++) s[i] = ss[i];
    return s;
}

int dfs(string s){
    if(ok(s)) return 0;
    int len = s.size();
    if(s[len-1]=='+'){
        return dfs(s.substr(0,len-1));
    }else{
        if(s[0]=='-'){
            return dfs(calc(s,len))+1;
        }else{
            int backblank = 0;
            int idx = len-1;
            while(idx>=0 && s[idx]=='-'){
                backblank++;
                idx--;
            }
            string ss = s.substr(0,len-backblank);
            string rss = calc(ss,ss.size());
            string m = "";
            for(int i=0;i<backblank;i++) m += "-";
            return dfs(rss+m)+1;
        }
    }
}

int main(){
    string s;
    int n;cin>>n;
    REP(i,n){
        cout << "Case #" << i+1 << ": ";
        cin >> s;
        cout << dfs(s) << endl;
    }
    return 0;
}
