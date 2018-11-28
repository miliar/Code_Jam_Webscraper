#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int kasus,r,c,jml,ar[7],con[7][7],cnt;
bool bisa,udah,pas[7][7];
char peta[7][7];
const int dr[8] = {-1,-1,-1,0,1,1,1,0};
const int dc[8] = {-1,0,1,1,1,0,-1,-1};

void pecah(int a,int b)
{
    for (int m=0;m<8;m++)
    {
        if ((a+dr[m]<0)||(b+dc[m]<0)||(a+dr[m]>=r)||(b+dc[m]>=c)) continue;
        if ((peta[a+dr[m]][b+dc[m]]=='*')||(pas[a+dr[m]][b+dc[m]])) continue;
        pas[a+dr[m]][b+dc[m]] = true;
        if (con[a+dr[m]][b+dc[m]]==0) pecah(a+dr[m],b+dc[m]);
    }
}

bool cek()
{
    cnt = 0;
    memset(con,0,sizeof(con));
    int rr = -1, cc = -1;
    for (int i=0;i<r;i++)
    {
        for (int j=0;j<c;j++)
        {
            if (peta[i][j]=='*') continue;
            for (int m=0;m<8;m++)
            {
                if ((i+dr[m]<0)||(j+dc[m]<0)||(i+dr[m]>=r)||(j+dc[m]>=c)) continue;
                con[i][j] += (peta[i+dr[m]][j+dc[m]]=='*');
            }
            cnt++;
            if (con[i][j]==0)
            {
                rr = i;
                cc = j;
            }
        }
    }
    
    /*cout << endl;
            for (int i=0;i<r;i++)
            {
                for (int j=0;j<c;j++) cout << con[i][j];
                cout << endl;
            }*/
    
    if (rr==-1 || cnt != jml) return false;
    memset(pas,0,sizeof(pas));
    pas[rr][cc] = true;
    pecah(rr,cc);
    for (int i=0;i<r;i++)
        for (int j=0;j<c;j++)
            if (peta[i][j]=='.' && !pas[i][j]) return false;
    return true;
}

void dfs(int kol)
{
    if (kol == c)
    {
        bisa = cek();
        if (bisa)
        {
            udah = false;
            for (int i=0;i<r;i++)
            {
                for (int j=0;j<c;j++)
                {
                    if (peta[i][j]=='.')
                    {
                        if (con[i][j]==0)
                        {
                            if (udah) printf(".");
                            else {udah = true; printf("c");}
                        }
                        else printf(".");
                    }
                    else printf("*");
                }
                printf("\n");
            }
            /*cout << endl;
            for (int i=0;i<r;i++)
            {
                for (int j=0;j<c;j++) cout << con[i][j];
                cout << endl;
            }*/
            return;
        }
    }
    else
    {
        dfs(kol+1);
        if (bisa) return;
        for (int i=0;i<r;i++)
        {
            peta[i][kol] = '.';
            dfs(kol+1);
            if (bisa) return;
        }
        for (int i=0;i<r;i++) peta[i][kol] = '*';
    }
}

int main()
{   
//    freopen("C-small-attempt0.in","r",stdin);
//    freopen("c.out","w",stdout);
    
    scanf("%d",&kasus);
    for (int z=1;z<=kasus;z++)
    {
        scanf("%d %d %d",&r,&c,&jml);
        jml = r*c-jml;
        printf("Case #%d:\n",z);
        if (jml==1)
        {
            for (int i=0;i<r;i++)
            {
                for (int j=0;j<c;j++)
                {
                    if (i==0 && j==0) printf("c");
                    else printf("*");
                }
                printf("\n");
            }
            continue;
        }
        
        for (int i=0;i<r;i++)
            for (int j=0;j<c;j++)
                peta[i][j] = '*';
                
        bisa = false;
        dfs(0);
        
        if (!bisa) printf("Impossible\n");
    }
    return 0;
}
