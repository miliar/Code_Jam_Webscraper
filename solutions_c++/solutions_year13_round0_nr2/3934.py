#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
using namespace std;

int yard[102][102];


bool can_reach(int x,int y){
    bool ok=true;
    int cx1=x,cy1=y,cx2=x,cy2=y;
    bool go1=true,go2=true;
    int h = yard[x][y];
    while (ok){
        if (go1) {
            cx1--;
            if (yard[cx1][cy1]==-1) go1=false;
            else if (yard[cx1][cy1] > h) ok=false;
        }
        if (go2) {
            cx2++;
            if (yard[cx2][cy1]==-1) go2=false;
            else if (yard[cx2][cy1] > h) ok=false;
        }
        if (!go1 && !go2) break;

    }
    if (ok) return true;
    cx1=x;cy1=y;cx2=x;cy2=y;go1=true;go2=true;ok=true;
    while (ok){
        if (go1) {
            cy1--;
            if (yard[cx1][cy1]==-1) go1=false;
            else if (yard[cx1][cy1] > h) ok=false;
        }
        if (go2) {
            cy2++;
            if (yard[cx1][cy2]==-1) go2=false;
            else if (yard[cx1][cy2] > h) ok=false;
        }
        if (!go1 && !go2) break;

    }
    return ok;
}




int main(){
    int n,x,y,cases;
    bool ok;
    string msg;
    scanf("%i\n",&cases);
    for (int n=0;n<cases;n++){
        ok = true;
        for (int i=0;i<102;i++) for (int j=0;j<102;j++) yard[i][j]=-1;
        scanf("%i %i\n",&x,&y);
        for (int i=1;i<=x;i++) for (int j=1;j<=y;j++) scanf("%i",&yard[i][j]);

        for (int i=1;i<=x;i++){
            for (int j=1;j<=y;j++){
                if (!can_reach(i,j)) {ok=false;break;}
            }
            if (!ok) break;
        }

        if (ok) msg="YES";
        else msg="NO";

        printf("Case #%i: %s\n",(n+1),msg.c_str());
        //for (int i=0;i<10;i++){ for (int j=0;j<10;j++) cout << yard[i][j]; cout << endl;}


    }


    return 0;
}
