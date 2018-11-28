#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<set>
#include<map>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<iomanip>
#include<queue>
#include<stack>
#include<string.h>

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))

#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define RREPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define RFOR(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define RFOREACH(it,c) for(VAR(it,(c).rbegin());it!=(c).rend();++it)
#define CLEAR(x) memset(x,0,sizeof x);

#define MP make_pair
#define MAPI(t1,t2) map<t1,t2>::iterator
#define RMAPI(t1,t2) map<t1,t2>::reverse_iterator
#define eps 1.0e-11
#define PAUSE system("Pause");
using namespace std;

bool pal(int i){
    stringstream ss;
    ss<<i;
    string s;
    ss>>s;
    string tmp=s;
    REVERSE(s);
    return tmp==s;
}
int main(){
    int t;
    cin>>t;
    int count=0;
    
    while(t--){
        count++;
        int ans=0;
        int a,b;
        cin>>a>>b;
        map<int, bool> mp;
        mp.clear();
        for(int i=0;i<=b;i++){
            if(!mp[i]){
                if(pal(i)){
                    mp[i]=true;
                }
            }
            if(mp[i]){
                int f=i*i;
                if(f>=a && f<=b && pal(f)){
                    mp[f]=true;
                    ans++;
                }
            } 
        }
        cout<<"Case #"<<count<<": "<<ans<<endl;
        
    }
    return 0;
    
}

