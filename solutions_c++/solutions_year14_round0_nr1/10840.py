#include<cstdio>
#include<cstring>

FILE *fin,*fout;
int t,ca,n,ans,a,b,c,d,e,f,g,h;
int used[20];

int main()
{
    fin=fopen("A-small-attempt6.in","r");
    fout=fopen("A.txt","w");
    fscanf(fin,"%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        memset(used,0,sizeof(used));
        fscanf(fin,"%d",&n);
        for(int i=1;i<=4;i++)
            if(i==n)
            {
                fscanf(fin,"%d%d%d%d",&a,&b,&c,&d);
                used[a]=used[b]=used[c]=used[d]=1;
            }
            else
                fscanf(fin,"%d%d%d%d",&a,&b,&c,&d);
        ans=0;
        fscanf(fin,"%d",&n);
        for(int i=1;i<=4;i++)
            if(i==n)
                fscanf(fin,"%d%d%d%d",&a,&b,&c,&d);
            else
                fscanf(fin,"%d%d%d%d",&e,&f,&g,&h);
        if(used[a]==1)
            ans=a;
        if(used[b]==1)
        {
            if(ans==0)
                ans=b;
            else
                ans=-1;
        }
        if(used[c]==1)
        {
            if(ans==0)
                ans=c;
            else
                ans=-1;
        }
        if(used[d]==1)
        {
            if(ans==0)
                ans=d;
            else
                ans=-1;
        }
        fprintf(fout,"Case #%d: ",ca);
        if(ans==0)
            fprintf(fout,"Volunteer cheated!\n");
        else if(ans==-1)
            fprintf(fout,"Bad magician!\n");
        else
            fprintf(fout,"%d\n",ans);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
