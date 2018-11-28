#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
#include<cstring>
using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359

int n,m;
bool mark[333][333];
char a[333][333];

char strelica[4] = {'^','>','v','<'};
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

bool unutra(int x, int y) {
    return (x>=0 && x<n && y>=0 && y<m);
}

int main() {

    FILE *ff=fopen("A-large.in", "r"), *gg=fopen("A-large.out", "w");

    int i,j,s,q,tt,ts,ps,px,py,ws,ttt,res,wres;
    bool ponovio,imastrelica;

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {
        fprintf(gg,"Case #%d: ", tt);

        fscanf(ff,"%d%d", &n, &m);

        for(i=0; i<n; i++) {
            fscanf(ff,"%s", &a[i]);
        }

        printf("primer %d\n", tt);

        res = 0;

        bool impos = false;
        for(i=0; i<n; i++) {
            for(j=0; j<m; j++) {
                if (a[i][j] != '.') {
                    bool bb = false;
                    for(s=0; s<4; s++) {
                        px = i + dx[s];
                        py = j + dy[s];
                        bool ima = false;
                        while(unutra(px,py)) {
                            if (a[px][py] != '.') {
                                ima = true;
                                break;
                            }
                            px += dx[s];
                            py += dy[s];
                        }
                        if (ima) {
                            bb = true;
                            break;
                        }
                    }
                    if (!bb) {
                        impos = true;
                    }
                }
            }
        }

        if (impos) {
            fprintf(gg,"IMPOSSIBLE\n");
            continue;
        }

        memset(mark,0,sizeof(mark));

        for(i=0; i<n; i++) {
            for(j=0; j<m; j++) if (!mark[i][j]) {
                if (a[i][j] != '.') {

                    ps = 0;
                    for(s=0; s<4; s++) if (strelica[s] == a[i][j]) ps = s;

                    px = i; py = j;

                    mark[px][py] = true;

                    px += dx[ps];
                    py += dy[ps];

                    //printf("-> %d %d\n", px, py);

                    bool bbb = false;
                    while(unutra(px,py)) {
                        //printf("~ %d %d\n", px, py);
                        if (a[px][py] != '.') {
                            if (mark[px][py]) {
                                bbb = true;
                                break;
                            }
                            mark[px][py] = true;
                            for(s=0; s<4; s++) if (strelica[s] == a[px][py]) ps = s;
                        }
                        px += dx[ps];
                        py += dy[ps];
                    }

                    if (!bbb) res++;
                }
            }
        }

        //printf("kraj");

        /*printf("%d %d\n", n, m);
        for(i=0; i<n; i++) {
            printf("%s\n", a[i]);
        }
        printf("res = %d\n", res);
        system("pause");*/

        if (res == 999) fprintf(gg, "IMPOSSIBLE\n");
        else fprintf(gg, "%d\n", res);
    }

    fclose(ff); fclose(gg);

    return 0;
}
