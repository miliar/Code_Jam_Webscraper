#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

int T, l, x, cas = 0;
char buf[11000];
int a[11000];
int s[11000];
int mtr[5][5];
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("c.out", "w", stdout);
    scanf("%d", &T);
    mtr[1][1] = 1;
    mtr[1][2] = 2;
    mtr[1][3] = 3;
    mtr[1][4] = 4;
    mtr[2][1] = 2;
    mtr[2][2] = -1;
    mtr[2][3] = 4;
    mtr[2][4] = -3;
    mtr[3][1] = 3;
    mtr[3][2] = -4;
    mtr[3][3] = -1;
    mtr[3][4] = 2;
    mtr[4][1] = 4;
    mtr[4][2] = 3;
    mtr[4][3] = -2;
    mtr[4][4] = -1;
    while(T--){
        scanf("%d%d", &l, &x);
        scanf("%s", buf);
        for (int i = 0; i < l; i++) a[i] = buf[i] - 'i' + 2;
        for (int i = l; i < x * l; i++) a[i] = a[i%l];
        s[0] = a[0];
        bool geti = s[0] == 2, getj = false; int sign;
        for (int i = 1; i < x * l; i++){
                sign = 1;
                if(s[i-1] > 0 && a[i] < 0) sign = -1;
                if(s[i-1] < 0 && a[i] > 0) sign = -1;
                s[i] = sign * mtr[(int)abs(s[i-1])][(int)abs(a[i])];
                if (s[i] == 2) geti = true;
                if (geti && s[i] == 4) getj = true;
        }
        bool flag = false;
        if (geti && getj && s[x*l-1] == -1) flag = true;
        if (flag)
            printf("Case #%d: YES\n", ++cas);
        else
            printf("Case #%d: NO\n", ++cas);
    }
    return 0;
}
