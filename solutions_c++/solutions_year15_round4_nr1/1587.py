#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
    int cas;
    FILE *fr,*fw;
    fr=fopen("a.in","r");
    fw=fopen("a.out","w");
    fscanf(fr,"%d",&cas);
    for (int cas1=1;cas1<=cas;cas1++)
    {
        int r,c;
        fscanf(fr,"%d%d",&r,&c);
        char a[100][100];
        bool up[100][100],down[100][100],left[100][100],right[100][100];
        for (int i=0;i<r;i++) 
        {
            char ch;
            fscanf(fr,"%c",&ch);
            for (int j=0;j<c;j++)
                fscanf(fr,"%c",&a[i][j]);
        }
        for (int i=0;i<r;i++) 
        {
            bool f=false;
            for (int j=0;j<c;j++)
            {
                left[i][j]=f;
                if (a[i][j]!='.') f=true;
            }
            f=false;
            for (int j=c-1;j>=0;j--)
            {
                right[i][j]=f;
                if (a[i][j]!='.') f=true;
            }        
        }
        
        for (int j=0;j<c;j++) 
        {
            bool f=false;
            for (int i=0;i<r;i++)
            {
                up[i][j]=f;
                if (a[i][j]!='.') f=true;
            }
            f=false;
            for (int i=r-1;i>=0;i--)
            {
                down[i][j]=f;
                if (a[i][j]!='.') f=true;
            }        
        }
        
        int cnt=0; bool f=true;
        for (int i=0;i<r;i++)
            for (int j=0;j<c;j++)
            {
                if (a[i][j]=='^' && !up[i][j]) {if (!up[i][j] && !down[i][j] && !left[i][j] && !right[i][j]) f=false; else cnt++;}
                if (a[i][j]=='v' && !down[i][j]) {if (!up[i][j] && !down[i][j] && !left[i][j] && !right[i][j]) f=false; else cnt++;}
                if (a[i][j]=='<' && !left[i][j]) {if (!up[i][j] && !down[i][j] && !left[i][j] && !right[i][j]) f=false; else cnt++;}
                if (a[i][j]=='>' && !right[i][j]) {if (!up[i][j] && !down[i][j] && !left[i][j] && !right[i][j]) f=false; else cnt++;}
            }
        if (f) fprintf(fw,"Case #%d: %d\n",cas1,cnt); else fprintf(fw,"Case #%d: IMPOSSIBLE\n",cas1);
    }    
    return 0;
}
