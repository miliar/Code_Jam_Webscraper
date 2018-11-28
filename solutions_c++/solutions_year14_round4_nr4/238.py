#include<stdio.h>
#include<cmath>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
#include<cstring>
#define Max 100000
using namespace std;
const int maxn = 10010;
struct AC_automaton
{
    struct NODE
    {
        int cnt,id;
        NODE *fail;
        NODE *ne[26];
    }A[maxn],*Q[maxn],*root;


    int L;
    NODE *new_node(){
        NODE *ret = &A[L++];
        ret->fail = 0;
        ret->cnt = 0;
        ret->id = L-1;
        for (int i = 0;i < 26;i++){
            ret->ne[i] = 0;
        }
        return ret;
    }
    void init(){
        L = 0;
        root = new_node();
        root->fail = root;
    }
    void insert(char ch[])
    {
        int n = strlen(ch);
        NODE *now = root;
        for (int i = 0;i < n;i++){
            NODE *ne;
            if (now->ne[ch[i]-'A'] == 0){
                now->ne[ch[i]-'A'] = new_node();
            }
            now = now->ne[ch[i]-'A'];
            if (i == n-1) now->cnt++;
        }
    }
}tre[110];
bool chec[110];
char str[110][110];
int n,m;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas = 1;
    while (T--) {
        scanf("%d%d",&m,&n);
        for (int i = 0; i < m; i++) {
            scanf("%s",str[i]);
        }
        int tot = 1;
        for (int i = 0; i < m; i++) tot *= n;
        int ans = 0,ans1 = 1;
       // continue;
        if (n == 1) {
            tre[0].init();
            for (int i = 0; i < m; i++) {
                tre[0].insert(str[i]);
            }
            ans = tre[0].L;
        }
        else {
           // continue;
            for (int i = 0; i < tot; i++) {
                memset(chec,0,sizeof(chec));
                for (int tt = 1; tt < tot; tt*=n) {
                    chec[i / tt % n] = true;
                }
               // continue;
                bool fail = false;
                for (int j = 0; j < n; j++)
                if (!chec[j]) fail = true;
                if (fail) continue;
                for (int i = 0; i < n; i++) tre[i].init();
                //continue;
                //cout<<'i'<<i<<endl;
                for (int j = 0,tt = 1; tt < tot; j++,tt*=n) {
                   // cout<<i / tt % n<<endl;
                    tre[i / tt % n].insert(str[j]);
                }
                int cnt = 0;
                for (int j = 0; j < n; j++) cnt += tre[j].L;
                if (cnt == ans) ans1++;
                else
                if (cnt > ans) {
                    ans1 = 1;
                    ans = cnt;
                }
            }
        }
        printf("Case #%d: %d %d\n",cas++,ans,ans1);
    }

}
