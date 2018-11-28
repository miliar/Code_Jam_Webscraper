#include<cstdio>
#include<iostream>
#include<string>
#include<set>
#include<algorithm>
#include<cstring>
using namespace std;
int t, n, ans, special;
multiset<int, greater<int> > S;
multiset<int, greater<int> >::iterator it;

void dfs(void) {
     //multiset<int>::iterator l;
     //cout << ans  << " Ssize: " << S.size() << endl;
      //getchar();
     //for( l = S.begin(); l != S.end(); l++) cout << *l << " ";
     //cout << endl;
     if(S.empty()) return;
     it = S.begin();
     int x = 1, y = *it;
     if(y + special < ans) ans = y + special;
     if(*it <= 3) return;
     while(true) {
         it++;
         if(it == S.end()) break;
         if(y != *it) break;
         x++;
     }
     S.erase(y);
     for(int i = 1; i <= y / 2 + 1; i++) {
         int j = y - i, jj = i;
         special += x;
         for(int k = 0; k < x; k++) {
             S.insert(j);
             S.insert(jj);
         }
         dfs();
        for(int k = 0; k < x; k++) {
             S.erase(S.find(j));
             S.erase(S.find(jj));
         }
         special -= x;
     }
     for(int i = 1;i <= x;i++)
     S.insert(y);
     return;
}

int main(void){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    scanf("%d",&t);
    for(int kk = 1; kk <= t; kk++) {
        scanf("%d", &n);
        S.clear();
        for(int i = 0; i < n; i++) {
            int x;
            scanf("%d",&x);
            S.insert(x);
        }
        special = 0;
        ans = 0x3fffffff;
        dfs();
        printf("Case #%d: %d\n", kk, ans);
    }
    return 0;
}
