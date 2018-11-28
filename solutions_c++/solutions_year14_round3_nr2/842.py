#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#define MOD 1000000007

using namespace std;

vector<int> perm;
char tr[10][120];
char str[1010];

int check(void){
    long long int res = 0;
    vector<int> tmp;
    tmp.clear();
    int arr[100];
    for(int i = 0; i < perm.size(); i++)
        tmp.push_back(perm[i]);
    do{
        int flag = 1;
        for(int i = 1; i < tmp.size(); i++){
            if(tr[tmp[i]][0] == tr[tmp[i-1]][strlen(tr[tmp[i-1]])-1]) continue;
            else flag = 0;
        }
        res += flag;
        res %= MOD;
        puts("====");
        for(int i = 0; i < tmp.size(); i++) printf("%d ", tmp[i]);
        printf("%d\n", flag);
        puts("====");

    }while(next_permutation(tmp.begin(), tmp.end()));
    return res;
}

long long int Build(int num, int N, int now){
    long long int tmp = 0;
    perm.push_back(now);
    if(perm.size() == num){
        tmp += check();
        tmp %= MOD;
    }
    for(int i = now+1; i < N; i++)
        tmp += Build(num, N, i);
    perm.pop_back();
    return tmp;
}

int checkstr(void){
    int flag = 1;
    int vis[100];
    for(int i = 0; i < 100; i++) vis[i] = 0;
    int len = strlen(str);
    vis[str[0]-'a'] = 1;
    for(int i = 1; i < len; i++){
        if(str[i] == str[i-1]) continue;
        vis[str[i]-'a']++;
    }
    for(int i = 0; i < 100; i++)
        if(vis[i] > 1) flag = 0;
    return flag;
}

void solve(void){
    long long int res = 0;
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; i++)
        memset(tr[i], 0, sizeof(tr[i]));
    for(int i = 0; i < N; i++)
        scanf("%s", tr[i]);
    /*
    for(int i = 2; i <= N; i++)
        for(int j = 0; j < N-i+1; j++){
            res += Build(i, N, j);
            res %= MOD;
        }
    */
    perm.clear();
    for(int i = 0; i < N; i++) perm.push_back(i);
    do{
        int flag = 1;
        memset(str, 0, sizeof(str));
        for(int i = 0; i < N; i++)
            strcat(str, tr[perm[i]]);
        res += checkstr();
        flag = 0;
    }while(next_permutation(perm.begin(), perm.end()));

    printf("%lld\n", res);
    return;
}

int main(void){
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
