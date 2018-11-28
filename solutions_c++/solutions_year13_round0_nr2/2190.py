#include<cstdio>
#include<algorithm>
#define N 105
using namespace std;

int T, n, m, tb[N][N], maxv;
int r[N],c[N];
bool ans;

void Input(){
     maxv = tb[0][0];
     for (int i = 0; i < n; i++)
         for (int j = 0; j < m; j++){
             scanf("%d",&tb[i][j]);
             maxv = max(tb[i][j],maxv);
         }
}

void Mark(){     
     for (int i = 0; i < n; i++){
         r[i] = tb[i][0];
         for (int j = 1; j < m; j++)
             if (tb[i][j] != tb[i][j-1]) r[i] = 0;
     }
     
     for (int i = 0; i < m; i++){
         c[i] = tb[0][i];
         for (int j = 1; j < n; j++)
             if (tb[j][i] != tb[j-1][i]) c[i] = 0;
     }
}

bool Check(){
     bool b = 1;
     for (int rd = 1; rd <= maxv; rd++){
       if (b){
         Mark();
         for (int i = 0; i < n; i++)
           if (b)
             for (int j = 0; j < m; j++)
                 if ((b)&&(tb[i][j] == rd)){
                    if ((r[i] != tb[i][j])&&(c[j] != tb[i][j]))
                       b = 0;
                    else tb[i][j] = min(rd+1,maxv);
                 }
       }
     }
     return b;
}
int main(){
    
//    freopen("GCJ13_QR_Blarge.in","r",stdin);
//    freopen("GCJ13_QR_Blarge.out","w",stdout);
    
    scanf("%d",&T);
    for (int i = 0; i < T; i++){
        scanf("%d%d",&n,&m);
        Input();
        ans = Check();
        if (ans)printf("Case #%d: YES\n", i+1);
        else printf("Case #%d: NO\n", i+1);
    }
    scanf("\n");
    return 0;
}
