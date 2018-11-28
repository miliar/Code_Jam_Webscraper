#include<cstdio>
#include<iostream>
#include<string.h>

using namespace std;

char s[1000002];

int main()
{
    FILE *fp,*fo;
    fp=fopen("input.txt","r");
    fo=fopen("output.txt","w");
    int t,i,l,n,j,count=1,ans=0,k,p,max1=0;
    fscanf(fp,"%d",&t);
    for(i=1;i<=t;i++)
    {
        ans=0,
        count=0;
        fscanf(fp,"%s%d",&s,&n);
        l=strlen(s);
        for(j=0;j<l;j++)
        {
            for(k=j;k<l;k++)
            {
                count=0;
                max1=0;
                for(p=j;p<=k;p++)
                {
                   
                if(s[p]!='a' && s[p]!='e' && s[p]!='i' && s[p]!='o' && s[p]!='u' )
                {
                    count++;
                }
                else
                { 
                    count=0;
                }
                if(count>=max1)
                        max1=count;
                    
                }
                //cout<<j<<" "<<k<<" "<<max1<<endl;
                //cout<<max<<"sid\n";
                if(max1>=(n))
                ans++;
            }
       
            }
        fprintf(fo,"Case #%d: %d\n",i,ans);
    }
    fclose(fp);
    fclose(fo);
    return 0;
}
