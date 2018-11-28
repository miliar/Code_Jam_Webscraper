#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
#include<vector>
#include<algorithm>
#include<sstream>
#include<cmath>
#include<queue>
using namespace std;
int ntest;
int key[202],x,n,k,req[50];
vector<int> store[50];
bool vis[3000000];
int pre[3000000];
bool flag;
string s;
void backtrack(int x){
    if(x==1) return;
    int nx = pre[x];
    //cout << x << " " << nx << endl;
    x ^= nx;
    for(int i=1; i<n; i++){
        if( (1<<i) == x){
            stringstream ss;
            ss << i;
            string str = ss.str();
            s = str + " " + s;
            break;
        }
    }
    backtrack(nx);
}

void preset(int x){
    for(int i=0; i<n; i++){
        if( x&(1<<i) ) {
            for(int j=0; j<store[i].size(); j++)
                key[store[i][j]]++;
            if(i) key[req[i]]--;
        }
    }
}

void go(int x){
    if(vis[x]) return;
    vis[x]=true;
    if(x == (1<<n)-1){
        flag=true;
        s = "";
        backtrack(x);
        cout << s << endl;
        return;
    }
    for(int i=1; i<n; i++){
        if( !(x&(1<<i))){
            memset(key,0,sizeof key);
            preset(x);
            /*cout << x  << " " << i << " " <<  "key = ";
            for(int j=0; j<n; j++){
                cout << key[j] << " ";
            }
            cout << endl;*/
            if(key[req[i]] > 0 ){
                pre[x|(1<<i)] = x;
                go(x|(1<<i));
            }
        }
    }
}


void solve(int test){
    printf("Case #%d: ",test+1);
    memset(vis,0,sizeof vis); flag=false;
    go(1);
    if(!flag){
        printf("IMPOSSIBLE\n");
    }
}

int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d\n",&ntest);
    for(int t=0; t<ntest; t++){
        scanf("%d %d",&k,&n);
        n++;
        store[0].clear();
        for(int i=0; i<k; i++){
            scanf("%d",&x);
            store[0].push_back(x);
        }
        for(int i=1; i<n; i++){
            store[i].clear();
            scanf("%d",&req[i]);
            int tmp;
            scanf("%d",&tmp);
            while(tmp--){
                scanf("%d",&x);
                store[i].push_back(x);
            }
        }
        solve(t);
    }
    return 0;
}
