#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
struct TreeS{
    TreeS* next[26];
} Nodes[1000];
int totNode;
TreeS* newnode(){
    for (int i = 0;i < 26; i++)
        Nodes[totNode].next[i] = 0;
    return &Nodes[totNode++];
}
struct Trie_s{
    TreeS *root;
    void clear(){
        root = NULL;
    }
    void pushTree(char *s){
        if (root ==NULL)
            root = newnode();
        TreeS *p = root;
        for (; *s; s++){
            int c = (*s)-'A';
            if (p->next[c]==NULL){
                p->next[c] = newnode();
            }
            p = p->next[c];
        }
    }
}trie[10];
char inputS[100][100];
int M,N,i;
void work(){
    int size = 1;
    for (i = 0;i<M;i++)
        size*=N;
    int result = 0, retCnt = 0;
    for (int st = 0; st<size; st++){
        int tmps = st;
        totNode = 0;
        for (i = 0;i<N;i++)
            trie[i].clear();
        for (i = 0;i<M;i++){
            int j = tmps%N;
            tmps/=N;
            trie[j].pushTree(inputS[i]);
        }
        if (totNode>result){
            result = totNode;
            retCnt = 1;
        }else if (totNode==result){
            retCnt++;
        }
    }
    printf("%d %d\n",result, retCnt);
}
int main(){
    
    freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int t;
    scanf("%d",&t);
    for (int cas = 1; cas<=t; cas++){
        scanf("%d%d",&M,&N);
        for (i = 0;i<M;i++)
            scanf("%s",inputS[i]);
        printf("Case #%d: ", cas);
        work();
    }
}
