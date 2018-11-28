#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
vector<int>E[110];
int par[110], m, n, C[110], D[110], ran[110][2];
char p[110], res[110], q[6][110];
bool v[110];
void DFS(int a){
    int i;
    D[a]=1;
    for(i=0;i<E[a].size();i++){
        DFS(E[a][i]);
        D[a] += D[E[a][i]];
    }
}
int main(){
    srand(1879);
    freopen("input.txt","r",stdin);
    FILE *out = fopen("output.txt","w");
    int TC, TT, i, a, TTT, j, k;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("%d\n",TT);
        fprintf(out,"Case #%d: ",TT);
        scanf("%d",&n);
        for(i=1;i<=n;i++)E[i].clear();
        for(i=1;i<=n;i++){
            scanf("%d",&par[i]);
            if(par[i])E[par[i]].push_back(i);
        }
        for(i=1;i<=n;i++){
            if(!par[i]){
                DFS(i);
            }
        }
        scanf("%s",p+1);
        scanf("%d",&m);
        for(i=1;i<=m;i++){
            scanf("%s",q[i]);
        }
        TTT = 7000;
        for(i=1;i<=m;i++)C[i]=0;
        while(TTT--){
            for(i=1;i<=n;i++)v[i]=false;
            int cc = 0;
            while(1){
                int pv = 0;
                for(i=1;i<=n;i++){
                    if(!v[i] && (par[i] == 0 || v[par[i]])){
                        ran[i][0] = pv;
                        ran[i][1] = pv+D[i];
                        pv += D[i];
                    }
                }
                int tt = rand()%pv;
                for(i=1;i<=n;i++){
                    if(!v[i] && (par[i] == 0 || v[par[i]])){
                        if(ran[i][0] <= tt && tt < ran[i][1])break;
                    }
                }
                v[i]=true;
                res[cc++] = p[i];
                if(cc==n)break;
            }
            res[cc] = 0;
            for(i=1;i<=m;i++){
                for(j=0;j<n;j++){
                    for(k=0;q[i][k];k++){
                        if(q[i][k]!=res[j+k])break;
                    }
                    if(!q[i][k])break;
                }
                if(j != n){
                    C[i]++;
                }
            }
        }
        for(i=1;i<=m;i++){
            fprintf(out,"%.5lf ",(double)C[i]/7000);
        }
        fprintf(out,"\n");
    }
}
