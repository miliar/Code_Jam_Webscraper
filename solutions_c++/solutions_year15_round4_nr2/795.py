#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>

using namespace std;

double mat[2][105],Vt,Et,Vd[105],Ed[105];
int kasus,N;

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        scanf("%d %lf %lf",&N,&Vt,&Et);
        bool ada = false;
        double waktu;
        
        for (int i=0;i<N;++i) {
            scanf("%lf %lf",&Vd[i],&Ed[i]);
            if (Ed[i] == Et) {
                ada = true;
                waktu = Vt / Vd[i];
            }
        }
        
        
        if (N == 1) {
            if (ada) printf("Case #%d: %.6lf\n",l,waktu);
            else printf("Case #%d: IMPOSSIBLE\n",l);
        } else if (N == 2) {
            if (Ed[0] == Ed[1]) {
                if (Ed[0] == Et) printf("Case #%d: %.6lf\n",l,Vt/(Vd[0]+Vd[1]));
                else printf("Case #%d: IMPOSSIBLE\n",l);
            } else if (ada) {
                printf("Case #%d: %.6lf\n",l,waktu);
            } else {
                Et *= Vt;
                for (int i=0;i<N;++i) {
                    Ed[i] *= Vd[i];
                    mat[0][i] = Ed[i];
                    mat[1][i] = Vd[i];
                }
                
                double kali = mat[1][0]/mat[0][0];
                ada = false;
                for (int i=0;i<N;++i) {
                    mat[1][i] -= kali*mat[0][i];
                    if (mat[1][i] != 0.0) ada = true;
                }
                
                if (Vt != Et*kali) Vt -= Et*kali;
                else Vt = 0.0;
                
                if (!ada) {
                    if (Vt != 0.0) printf("Case #%d: IMPOSSIBLE\n",l);
                    else printf("Case #%d: %.6lf\n",l,Et / (Ed[0]+Ed[1]));
                } else {
                    double t[2];
                    t[1] = Vt / mat[1][1];
                    t[0] = (Et-Ed[1]*t[1])/Ed[0];
                    
                    //printf("M: %.6lf %.13lf\n",mat[1][1],Vt);
                    //printf("T: %.6lf %.6lf\n",t[0],t[1]);
                    if (t[1]>=0 && t[0]>=0) printf("Case #%d: %.6lf\n",l,max(t[0],t[1]));
                    else printf("Case #%d: IMPOSSIBLE\n",l);
                }
            }
        }
    }
    return 0;
}
