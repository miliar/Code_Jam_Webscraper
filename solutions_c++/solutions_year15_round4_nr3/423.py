#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <set>
#include <map>
#include <unordered_map>
using namespace std;

#define CLR(a,b) memset(a,b,sizeof(a))
const double eps = 1e-8;
const int N = 30 + 5;
int n;
char buff[100000];

int cnt[5000][2];
string w[N][3000];
int num[N][3000];
int len[N];
vector<string> pool;
map<string,int> mp;

vector<string> split(){
    int len = strlen(buff);
    vector<string> ret;
    for(int i = 0 ; i < len ;){
        int j = i;
        string word;
        while(j < len && buff[j] != ' '){
            word += buff[j];
            j ++;
        }
        if(word.length() > 0)ret.push_back(word);
        i = j + 1;
    }
    for(int i = 0 ; i < ret.size() ; i ++){
        pool.push_back(ret[i]);
    }
    return ret;
}
void solve(){
    mp.clear();
    CLR(len, 0);
    CLR(num, 0);
    CLR(cnt ,0);
    pool.clear();
    int ans = INT_MAX;
    int base = 0;
    for(int i = 0 ; i < n ; i ++){
        scanf(" %[^\n]",buff);
        vector<string> words = split();
        for(int j = 0 ; j < words.size(); j ++){
            w[i][len[i]++] = words[j];
        }
    }
    sort(pool.begin(), pool.end());
    pool.erase(unique(pool.begin(), pool.end()), pool.end());
    for(int i = 0 ; i < pool.size() ; i ++){
        mp[pool[i]] = i;
    }
    for(int i = 0 ; i < n ; i ++){
        for(int j = 0 ;j < len[i] ; j ++){
            num[i][j] = mp[w[i][j]];
            if(i <= 1){
                cnt[num[i][j]][i] ++;
                if(cnt[num[i][j]][i] == 1 && cnt[num[i][j]][i^1] > 0)
                    base ++;
            }
        }
    }
    for(int s = 0 ; s < (1<<(n-2)) ; s ++){
        int ts = 0;
        for(int j = 0 ; j < n-2 ; j ++){
            for(int k = 0 ; k < len[j+2] ; k ++){
                int curr = num[j+2][k];
                int bit = (s>>j) & 1;
                cnt[curr][bit] ++;
                if(cnt[curr][bit] == 1 && cnt[curr][bit ^ 1] > 0)ts ++;
            }
        }
        ans = min(ans, base + ts);
        for(int j = 0 ; j < n-2 ; j ++){
            for(int k = 0 ; k < len[j+2] ; k ++){
                int curr = num[j+2][k];
                int bit = (s>>j) & 1;
                cnt[curr][bit] --;
            }
        }
    }
    printf("%d\n",ans);
}
int main()
{
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d",&T);
    while(T--){
        cas ++;
        printf("Case #%d: ",cas);
        scanf("%d",&n);
        //printf("%d\n",n);
        solve();
    }
    return 0;
}