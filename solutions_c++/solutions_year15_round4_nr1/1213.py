#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <limits>
#include <set>
#include <cmath>
#include <iomanip>
#include <stdio.h>
#include <cstring>
using namespace std;
#define pb push_back
#define MAXN 110

char mappa[MAXN][MAXN];
bool prev_[MAXN][MAXN];
bool usato[MAXN][MAXN];
bool ok[MAXN][MAXN];
int T,R,C,sol;

void prova(int i ,int j)
{
    usato[i][j]=true;
    int i2=i,j2=j;
    if(mappa[i][j]=='>') {j2++ ; while(j2<C && mappa[i2][j2]=='.') j2++;}
    if(mappa[i][j]=='^') {i2-- ; while(i2>=0 && mappa[i2][j2]=='.') i2--;}
    if(mappa[i][j]=='<') {j2-- ; while(j2>=0 && mappa[i2][j2]=='.') j2--;}
    if(mappa[i][j]=='v') {i2++ ; while(i2<R && mappa[i2][j2]=='.') i2++;}

    if(i2>=R || i2<0 || j2<0 || j2>=C) return;
    prev_[i2][j2]=true;
    if(!usato[i2][j2])  prova(i2,j2);
}

bool calcola(int i ,int j)
{
    usato[i][j]=true;
    int i2=i,j2=j;
    if(mappa[i][j]=='>') {j2++ ; while(j2<C && mappa[i2][j2]=='.') j2++;}
    if(mappa[i][j]=='^') {i2-- ; while(i2>=0 && mappa[i2][j2]=='.') i2--;}
    if(mappa[i][j]=='<') {j2-- ; while(j2>=0 && mappa[i2][j2]=='.') j2--;}
    if(mappa[i][j]=='v') {i2++ ; while(i2<R && mappa[i2][j2]=='.') i2++;}

    if(i2>=R || i2<0 || j2<0 || j2>=C)
    {
        if(prev_[i][j]) ok[i][j]=true , sol++;
        else
        {
            ok[i][j]=true;

            i2=i,j2=j;
            if(mappa[i][j]!='>') {j2++ ; while(j2<C && mappa[i2][j2]=='.') j2++;
            if(j2<C) {sol++; if(!usato[i2][j2]) calcola(i2,j2); return true;}}

            i2=i,j2=j;
            if(mappa[i][j]!='^') {i2-- ; while(i2>=0 && mappa[i2][j2]=='.') i2--;
            if(i2>=0) {sol++; if(!usato[i2][j2]) calcola(i2,j2); return true;}}

            i2=i,j2=j;
            if(mappa[i][j]!='<') {j2-- ; while(j2>=0 && mappa[i2][j2]=='.') j2--;
            if(j2>=0) {sol++; if(!usato[i2][j2]) calcola(i2,j2); return true;}}

            i2=i,j2=j;
            if(mappa[i][j]!='v') {i2++ ; while(i2<R && mappa[i2][j2]=='.') i2++;
            if(i2<R) {sol++; if(!usato[i2][j2]) calcola(i2,j2); return true;}}
            return ok[i][j]=false;
        }
        return true;
    }

    if(!usato[i2][j2])  ok[i][j]=true , ok[i][j]=calcola(i2,j2);
    else ok[i][j]=ok[i2][j2];
    return ok[i][j];
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        scanf("%d%d",&R,&C);
        for(int i=0;i<R;++i)
            scanf("%s",mappa[i]);

        memset(prev_,false,sizeof prev_);
        memset(usato,false,sizeof usato);
        sol=0;
        for(int i=0;i<R;++i)
            for(int j=0;j<C;++j)
                if(mappa[i][j]!='.' && !usato[i][j]) prova(i,j);

        memset(usato,false,sizeof usato);
        memset(ok,false,sizeof ok);
        for(int i=0;i<R && sol!=-1;++i)
            for(int j=0;j<C && sol!=-1;++j)
                if(mappa[i][j]!='.' && !usato[i][j])
                {
                    if(!calcola(i,j)) sol=-1;
                }

        if(sol==-1) printf("Case #%d: IMPOSSIBLE\n",t);
        else printf("Case #%d: %d\n",t,sol);

    }

    return 0;
}
