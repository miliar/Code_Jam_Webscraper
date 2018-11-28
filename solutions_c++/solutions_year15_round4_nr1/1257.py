#include <bits/stdc++.h>

using namespace std;

char Z[105];
char A[105][105];
bool fuera;
int casos, cto1, cto2, x, y, res;

inline void ponlo(char que){
    if(que=='^'){
        x=0;
        y=1;
    }
    else if(que=='>'){
        x=1;
        y=0;
    }
    else if(que=='<'){
        x=-1;
        y=0;
    }
    else if(que=='v'){
        x=0;
        y=-1;
    }
}

inline void sim(int a, int b){
    do {
        a+=x;
        b+=y;
    }while(a<=cto1 and b<=cto2 and a>0 and b>0 and A[a][b]=='.');
    fuera=true;
    if(a<=cto1 and b<=cto2 and a>0 and b>0){
        fuera=false;
    }
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d",&casos);
    for(int v=1; v<=casos; v++){
        scanf("%d%d",&cto2,&cto1);
        for(int i=cto2; i>0; i--){
            scanf("%s",Z+1);
            for(int e=1; e<=cto1; e++){
                A[e][i]=Z[e];
            }
        }
        res=0;
        for(int i=cto2; i>0; i--){
            for(int e=1; e<=cto1; e++){
                if(A[e][i]!='.'){
                    ponlo(A[e][i]);
                    sim(e, i);
                    if(fuera){
                        ++res;
                        x=0;
                        y=1;
                        sim(e, i);
                        if(fuera){
                            x=0;
                            y=-1;
                            sim(e, i);
                            if(fuera){
                                x=1;
                                y=0;
                                sim(e, i);
                                if(fuera){
                                    x=-1;
                                    y=0;
                                    sim(e, i);
                                    if(fuera){
                                        res=-1000000000;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        printf("Case #%d: ",v);
        if(res<0){
            printf("IMPOSSIBLE\n");
        }
        else {
            printf("%d\n",res);
        }
    }
    return 0;
}
