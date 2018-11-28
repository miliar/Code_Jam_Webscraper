#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<set>

using namespace std;

string kata[10];
int banyak,server,coba[10],best,total,kasus;

void recurse(int urut) {
    if (urut == banyak) {
        set<string> trie[server];
        int temp = server;
        for (int i=0;i<banyak;++i) {
            for (int j=1;j<=kata[i].length();++j) {
                if (trie[coba[i]].find(kata[i].substr(0,j)) == trie[coba[i]].end()) {
                    trie[coba[i]].insert(kata[i].substr(0,j));
                    ++temp;
                }
            }
        }
        
        for (int i=0;i<server;++i) if (trie[i].size() == 0) return ;
        
        if (temp > best) {
            best = temp;
            total = 1;
        } else if (temp == best) ++total;
    } else {
        for (int i=0;i<server;++i) {
            coba[urut] = i;
            recurse(urut+1);
        }
    }
}

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        scanf("%d %d",&banyak,&server);
        for (int i=0;i<banyak;++i) cin>>kata[i];
        
        best = 0;
        total = 0;
        
        recurse(0);
        printf("Case #%d: %d %d\n",l,best,total);
    }
    return 0;
}
