#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#define pii pair<int,int>
#define LL long long
using namespace std;
int t,n,b,c,d,e,f;
char a[15][15];

int main(){
    scanf("%d",&t);
    for (int l=1;l<=t;l++){
        for (int i=1;i<=4;i++)
            scanf("%s",a[i]+1);
        f=0;
        for (char x='O';x<='X';x+='X'-'O'){
            c=0;
            for (int i=1;i<=4;i++){
                b=0;d=0;
                for (int j=1;j<=4;j++){
                    b+=(a[i][j]==x)||(a[i][j]=='T');
                    d+=(a[j][i]==x)||(a[j][i]=='T');
                    }
                if (b==4 || d==4) c=1;
                }
            b=d=0;
            for (int i=1;i<=4;i++){
                b+=(a[i][i]==x)||(a[i][i]=='T');
                d+=(a[i][5-i]==x)||(a[i][5-i]=='T');
                }
            if (b==4 || d==4 || c){
               printf("Case #%d: %c won\n",l,x);
               f=1;
               break;
               }
            }
        if (!f){
           e=0;
           for (int i=1;i<=4;i++)
               for (int j=1;j<=4;j++)
                   if (a[i][j]=='.') e=1;
           if (e) printf("Case #%d: Game has not completed\n",l);
           else printf("Case #%d: Draw\n",l);   
           }
    }
    return 0;
}
