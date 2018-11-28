#include <cstdio>
#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include <set>
#include <cmath>
#include <map>
#include <cstring>

#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)

using namespace std;

typedef pair<int,int> P;

int N,SERVERS;
string V[99];
int mx,cnt;
vector<set<int> > vc;

string to_s(int k){
    string mask = "";
    set<char> st;
    char c;
    while(k > 0){
        c = '0' + (k % SERVERS);
        mask += c;
        k/=SERVERS;
        st.insert(c);
    }

    while(mask.size() < N){
        mask += '0';
        st.insert('0');
    }

    if(st.size() < SERVERS)return "@" + mask;

    return mask;
}

int g[99999][30];
int id;//state id

void add_tree(string str){
    // cout << str << endl;
    int x = 0,y; // root
    foreach(c,str){
        y = (*c - 'A');
        // cout << *c << " " << y << endl;
        if (g[x][y] == -1) {
            g[x][y] = id;
            memset(g[id], -1, sizeof g[id]);
            id++;
        }
        x = g[x][y];
    }
}

int process_server(int S,string mask){
    memset(g[0], -1, sizeof g[0]);
    id = 1;
    for(int i=0;i<N;i++){
        if(mask[i]-'0' == S){
            add_tree(V[i]);
        }
    }
    return id;
}
void process(string mask){
    int node_count = 0;
    for(int i=0;i<SERVERS;i++){
        node_count += process_server(i,mask);
    }

    if(node_count > mx){
        mx = node_count;
        cnt = 1;
    }else if(node_count == mx){
        cnt++;
    }
}

void solve(){
    cin >> N >> SERVERS;
    for(int i=0;i<N;i++){
        cin >> V[i];
    }

    vc.clear();
    mx = 0;
    cnt=0 ;

    int lim = pow(SERVERS,N);
    string mask;
    for(int i=0;i<lim;i++){
        mask = to_s(i);
        // cout << mask << endl;
        if(mask[0] == '@')continue;
        process(mask);
    }

    printf("%d %d\n",mx,cnt);
}
int main(){
    int NC;cin >> NC;
    for(int i=1;i<=NC;i++){
        printf("Case #%d: ",i);
        solve();
    }
}