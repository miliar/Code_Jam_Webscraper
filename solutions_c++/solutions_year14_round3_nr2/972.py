#include <iostream>
#include <ctype.h>
#include <stack>
#include <queue>
#include <limits.h>
#include <fstream>
#include <map>
#include <cmath>
#include <ctime>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#include <set>

#define rep(i, a) for(int i = 0; i < a; i++)
#define rep1(i, a) for(int i = 1; i <= a; i++)
#define fo(i, a, b) for(int i = a; i < b; i++)
#define defo(i, a, b) for(int i = a; i >= b; i--)
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a.size()))
#define x first
#define y second
#define SET(x, a) memset(x, a, sizeof(x));
using namespace std;

typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
int vis[12]={0},ans = 0;
vector<string> v;
int n;
int check(string s){
    int i,arr[30]={0};
    arr[s[0]-'a']++;
    for(i=1;i<s.size();i++){
        if(s[i]!=s[i-1]){
            arr[s[i]-'a']++;
        }
        if(arr[s[i]-'a']>=2){
            return 0;
        }
    }
    return 1;
}
void rec(int index,string s,set<int> se[27]){
    int i;
    if(index==n){
        int a = check(s);
        if(a==1){
            ans++;
        }
        return;
    }
    for(i=0;i<n;i++){
        if(vis[i]==0){
            vis[i] = 1;
            int x = s[s.size()-1]-'a';
            if(se[x].find(i)!=se[x].end()||se[x].size()==1){
                rec(index+1,s+v[i],se);
            }
            else {
                set<int>::iterator it;
                int fl = 0;
                for(it = se[x].begin();it!=se[x].end();it++){
                    if(vis[*it]!=1){
                        fl = 1;
                    }
                }
                if(fl==0){
                    rec(index+1,s+v[i],se);
                }
            }
            vis[i] = 0;
        }
    }
}
int main(){
    freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
    int test,l=0;
    cin>>test;
    while(test--){
        l++;
        cin>>n;
        int i,j;
        set<int> se[27];
        for(i=0;i<=11;i++){
            vis[i] = 0;
        }
        v.clear();
        ans =  0;
        for(i=0;i<n;i++){
            string s;
            cin>>s;
            for(j=0;j<s.size();j++){
                se[s[j]-'a'].insert(i);
            }
            v.push_back(s);
        }
        for(i=0;i<v.size();i++){
            vis[i] = 1;
            rec(1,v[i],se);
            vis[i] = 0;
        }
        cout<<"Case #"<<l<<": "<<ans<<"\n";
    }
    return 0;
}
