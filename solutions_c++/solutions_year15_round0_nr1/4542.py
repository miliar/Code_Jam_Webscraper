#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>


using namespace std;

int t;
int m;
char a[200];

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    scanf("%d", &t);
    for(int c=0;c<t;c++) {
        scanf("%d", &m);
        scanf("%s", &a);
        int total=0;
        int ans=0;
        for(int i=0;i<=m;i++) {
            int si=a[i]-'0';
            if(total<i) {
                int f=i-total;
                total+=f;
                ans+=f;
            }
            total+=si;
        }
        printf("Case #%d: %d\n", c+1, ans);
    }
}
