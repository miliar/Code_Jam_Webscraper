/*************************************************************************
	> File Name: gb.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com 
	> Created Time: 2014年05月31日 星期六 23时35分06秒
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;
#define MAXN 1005
template <typename T> inline T Min(T a, T b) {return a<b?a:b;}
int t, Cas = 1, n, a[MAXN], ra[MAXN], rank[MAXN];
map <int, int> ma;
void Swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}
int cmp(int x, int y)
{
    return a[x] < a[y];
}
void work()
{
    printf("Case #%d: ", Cas ++);
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++) {
        scanf("%d", &a[i]);
        ra[i] = i;
    }
    sort(ra+1, ra+1+n, cmp);
    ma.clear();
    for (int i = 1; i <= n; i ++) {
        ma[a[ra[i]]] = i;
    }
    int top = 1, rail = n, ans = 0;
    for (int i = 1; i <= n; i ++) {
        int pos;
        for (int j = 1; j <= n; j ++) {
            if (ma[a[j]] == i) {
                pos = j;
                break;
            }
        }
        if (pos - top < rail - pos) {
            for (int j = pos; j > top; j --) {
                Swap(a[j], a[j-1]);
                ans ++;
            }
            top ++;
        } else {
            for (int j = pos; j < rail; j ++) {
                Swap(a[j], a[j+1]);
                ans ++;
            }
            rail --;
        }
    }
    cout << ans << endl;
}
int main()
{
    scanf("%d", &t);
    while (t --) {
        work();
    }
	return 0;
}
