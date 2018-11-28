# include<stdio.h>

FILE *fin  = fopen ("A-small-practice.in", "r");
FILE *fout = fopen ("A-small-practice.out", "w");
void solve();
int L,m,n;
int high[101][101];

int judge(int x,int y)
{
    int i;   
    int k = high[x][y];
    int totalX = 0,totalY = 0;
    
    for(i=0;i<m;i++) if (high[x][i]>k) totalX = 1;
    for(i=0;i<n;i++) if (high[i][y]>k) totalY = 1;
    
    if(totalX==1 && totalY==1)return 1;
        else
    return 0;
}


void solve()
{
    int i,j;    
     for(i=0;i<n;i++)
     for(j=0;j<m;j++)
      if(judge(i,j)==1) {
                        fprintf(fout,"Case #%d: NO\n",L);
                        return;
                        }
        
    fprintf(fout,"Case #%d: YES\n",L);  
    return;    
}


int main()
{
 int T,i,j;
 fscanf(fin,"%d",&T);
 for(L=1;L<=T;L++)
 {
     fscanf(fin,"%d%d",&n,&m);
     for(i=0;i<n;i++)
      for(j=0;j<m;j++)
        fscanf(fin,"%d",&high[i][j]);
        
     solve();
      
 }
 return 0;
}
