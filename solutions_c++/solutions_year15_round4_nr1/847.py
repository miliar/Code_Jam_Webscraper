#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int uy[4] = {-1,0,1,0};
int ux[4] = {0,1,0,-1};
int kasus,R,C;
char peta[105][105];

bool sah(int y,int x) {
    return (y>=0&&y<R&&x<C&&x>=0);
}

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        scanf("%d %d",&R,&C);
        for (int i=0;i<R;++i) scanf("%s",&peta[i]);
        
        int jawab = 0;
        bool flag = true;
        for (int i=0;i<R && flag;++i) {
            for (int j=0;j<C && flag;++j) {
                int pakai;
                if (peta[i][j] == '^') pakai = 0;
                else if (peta[i][j] == '>') pakai = 1;
                else if (peta[i][j] == 'v') pakai = 2;
                else if (peta[i][j] == '<') pakai = 3;
                else continue;
                
                int y = i+uy[pakai];
                int x = j+ux[pakai];
                bool ada = false;
                
                while (!ada && sah(y,x)) {
                    if (peta[y][x] != '.') ada = true;
                    y += uy[pakai];
                    x += ux[pakai];
                }
                
                if (!ada) {
                    ++jawab;
                    bool dapat = false;
                    
                    for (int k=0;k<4 && !dapat;++k) {
                        pakai = k;
                        y = i+uy[pakai];
                        x = j+ux[pakai];
                        ada = false;
                        
                        while (!ada && sah(y,x)) {
                            if (peta[y][x] != '.') ada = true;
                            y += uy[pakai];
                            x += ux[pakai];
                        }
                        
                        if (ada) dapat = true;
                    }
                    
                    if (!dapat) flag = false;
                }
            }
        }
        
        if (!flag) printf("Case #%d: IMPOSSIBLE\n",l);
        else printf("Case #%d: %d\n",l,jawab);
    }
    return 0;
}
