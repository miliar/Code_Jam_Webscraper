#include <bits/stdc++.h>
using namespace std;
const char fileIn[]="input.txt";
const char fileOut[]="output.txt";
const bool file=1;
const int MAXN=1010;
char MAT[MAXN][MAXN];
int a[MAXN][MAXN];
bool valid[4][MAXN][MAXN];
int f(char c)
{
    if(c=='<') return 0;
    if(c=='>') return 1;
    if(c=='^') return 2;
    if(c=='v') return 3;
}
 //0-levo
        //1-desno
        //2-gore
        //3-dole
int main()
{
    if(file)
    {
        freopen(fileIn,"r",stdin);
        freopen(fileOut,"w",stdout);
    }
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        for(int i=0;i<4;i++)
            for(int j=0;j<MAXN;j++)
            for(int k=0;k<MAXN;k++) valid[i][j][k]=true;
        int r,c;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++)
            scanf("%s",MAT[i]);
        //0-levo
        //1-desno
        //2-gore
        //3-dole
        //Rows from left
        for(int i=0;i<r;i++)
        {
            int mostleft=-1;
            for(int j=0;j<c;j++) if(MAT[i][j]!='.') {mostleft=j;break;}
            if(mostleft!=-1) valid[0][i][mostleft]=false;
        }
        for(int i=0;i<r;i++)
        {
            int mostright=-1;
            for(int j=c-1;j>=0;j--) if(MAT[i][j]!='.') {mostright=j;break;}
            if(mostright!=-1) valid[1][i][mostright]=false;
        }
        for(int j=0;j<c;j++)
        {
            int mostup=-1;
            for(int i=0;i<r;i++)
            {
                if(MAT[i][j]!='.') {mostup=i;break;}
            }
            if(mostup!=-1) valid[2][mostup][j]=false;
        }
        for(int j=0;j<c;j++)
        {
            int mostdown=-1;
            for(int i=r-1;i>=0;i--)
            {
                if(MAT[i][j]!='.') {mostdown=i;break;}
            }
            if(mostdown!=-1) valid[3][mostdown][j]=false;
        }
        int ans=0;
        bool passed=true;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(MAT[i][j]=='.') continue;
                int cnt=0;
                if(valid[0][i][j]) cnt++;
                if(valid[1][i][j]) cnt++;
                if(valid[2][i][j]) cnt++;
                if(valid[3][i][j]) cnt++;
                if(cnt==0) passed=false;
                else if(!valid[f(MAT[i][j])][i][j]) ans++;
            }
        }
        if(passed) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
