#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
const int maxn = 10010;
struct info{
    char c;
    int f;
}a[maxn], b[500][500];
int main(){
    //freopen("a.in", "r", stdin);
    //freopen("a.txt", "w", stdout);
    int T, n, m;
    scanf("%d", &T);//printf("%d\n", T);
    b['1']['1'].c = '1'; b['1']['1'].f = 1;
    b['1']['i'].c = 'i'; b['1']['i'].f = 1;
    b['1']['j'].c = 'j'; b['1']['j'].f = 1;
    b['1']['k'].c = 'k'; b['1']['k'].f = 1;

    b['i']['1'].c = 'i'; b['i']['1'].f = 1;
    b['i']['i'].c = '1'; b['i']['i'].f = -1;
    b['i']['j'].c = 'k'; b['i']['j'].f = 1;
    b['i']['k'].c = 'j'; b['i']['k'].f = -1;

    b['j']['1'].c = 'j'; b['j']['1'].f = 1;
    b['j']['i'].c = 'k'; b['j']['i'].f = -1;
    b['j']['j'].c = '1'; b['j']['j'].f = -1;
    b['j']['k'].c = 'i'; b['j']['k'].f = 1;

    b['k']['1'].c = 'k'; b['k']['1'].f = 1;
    b['k']['i'].c = 'j'; b['k']['i'].f = 1;
    b['k']['j'].c = 'i'; b['k']['j'].f = -1;
    b['k']['k'].c = '1'; b['k']['k'].f = -1;
    for(int icase = 1; icase <= T; icase++){
        scanf("%d%d", &n, &m);
        string str, s;
        cin>>str;
        for(int i = 0; i < m; i++) s+=str;
        n *= m;
        a[0].c = s[0]; a[0].f = 1;
        for(int i = 1; i < n; i++){
            a[i].c = b[a[i-1].c][s[i]].c;
            a[i].f = b[a[i-1].c][s[i]].f*a[i-1].f;//printf("%d %c\n", a[i].f, a[i].c);
        }
        printf("Case #%d: ", icase);
        if(a[n-1].f != -1 || a[n-1].c != '1'){
            printf("NO\n"); continue;
        }
        info q[10];
        q[0].f = 1; q[0].c = 'i';
        q[1].f = 1; q[1].c = 'k';
        int cnt = 0;
        for(int i = 0; i < n && cnt < 2; i++){
            if(a[i].f == q[cnt].f && a[i].c == q[cnt].c) cnt++;
        }
        if(cnt == 2) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
