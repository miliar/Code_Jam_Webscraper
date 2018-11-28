#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

char ch[10][10];
bool flag,f,wo,wx;
int T,a,b;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    for (int t=1;t<=T;t++){
        flag=false;wx=false;wo=false;getchar();
        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                ch[i][j]=getchar();
                if (ch[i][j]=='.') flag=true;
            }
            getchar();
        }
        
        for (int i=0;i<4;i++){
            f=false;a=0;b=0;
            for (int j=0;j<4;j++){
                if (ch[i][j]=='T') f=true;
                if (ch[i][j]=='X') a++;
                if (ch[i][j]=='O') b++;
            }
            if (a==3 && f || a==4) {wx=true;break;}
            if (b==3 && f || b==4) {wo=true;break;}
        }

        for (int i=0;i<4;i++){
            f=false;a=0;b=0;
            for (int j=0;j<4;j++){
                if (ch[j][i]=='T') f=true;
                if (ch[j][i]=='X') a++;
                if (ch[j][i]=='O') b++;
            }
            if (a==3 && f || a==4) {wx=true;break;}
            if (b==3 && f || b==4) {wo=true;break;}
        }        
        
        f=false;a=0;b=0;
        for (int i=0;i<4;i++){
            if (ch[i][i]=='T') f=true;
            if (ch[i][i]=='X') a++;
            if (ch[i][i]=='O') b++;
        }
        if (a==3 && f || a==4) wx=true;
        if (b==3 && f || b==4) wo=true;
        
        f=false;a=0;b=0;
        for (int i=0;i<4;i++){
            if (ch[i][3-i]=='T') f=true;
            if (ch[i][3-i]=='X') a++;
            if (ch[i][3-i]=='O') b++;
        }
        if (a==3 && f || a==4) wx=true;
        if (b==3 && f || b==4) wo=true;
        
        if (wx) printf("Case #%d: X won\n",t); else
           if (wo) printf("Case #%d: O won\n",t); else
              if (!flag) printf("Case #%d: Draw\n",t); else printf("Case #%d: Game has not completed\n",t);
    }
    return 0;
}
