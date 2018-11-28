#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;

int T, C=1;
int n, S, x[1024], y[1024], z[1024], vx[1024], vy[1024], vz[1024];
double dist[1024];
bool visited[1024];
int pai[1024];
double wpai[1024];

double gdist(double x1, double y1, double z1, double x2, double y2, double z2) {
    return sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1) );
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d %d",&n,&S);
        for (int i=0;i<n;i++) {
            scanf("%d %d %d",x+i,y+i,z+i);
            scanf("%d %d %d",vx+i,vy+i,vz+i);
        }

        for (int i=0;i<n;i++)
            dist[i] = 1e30;
        memset(visited,false,sizeof(visited));
        dist[0] = 0;
        int u = 0;
        while (u != -1) {
            visited[u] = true;
            for (int i=0;i<n;i++) if (!visited[i]) {
                double w = gdist(x[u],y[u],z[u],x[i],y[i],z[i]);
                if (w < dist[i]) {
                    dist[i] = w;
                    pai[i] = u;
                    wpai[i] = w;
                }
            }
            u = -1;
            double menor = 1e25;
            for (int i=0;i<n;i++) if (!visited[i] and dist[i] <menor) {
                u = i;
                menor = dist[i];
            }
        }
        double maior = 0;
        u = 1;
        while (u != 0) {
            maior = max(maior, wpai[u]);
            u = pai[u];
        }

        printf("%.12lf\n",maior);
    }

    return 0;
}
