#include <iostream>
#include <string>
#include <map>
#include <queue>
using namespace std;
typedef long long ll;
int abs(int k){
    return k > 0 ? k : -k;
}
int main(){
    int t; scanf("%d",&t);
    for( int cs = 1 ; cs <= t ; ++cs ){
        map<string, int> mp;
        string s; cin >> s;
        char target_t[105];
        for( int i = 0 ; i < s.length() ; ++i ) target_t[i] = '+';
        target_t[s.length()] = '\0';
        string target = string(target_t);
        if( target.compare(s) == 0){
            printf("Case #%d: 0\n",cs);
            continue;
        }
        
        queue<pair<string,int>> q;
        q.push(make_pair(s,1));
        q.push(make_pair(target, -1));
        mp[s] = 1;
        mp[target] = -1;
        int ret = 0;
        int len = s.length();
        while(!q.empty()){
            string cur = q.front().first;
            int dir = q.front().second;
            q.pop();
            
            for( int i = 0 ; i < len ; ++i ){
                char rep[105];
                for( int j = 0 ; j <= i ; ++j ){
                    rep[i-j] = (cur[j] == '+' ? '-' : '+');
                }
                for( int j = i+1 ; j < len ; ++j ){
                    rep[j] = cur[j];
                }
                rep[len] = '\0';
                string next = string(rep);
                int &p = mp[next];
                if( mp[next] ){
                    if( p*dir >0)
                        continue;
                    else{
                        ret = abs(dir)+abs(p);
                        break;
                    }
                }
                else{
                    int d = dir>0?dir+1:dir-1;
                    mp[next] = d;
                    q.push(make_pair(next, d));
                }
            }
            if( ret != 0 ) break;
        }
        printf("Case #%d: %d\n", cs,ret-1);
    }
    return 0;
}