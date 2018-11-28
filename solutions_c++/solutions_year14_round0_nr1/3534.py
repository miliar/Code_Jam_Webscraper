#include<stdio.h>
#include<algorithm>
using namespace std;

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int ans;
int vis[20];

int main()
{
    int i , a , j , cases , flag , ret;
    int caseID = 0;
    
    fscanf(in,"%d",&cases);
    while(cases--)
    {
        memset(vis,0,sizeof vis);
        
        fscanf(in,"%d",&ans);
        ans--;
        
        for(i=0;i<4;i++)
            for(a=0;a<4;a++)
            {
                fscanf(in,"%d",&j);
                if(i == ans) vis[j]++;
            }
        
        fscanf(in,"%d",&ans);
        ans--;
        
        for(i=0;i<4;i++)
            for(a=0;a<4;a++)
            {
                fscanf(in,"%d",&j);
                if(i == ans) vis[j]++;
            }
        
        flag = 0;
        for(i=1;i<=16;i++)
            if(vis[i] == 2)
                ret = i , flag++;
        
        fprintf(out,"Case #%d: ",++caseID);
        if(flag > 1) fprintf(out,"Bad magician!\n");
        if(flag == 1) fprintf(out,"%d\n",ret);
        if(!flag) fprintf(out,"Volunteer cheated!\n");
        
    }
    
    return 0;
}
