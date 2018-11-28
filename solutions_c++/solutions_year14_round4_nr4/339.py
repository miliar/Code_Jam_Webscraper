#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;

struct Node{
    Node* next[26];
} buf[101000];
int refCnt;
Node* newnode(){
    memset(buf[refCnt].next, 0, sizeof(buf[refCnt].next));
    return &buf[refCnt++];
}
struct Trie{
    int cnt;
    Node *root;
    void clear(){
        cnt = 0;
        
        root = newnode();
    }
    void insert(char *s){
        cnt++;
        Node *p = root;
        for (; *s; s++){
            int c = (*s)-'A';
            if (p->next[c]==NULL){
                p->next[c] = newnode();
            }
            p = p->next[c];
        }
    }
}trie[4];
char str[10][100];
int main(){
    int tt;
    int M,N,i;
    freopen("3.in","r",stdin), freopen("3.out","w",stdout);
    scanf("%d",&tt);
    for (int tcas = 1; tcas<=tt; tcas++){
        scanf("%d%d",&M,&N);
        for (i = 0;i<M;i++){
            scanf("%s",str[i]);
        }
        int size = 1;
        for (i = 0;i<M;i++)
            size*=N;
        int ans = 0, ansT = 0;
        for (int st = 0; st<size; st++){
            int tmps = st;
            refCnt = 0;
            for (i = 0;i<N;i++)
                trie[i].clear();
            for (i = 0;i<M;i++){
                int j = tmps%N;
                tmps/=N;
                trie[j].insert(str[i]);
            }
            for ( i =0;i<N;i++)
                if (trie[i].cnt==0)
                    refCnt--;
            int tmpans = refCnt;
            if (tmpans>ans){
                ans = tmpans;
                ansT = 1;
            }else if (tmpans==ans){
                ansT++;
            }
        }
        printf("Case #%d: %d %d\n", tcas, ans, ansT);
    }
}
