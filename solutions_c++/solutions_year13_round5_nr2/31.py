#include <stdio.h>
#include <math.h>
int b[20], u[20], n;
int ans, ansb[20];
int sgn(int a){
    if (a < 0) return -1;
    if (a > 0) return 1;
    return 0;
}
int dmin(int a, int b){
	return a < b ? a : b;
}
int dmax(int a, int b){
	return a > b ? a : b;
}
struct Point{
    int x, y;
}c[20];
struct Segment{
	Point s, e;
}a[20];
int cross(Point a, Point b, Point c){
    return (b.x - a.x) * (c.y - b.y) - (c.x - b.x) * (b.y - a.y);
}
bool Seg_Intersect(Segment a, Segment b){
	return (dmax(a.s.x, a.e.x) >= dmin(b.s.x, b.e.x))
		&& (dmax(b.s.x, b.e.x) >= dmin(a.s.x, a.e.x))
		&& (dmax(a.s.y, a.e.y) >= dmin(b.s.y, b.e.y))
		&& (dmax(b.s.y, b.e.y) >= dmin(a.s.y, a.e.y))
		&& cross(a.s, a.e, b.s) * cross(a.s, a.e, b.e) <= 0
		&& cross(b.s, b.e, a.s) * cross(b.s, b.e, a.e) <= 0;
}
int myabs(int x){
    return x < 0? -x: x;
}
bool onseg(Point p, Segment ls){
	return myabs(cross(p, ls.s, ls.e)) <= 0 && (p.x - ls.s.x) * (p.x - ls.e.x) <= 0 && (p.y - ls.s.y) * (p.y - ls.e.y) <= 0;
}

bool Seg_Intersect_2(Segment a, Segment b){
	return Seg_Intersect(a, b);
}

int pd(){
    b[n] = b[0];
    int i, j;
    for (i = 0; i < n; i++){
        a[i].s = c[b[i]];
        a[i].e = c[b[i + 1]];
    }
    for (i = 0; i < n; i++){
        for (j = i + 2; j < n; j++){
            if (i == 0 && j == n - 1) continue;
            if (Seg_Intersect_2(a[i], a[j])){
                return -1;
            }
        }
    }
    int ans = 0;
    for (i = 0; i < n; i++){
        ans += c[b[i]].x * c[b[i + 1]].y - c[b[i + 1]].x * c[b[i]].y;
    }
    return myabs(ans);
}
void dfs(int x){
    int i;
    if (x == n){
        int t = pd();
        if (t > ans){
            ans = t;
            for (int i = 0; i < n; i++){
                ansb[i] = b[i];
            }
        }
        return;
    }
    for (i = 0; i < n; i++){
        if (u[i] == 0){
            u[i] = 1;
            b[x] = i;
            dfs(x + 1);
            u[i] = 0;
        }
    }
}
int main(){
    int T, ri = 1, i;
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (i = 0; i < n; i++){
            scanf("%d%d", &c[i].x, &c[i].y);
        }
        ans = 0;
        dfs(0);
        printf("Case #%d:", ri++);
        for (i = 0; i < n; i++){
            printf(" %d", ansb[i]);
        }
        printf("\n");
    }
    return 0;
}
