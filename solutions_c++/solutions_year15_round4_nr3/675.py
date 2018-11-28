#include <iostream>
#include <utility>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <numeric>
#include <list>
#include <stack>
#include <cmath>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>

#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef  long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<pair<int,int> > VII;
typedef priority_queue<int> PQI;
const int Mod = 1e9 + 7;
inline LL FIX(LL a) {return (a % Mod + Mod) % Mod;}
#define MP(x,y) make_pair(x,y)
#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define take(x,y) (((x)>>(y)) & 1ll)
#define mv(n) (1<<(n))
#define what_is(x) cerr << #x << " is " << x << endl;
#define eb emplace_back
#define pb push_back
#define UNQ(x) (sort(begin(x),end(x)),x.erase(unique(begin(x),end(x)),end(x)))

char cmd[100000 + 5];
map<string,int>M;
int idx = 0;
int getidx(string x) {
    if(M.find(x) == M.end()) {
        M[x] = idx++;
        //cout << x << " " << idx - 1 << endl;
        return idx - 1;
    }
    return M[x];
}
vector<int> gao(char cmd[]) {
    int len = (int)strlen(cmd);
    string x = "";
    vector<int>ret;
    for(int i = 0;i < len;i++) {
      
        if(cmd[i] == ' ') {
            if(x != "") {
                ret.push_back(getidx(x));
            }
            /*printf("word :");
            cout << x << endl;*/
            x = "";
        }else {
            x += cmd[i];
        }
    }
    /*printf("word :");
    cout << x << endl;*/
    if(x != "")
    ret.push_back(getidx(x));
    return ret;
}
vector<int>S[1000 + 5];
int know[50000 + 5][2],unk[50000 + 5][2];
int main(){
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    int T,cas = 0;
    scanf("%d",&T);
    while(T--) {
        idx = 0;
        M.clear();
        int n;
        scanf("%d",&n);
        for(int i = 0;i < n;i++) S[i].clear();
        getchar();
        memset(know,0,sizeof(know));
        memset(unk,0,sizeof(unk));
        for(int i = 0;i < n;i++) {
            gets(cmd);
            S[i] = gao(cmd);
            /*printf("i %d\n",i);
            for(auto x : S[i]) {
                printf("%d ",x);
            }
            printf("\n");*/
            if(i == 0) {
                for(auto x : S[i]) {
                    know[x][0] = 1;
                }
            }else if(i == 1){
                for(auto x : S[i]) {
                    know[x][1] = 1;
                }
            }
        }
        int p = n - 2;
        int Min = -1;
        for(int i = 0;i < (1 << p);i++) {
            //memset(unk,0,sizeof(unk));
            for(int j = 0;j < p;j++) {
                if(take(i,j) == 0) {
                    for(auto x : S[j + 2]) {
                        unk[x][0]++;
                    }
                }else {
                    for(auto x : S[j + 2]) {
                        unk[x][1]++;
                    }
                }
            }
            int cnt = 0;
            for(int j = 0;j < idx;j++) {
                int x1 = (know[j][0] >= 1 || unk[j][0] >= 1);
                int y1 = (know[j][1] >= 1 || unk[j][1] >= 1);
                if(x1 && y1) {
                    //printf("%d : x1 %d y1 %d\n",j,x1,y1);
                    cnt++;
                }
            }
           // printf("mask %d : %d\n",i,cnt);
            if(Min == -1 || Min > cnt) Min = cnt;
            for(int j = 0;j < p;j++) {
                if(take(i,j) == 0) {
                    for(auto x : S[j + 2]) {
                        unk[x][0]--;
                    }
                }else {
                    for(auto x : S[j + 2]) {
                        unk[x][1]--;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",++cas,Min);
    }
    return 0;
}