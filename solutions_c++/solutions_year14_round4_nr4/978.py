#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int _,N,M;
int i,j,k,l,m,n,a[100000];
string c[111];
int cnt,____M,____a;
int d[111];

struct node {
    node* c[26];
    node() {
        memset(c,0,sizeof(c));
        cnt++;
    }
};

node *root[100];


void ____i(string &s,int p) {
    node *now = root[p];
    if (!now) {
        now = root[p] = new node();
    }
    for (string::iterator k=s.begin(); k!=s.end(); k++) {
        int pp = *k-'A';
        if(!now->c[pp]) now -> c[pp] = new node();
        now = now -> c[pp];
    }
}

void ____d(int i) {
    if (i>M) {
        for (int i=1; i<=N; i++) {
            root[i]=NULL;
        }
        cnt=0;
        for (int i=1; i<=M; i++) ____i(c[i],d[i]);
        if (cnt > ____M) {
            ____M = cnt;
            ____a = 1;
        } else if (cnt==____M) ____a++;
        return;
    }
    for(int ii=1; ii<=N; ii++) {
        d[i]=ii;
        ____d(i+1);
    }
}

int main() {
    //freopen("in.txt","r",stdin);
    freopen("D-small-attempt1.in","r",stdin);
    //freopen("D-small-attempt1.out","w",stdout);
    scanf("%d",&_);
    int ____c = 0;
    while(_--) {
        ____M = -1;
        scanf("%d%d",&M,&N);
        for (int i=1; i<=M; i++) cin >> c[i];
        ____d(1);
        printf("Case #%d: %d %d\n",++____c,____M,____a);
    }
}
