#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<iostream>
#include<vector>
#include<set>
#include<deque>
#include<algorithm>
using namespace std;
#define DEBUG_FILE_OUT freopen("out.txt","w",stdout)
#define DEBUG_FILE_IN freopen("A-large.in","r",stdin)
char s[4][4];
bool check(int x,char ch){
    bool flagr=true,flagc=true;
    for(int i=0;i<4;i++){
        if(s[x][i]!=ch && s[x][i]!='T') flagr=false;
        if(s[i][x]!=ch && s[i][x]!='T') flagc=false;
    }
    return flagr || flagc;
}
bool checkd(int ch){
    bool flag1=true,flag2=true;
    for(int i=0;i<4;i++){
        if(s[i][3-i]!=ch && s[i][3-i]!='T') flag1=false;
        if(s[i][i]!=ch && s[i][i]!='T') flag2=false;
    }
    return flag1 || flag2;
}
int main(){
    int T,cas=1;
    DEBUG_FILE_IN;
    DEBUG_FILE_OUT;
    cin>>T;
    while(T--){
        gets(s[0]);
        for(int i=0;i<4;i++) gets(s[i]);
        bool flags=false,flagw=false;
        printf("Case #%d: ",cas++);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++) if(s[i][j]=='.') flags=true;
            if(check(i,'X')){puts("X won");flagw=true;break;}
            if(check(i,'O')){puts("O won");flagw=true;break;}
        }
        if(!flagw && checkd('X')){puts("X won");flagw=true;}
        if(!flagw && checkd('O')){puts("O won");flagw=true;}

        if(!flagw) puts(flags?"Game has not completed":"Draw");
    }
}
