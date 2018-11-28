#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>


using namespace std;

int t;
char a[200];
int ans;

void split (int p[], int time) {
    if(ans<=time) return;
    int m=0;
    for(int i=9;i>=0;i--) {
        if(p[i]>0) {m=i; break;}
    }
    if(ans>time+m) ans=time+m;
    if(m>1) {
        for(int i=1;i<m;i++) {
            int pt[10];
            for(int j=0;j<10;j++) {
                pt[j]=p[j];
            }
            pt[m]--;
            pt[i]++;
            pt[m-i]++;
            split(pt,time+1);
        }
    }
}

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);

    scanf("%d", &t);
    for(int c=0;c<t;c++) {
        int d;
        scanf("%d", &d);
        int p[10];
        for(int i=0;i<10;i++) p[i]=0;
        int pi;
        for(int i=0;i<d;i++) {
            scanf("%d", &pi);
            p[pi]++;
        }
        ans=10;
        split(p, 0);

        printf("Case #%d: %d\n", c+1, ans);
    }
}
