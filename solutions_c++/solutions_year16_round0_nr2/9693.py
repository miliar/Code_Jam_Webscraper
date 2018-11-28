#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;


int N;
string fim;

/*
00101
10100
*/

const int inf = 0x3f3f3f3f;
map<string,int> dp;

int go(string mask){
    queue<string> q;
    q.push(mask);
    string adj;
    dp.clear();
    dp[mask] = 0;
    while(!q.empty()){
        mask = q.front();
        q.pop();
        if(mask == fim) return dp[mask];
        for(int i = 1; i <= mask.length(); i++){
            adj = mask;
            reverse(adj.begin(), adj.begin()+i);
            for(int j = 0; j < i; j++) adj[j] = (adj[j]=='+') ? '-' : '+';
            if(dp.find(adj) != dp.end()) continue;
            dp[adj] = 1 + dp[mask];
            q.push(adj);

        }

    }
}

/*
int go(string mask){
    //while(!mask.empty() && mask.back() == '+') mask.pop_back();
    if(mask == fim) return 0;
    //if(mask.empty()) return 0;
    //cout << "mask: " << mask << endl;
    if(dp.count(mask)) {
        return inf;
        return dp[mask];
    }
    dp[mask] = 1;
    int ans = 0x3f3f3f3f;
   for(int i = 1; i <= mask.length(); i++){
    reverse(mask.begin(), mask.begin()+i);
    for(int j = 0; j < i; j++) mask[j] = (mask[j]=='+') ? '-' : '+';
    ans = min(ans, 1 + go(mask));
    
    reverse(mask.begin(), mask.begin()+i);
    for(int j = 0; j < i; j++) mask[j] = (mask[j]=='+') ? '-' : '+';
   }
return ans;
   return dp[mask] = ans;
}

*/

char str[100000];
int main(int argc, char const *argv[]){

    string s = "abc";

    int tt;
    scanf("%d", &tt);
    
    for(int T = 1; T <= tt; T++){
        dp.clear();
        scanf("%s", str);
        fim = "";
        for(int i = 0; i < str[i]; i++) fim.push_back('+');
        //cout << fim << endl;
        int ans = go(str);

        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}