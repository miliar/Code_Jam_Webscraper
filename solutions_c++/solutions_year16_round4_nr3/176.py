#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

int h, w;

int dx[] = {-1,0,1,0};
int dy[] = {0,-1,0,1};
int l[105*105];

bool ing(int y, int x) {
    return 0 <= y && y < h && 0 <= x && x < w;
}

int glbl(int y, int x, int d) {
    if (y == -1) return x;
    else if (x == w) return w+y;
    else if (y == h) return w+h+(w-1-x);
    else if (x == -1) return 2*w+h+(h-1-y);
    else {
        return 2*w+2*h + (y*w + x)*4 + d;
    }
}

int gl(int i) {
    return l[i] == i ? i : l[i]=gl(l[i]);
}

void adde(int y, int x, int d, int ny, int nx, int nd) {
    //printf("(%d,%d,%d) to (%d,%d,%d)\n", y, x, d, ny, nx, nd);
    int la = glbl(y,x,d);
    int lb = glbl(ny,nx,nd);
    l[gl(la)] = gl(lb);
}

void bg(int m) {
    FO(i,0,2*w+2*h+4*w*h) l[i] = i;
    FO(y,0,h) FO(x,0,w) {
        if (m&((1<<(y*w+x)))) {
            adde(y,x,0,y,x,1);
            adde(y,x,2,y,x,3);
        } else {
            adde(y,x,0,y,x,3);
            adde(y,x,2,y,x,1);
        }
        FO(i,0,4) {
            int ny = y+dy[i], nx = x+dx[i];
            adde(y,x,i,ny,nx,(i+2)%4);
        }
    }
}

int t[500];

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        printf("Case #%d:\n", Z);
        scanf("%d %d", &h, &w);
        FO(i,0,2*w+2*h) scanf("%d", t+i);
        FO(m,0,1<<(h*w)) {
            bg(m);
            set<int> s;
            bool bad = false;
            FO(i,0,w+h) {
                int a = t[2*i], b = t[2*i+1];
                a--; b--;
                if (gl(a) != gl(b)) {
                    //printf("not %d, %d\n", a, b);
                    bad = true;
                }
                s.insert(gl(a));
            }
            bad |= sz(s) != w+h;
            if (!bad) {
                FO(y,0,h) {
                    FO(x,0,w) {
                        if (m&(1<<(y*w+x))) {
                            printf("/");
                        } else {
                            printf("\\");
                        }
                    }
                    printf("\n");
                }
                goto done;
            }
        }

        printf("IMPOSSIBLE\n");
done:;
    }
}

