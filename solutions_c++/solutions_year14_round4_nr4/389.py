#include <iostream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;
const int MAXM = 30;
int n, m, num;
char s[MAXM];
char str[10][MAXM];

int id[MAXM];
int visit[10];
int num_m = -1, way_m = 0;

struct node {
    char* s;
    int prefix;
    bool isword;
    node* next[26];
    void init() {
        s = NULL;
        memset(next,0,sizeof(next));
    }
} a[123456], *root[4];

void insert(node *root,char *s) {
    node *p = root;
    for (int i = 0;s[i];i++) {
        int x = s[i] - 'A';
        p->s = s + i;
        if (p->next[x] == NULL) {
            a[num].init();
            p->next[x] = &a[num++];
        }
        p = p->next[x];
    }
}


void dfs(int now, int m, int n) {
    if (now == m) {
        for (int i = 0; i < n; i++) {
            if (visit[i] == 0) {
                return;
            }
        }
        int numNode = 0;
        num = 0;
        for (int i = 0; i < n; i++) {
            root[i] = &a[num++];
            root[i] -> init();
        }
        for (int i = 0; i < m; i++) {
            insert(root[id[i]], str[i]);
        }
        //numNode = num;
        if (num == num_m)
        {
            way_m++;
            
        }
        else if (num > num_m)
        {
            num_m = num;
            way_m = 1;
        }
        return;
    }
    for (int i = 0; i < n; i++) {
        id[now] = i;
        visit[i]++;
        dfs(now + 1, m, n);
        visit[i]--;
    }
}

int main() {
    int i,j,k,t,Case = 1;
    cin>>t;
    while(t--){
        num_m = -1, way_m = 0;
        cin>>m>>n;
        char temp[10];
        gets(temp);
        for (int i = 0; i < m; i++)
        {
            gets(str[i]);
        }
        for(i = 0 ; i < 10;i++)
            visit[i] = 0;
        dfs(0, m, n);
        cout<<"Case #"<<Case++<<": "<<num_m<<" "<<way_m<<endl;
        
    }
    
}