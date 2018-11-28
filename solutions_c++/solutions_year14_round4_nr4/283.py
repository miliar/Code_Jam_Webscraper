#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <vector>
#include <sstream>
#include <set>
#include <ctime>
#include <queue>
#include <map>
#include <cmath>
using namespace std;
const int N = 100005;
const int MOD = 1000000007;
struct Trie  {    
    Trie *next[26];  
};    
Trie *que[N],s[N],*root;   
int idx , id[N];
int ans , cnt;
int n , m;
char str[100][105];
Trie *NewNode()  {    
    Trie *tmp=&s[idx ++];    
    memset (tmp->next,NULL , sizeof (tmp->next)); 
    return tmp;    
}    
void Insert(Trie *root,char *s,int len)  { 
    Trie *p=root;    
    for(int i=0; i<len; i++){    
        if(p->next[s[i]-'A']==NULL) p->next[s[i]-'A']=NewNode();    
        p=p->next[s[i]-'A'];    
    }    
} 
void dfs (int u) {
    if (u == n) {
        vector <int> b[10];
        for (int i = 0 ; i < n ; i ++) {
            b[id[i]].push_back (i);
        }
        for (int i = 0 ; i < m ; i ++) {
            if (b[i].size() == 0)
                return ;
        }
        int tot = 0;
        for (int i = 0 ; i < m ; i ++) {
            idx = 0;
            root = NewNode ();
            for (int j = 0 ; j < b[i].size() ; j ++)
                Insert (root , str[b[i][j]] , strlen (str[b[i][j]]));
            tot += idx;
        }
        if (tot == ans) cnt ++;
        else if (tot > ans) {
            ans = tot;
            cnt = 1;
        }
        return ;
    }
    for (int i = 0 ; i < m ; i ++) {
        id[u] = i;
        dfs (u + 1);
    }
}
int main(){
    // freopen("input.txt" , "r" , stdin);
    // freopen("D.out" , "w" , stdout);
    int t , cas = 0;
    scanf ("%d" , &t);
    while (t --) {
        scanf ("%d %d" , &n , &m);
        for (int i = 0 ; i < n ; i ++) {
            scanf ("%s" , str[i]);
        }
        ans = 0;cnt = 0;
        dfs (0);
        printf ("Case #%d: %d %d\n" , ++cas , ans , cnt);
    }
    return 0;
}
