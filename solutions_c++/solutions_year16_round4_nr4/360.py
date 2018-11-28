#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAX = 4 + 10;

int ans = 256;
int n;

char arr[MAX][MAX];
char rec[MAX][MAX];

int val[MAX];
int hsh[MAX];

void go(int x, int y, int t){
    if(arr[x][y] == '1' && t == 0) return;
    rec[x][y] = t + '0';
    if(x == n-1 && y == n-1){
        int cnt = 0;
        for(int i = 0 ; i < n ; i++)
            for(int j = 0 ; j < n ; j++)
                if(arr[i][j] != rec[i][j])
                    cnt++;
        bool get = true;
        for(int k = 0 ; k < 5 ; k++){
            memset(val, 0, sizeof(val));
            for(int i = 0 ; i < n ; i++){
                hsh[i] = rand()%65536+1;
                for(int j = 0 ; j < n ; j++){
                    if(rec[i][j] == '1'){
                        val[j] += hsh[i];
                    }
                }
            }
            for(int i = 0 ; i < n ; i++){
                int rcnt = 0;
                for(int t = 0 ; t < n ; t++)
                    if(rec[i][t] == '1') rcnt++;
                if(rcnt == 0){get=false; break;}
                int j;
                for(j = 0 ; j < n ; j++){
                    if(rec[i][j] == '1') break;
                }
                int tmp = val[j];
                for(; j < n ; j++){
                    if(rec[i][j] == '1'){
                        int tcnt = 0;
                        for(int t = 0 ; t < n ; t++){
                            if(rec[t][j] == '1') tcnt++;
                        }
                        if(tcnt != rcnt) get = false;
                    }
                    if(rec[i][j] == '1' && val[j] != tmp) get = false;
                }
                if(!get) break;
            }
            if(!get) break;
            for(int i = 0 ; i < n ; i++){
                bool flag = false;
                for(int j = 0 ; j < n ; j++)
                    if(rec[i][j] == '1') flag = true;
                get = flag;
            }
            if(!get) break;
        }
        if(!get) return;
        ans = min(ans, cnt);
        return;
    }else if(x == n-1){
        go(0, y+1, 0);
        go(0, y+1, 1);
    }else{
        go(x+1, y, 0);
        go(x+1, y, 1);
    }
}

int main(){
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        ans = 256;
        printf("Case #%d: ", casen);
        scanf("%d", &n);
        for(int i = 0 ; i < n ; i++)
            scanf("%s", arr[i]);
        go(0, 0, 0);
        go(0, 0, 1);
        printf("%d\n", ans);
    }
    return 0;
}
