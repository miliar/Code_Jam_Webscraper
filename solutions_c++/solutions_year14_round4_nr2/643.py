#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;

const int N = 1005;
int a[N],b[N],c[N],d[N],e[N],f[N],P[N],Q[N];
int n, ans;
void Swap(int s, int t){
    if (s < t){
    ans += t-s;
    for (int i = t; i > s; i--)
        swap(a[i],a[i-1]);
    } else {
        ans += s-t;
        for (int i = t; i < s; i++)
        swap(a[i],a[i+1]);
    }
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("BL.out","w",stdout);
    int T; cin >> T;

    for (int o = 1; o <= T; o++){
        cin >> n;
        for (int i = 1; i <= n; i++)
            scanf("%d", a + i);

        int s = 1, t = n;
        ans = 0;
        while (s <= t){
            int mi = 2000000000, pos = -1;
            for (int i = s; i <= t; i++)
            if (a[i] < mi){
                mi = a[i]; pos = i;
            }
            if (pos - s < t - pos){
                Swap(s, pos);s++;
            }
            else{
                Swap(t, pos); t--;
            }
        }
        printf("Case #%d: %d\n", o, ans);
    }
}


/*
 memset(P, 0, sizeof P);
        memset(Q, 0, sizeof Q);
        for (int i = 1; i <= n; i++){
            P[i] = P[i-1];
            for (int j = 1; j <= i - 1; j++)
                if (a[j] > a[i]) P[i]++;
        }
        for (int i = n; i >= 1; i--){
            Q[i] = Q[i+1];
            for (int j = i + 1; j <= n; j++)
                if (a[j] > a[i]) Q[i]++;
        }
        int ans = n * n;
        for (int i = 1; i <= n; i++){
            int now = 0;
          //  if (i == pos){
                //now += P[i - 1] + Q[i + 1];
            //} else
           // if (i < pos){
                now = P[i] + Q[i+1];
          //  } else
            //    now += Q[i + 1] + P[i] + (i - pos) + pos - 1;

            if (now < ans)ans = now;
        }
        printf("Case #%d: %d\n", o, ans);
    }*/
