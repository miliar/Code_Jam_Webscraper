#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>

using namespace std;

long long int gr[20][20];
long long int n,r,c,ans;
void calculate();
long long int get_min(long long int,long long int,long long int);
//void init();

int main()
{
    int i,j,k,t;
    
    FILE *fp,*ft,*fk;
    
    fp=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest R1B\\B-small-attempt0.in","r+");
    ft=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest R1B\\Noisy Neighbors.txt","w+");
    fk=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest R1B\\Noisy Ngprc.txt","w+");
    
    fscanf(fp,"%d",&t);
    
    //scanf("%d",&t);
    
    //init();
    
    for(k=0;k<t;k++)
    {
        fscanf(fp,"%lld%lld%lld",&r,&c,&n);
        //scanf("%lld%lld%lld",&r,&c,&n);
        
        calculate();
        
        fprintf(ft,"Case #%d: %lld\n",k+1,ans);
        fprintf(fk,"Case #%d: %lld %lld %lld\n",k+1,r,c,n);
        //printf("Case #%d: %lld\n",k+1,ans);
        
    }
    
    fclose(fp);
    fclose(ft);
    fclose(fk);
    
    return 0;
}

void calculate()
{
    long long int i;
    
    ans=get_min(0,0,0);
    
}

long long int get_min(long long int i,long long int j,long long int m)
{
    long long int t1,t2,s,temp;
    
    if(i>=r && m!=n)
    {
        return 2000000000;
    }
    else if(i>=r && m==n)
    {
        return 0;
    }
    
    if(j!=c-1)
    {
        gr[i][j]=0;
        t1=get_min(i,j+1,m);
        
        gr[i][j]=1;
        t2=get_min(i,j+1,m+1);
        
        if(i>0 && gr[i-1][j]==1)
        {
            t2++;
        }
        if(j>0 && gr[i][j-1]==1)
        {
            t2++;
        }
        
        s=min(t1,t2);
        
    }
    else
    {
        gr[i][j]=0;
        t1=get_min(i+1,0,m);
        
        gr[i][j]=1;
        t2=get_min(i+1,0,m+1);
        
        if(i>0 && gr[i-1][j]==1)
        {
            t2++;
        }
        if(j>0 && gr[i][j-1]==1)
        {
            t2++;
        }
        
        s=min(t1,t2);
        
    }
    
    return s;
    
}

