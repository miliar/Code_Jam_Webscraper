#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int a[1005],n,ans;
char s[1005];
void calculate();

int main()
{
    int i,j,k,t;
    
    FILE *fp,*ft;
    
    //fp=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest QLR\\A-small-attempt0.in","r+");
    fp=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest QLR\\A-large.in","r+");
    ft=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest QLR\\Standing Ovationoplarge.txt","w+");
    
    fscanf(fp,"%d",&t);
    
    //scanf("%d",&t);
    
    for(k=0;k<t;k++)
    {
        fscanf(fp,"%d",&n);
        //scanf("%d",&n);
        
        fscanf(fp,"%s",s);
        //scanf("%s",s);
        
        calculate();
        
        fprintf(ft,"Case #%d: %d\n",k+1,ans);
        //printf("Case #%d: %d\n",k+1,ans);
        
    }
    
    fclose(fp);
    fclose(ft);
    
    return 0;
}

void calculate()
{
    int i,j,k,l,p,q,temp;
    
    ans=0;
    
    for(i=0;i<=n;i++)
    {
        if(i==0)
        {
            a[i]=s[i]-'0';
        }
        else
        {
            if(a[i-1]<i)
            {
                ans+=i-a[i-1];
                a[i-1]=i;
            }
            
            a[i]=a[i-1]+s[i]-'0';
            
        }
    }
    
}

