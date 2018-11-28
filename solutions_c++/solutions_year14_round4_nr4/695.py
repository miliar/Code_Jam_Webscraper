//Jakub Sygnowski
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;
#define F first
#define S second
#define M 1000000007
typedef long long ll;
typedef pair<int,int> pii;
int best, ways, m, n;
string words[10];
vector<string> nodes[5];
char tab[120];
set<string> all;
int subtr(vector<string> w){
    all.clear();
    for(int i = 0; i < w.size(); i++){
        for(int j = 0; j <= w[i].size(); j++){
            all.insert(w[i].substr(0, j));
        }
    }
    return int(all.size());
}
void check(){
    int sum = 0;
/*    for(int i = 0; i < n; i++){
        printf("%d\n", i);
        for(int j = 0; j < nodes[i].size(); j++){
            printf("%s ", nodes[i][j].c_str());
        }
        printf("\n");
    }*/
    for(int i = 0; i < n; i++){
        if (!nodes[i].size())
            return;
        sum += subtr(nodes[i]);
    }
 //   printf("%d\n", sum);
    if (sum == best){
        ways++;
    }
    if (sum > best){
        best = sum;
        ways = 1;
    }
}
void backtrack(int x){
    if (x == m){
        check();
        return;
    }
    for(int i = 0; i < n; i++){
        nodes[i].push_back(words[x]);
        backtrack(x+1);
        nodes[i].pop_back();
    }
}
void solve(int test){
    best = -1; ways = 0;
    scanf("%d%d",&m, &n);
    for(int i = 0; i < n; i++){
        nodes[i].clear();
    }
    for(int i = 0; i < m; i++){
        scanf("%s", tab);
        words[i] = ((string)(tab));
    }
    backtrack(0);
    printf("Case #%d: %d %d\n", test, best, ways);
}

int main(){
    int t;
    scanf("%d",&t);
    int test;
    while(test++ < t){
        solve(test);
    }
}
