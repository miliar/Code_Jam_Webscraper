#include<cstdio>
#include<cstring>
#include<vector>

using namespace std;

int chest[1050000][50];
bool used[1050000];
int K, N;
int inbox[30][50], open[30];
int pre[1050000][2];
vector< int > key;
vector< int > path;

int relabel(int k);
void DFS(int v);

int main(){
    freopen("pdout.txt", "w", stdout);
    int T;
    int cnt = 0;
    scanf("%d", &T);
    while(T--){
        memset(chest, 0, sizeof(chest));
        memset(used, false, sizeof(used));
        memset(pre, -1, sizeof(pre));
        key.clear();
        scanf("%d%d", &K, &N);
        for(int i = 0; i < K; i++){
            int tmp;
            scanf("%d", &tmp);
            int k = relabel(tmp);
            chest[0][k]++;
        }
        memset(inbox, 0, sizeof(inbox));
        for(int i = 0; i < N; i++){
            int t1, t2;
            scanf("%d%d", &t1, &t2);
            open[i] = relabel(t1);
            for(int j = 0; j < t2; j++){
                int tt;
                scanf("%d", &tt);
                int k = relabel(tt);
                inbox[i][k]++;
            }
        }
        DFS(0);
        printf("Case #%d:", ++cnt);
        if(!used[(1<<N)-1]) printf(" IMPOSSIBLE\n");
        else{
            path.clear();
            int now = (1<<N)-1;
            while(now != 0){
                path.push_back(pre[now][1]);
                now = pre[now][0];
            }
            for(int i = N-1; i >= 0; i--) printf(" %d", path[i]+1);
            printf("\n");
        }
    }
    return 0;
}

int relabel(int k){
    for(int i = 0; i < (int)key.size(); i++){
        if(k == key[i]) return i;
    }
    key.push_back(k);
    return (int)key.size()-1;
}

void DFS(int v){
    if(used[v]) return;
    used[v] = true;
    if(used[(1<<N)-1]) return;
    for(int i = 0; i < N; i++){
        if(!(v & (1<<i))){
            if(chest[v][open[i]] > 0){
                int tar = v | (1<<i);
                for(int j = 0; j < (int)key.size(); j++){
                    chest[tar][j] = chest[v][j] + inbox[i][j];
                }
                chest[tar][open[i]]--;
                pre[tar][0] = v;
                pre[tar][1] = i;
                DFS(tar);
            }
        }
    }
}
