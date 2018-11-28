#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>


using namespace std;
typedef long long ll;

const int N = 3000;


int cas;
bool vis[N];
int cnt[N];

bool ok(int n){
    char s[10];
    sprintf(s,"%d",n);
    int len = strlen(s);
    //cout << s << endl;
    for(int i = 0; i < len; ++i){
        //cout << s[i] << " " << s[n-1-i] << endl;
        if(s[i] != s[len-1-i]) return false;
    }
    return true;
}

void init(){
    memset(vis, 0, sizeof(vis));
    for(int i = 1; i < 10; ++i){
        if(ok(i*i))vis[i*i] = 1;
    }
    for(int i = 1; i < 10; ++i){
        int t = i*10 + i;
        if(ok(t*t) && t*t < 1000) vis[t*t] = 1;
    }
    //cout << vis[1] <<" " << vis[4] << endl;
    cnt[0] = 0;
    for(int i = 1; i <= 1000; ++i) cnt[i] = cnt[i-1] + vis[i];
}

int main(){
    int tcas = 0;
    //cout << ok(4) << endl;
    init();
    int a,b;
   
    for(cin >> cas; cas; --cas){
        cin >> a >> b;
        int ans = cnt[b] - cnt[a-1];
        printf("Case #%d: %d\n",++tcas,ans);
    }    
}

