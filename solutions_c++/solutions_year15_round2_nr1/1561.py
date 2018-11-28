#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>

using namespace std;

long long int dp[1000005];
long long int n,ans;
void calculate();
long long int rev(long long int);
//long long int get_min(long long int);
void init();

int main()
{
    int i,j,k,t;
    
    FILE *fp,*ft,*fk;
    
    fp=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest R1B\\A-small-attempt1.in","r+");
    ft=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest R1B\\Counter Culture4.txt","w+");
    fk=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest R1B\\Countercprac2.txt","w+");
    
    fscanf(fp,"%d",&t);
    
    //scanf("%d",&t);
    
    init();
    
    for(k=0;k<t;k++)
    {
        fscanf(fp,"%lld",&n);
        //scanf("%lld",&n);
        
        calculate();
        
        fprintf(ft,"Case #%d: %lld\n",k+1,ans);
        fprintf(fk,"Case #%d: %lld\n",k+1,n);
        //printf("Case #%d: %lld\n",k+1,ans);
        
    }
    
    fclose(fp);
    fclose(ft);
    fclose(fk);
    
    return 0;
}

void init()
{
    long long int i,j,revv,k,temp;
    
    dp[1]=1;
    
    for(i=2;i<=1000001;i++)
    {
        //printf("i=%lld\n",i);
        
        dp[i]=min(i,dp[i-1]+1);
        
        revv=rev(i);
        
        if(i%10!=0 && revv<i)
        {
            dp[i]=min(dp[i],dp[revv]+1);
        }
        
        //printf("i=%lld revv=%lld dp[i]=%lld\n",i,revv,dp[i]);
        
    }
    
}

void calculate()
{
    long long int i;
    
    ans=0;
    
    ans=dp[n];
    
}

/*
long long int get_min(long long int m)
{
    long long int t1,t2,revv,s;
    
    //printf("m=%lld\n",m);
    
    if(m==1)
    {
        return 1;
    }
    
    if(dp[m]!=-1)
    {
        return dp[m];
    }
    
    t1=1+get_min(m-1);
    //printf("jj\n");
    revv=rev(m);
    
    if(revv<m && revv>=1)
    {
        t2=1+get_min(revv);
        s=min(t1,t2);
    }
    else
    {
        s=t1;
    }
    
    dp[m]=s;
    
    return s;
    
}
*/

long long int rev(long long int m)
{
    long long int r,i,d,k,temp,t1;
    
    temp=m;
    
    while(temp%10==0)
    {
        //printf("inin");
        temp=temp/10;
    }
    
    t1=temp;
    d=0;
    
    while(t1)
    {
        t1/=10;
        d++;
    }
    
    k=1;
    for(i=1;i<d;i++)
    {
        k*=10;
    }
    
    //k=pow(10,d-1);
    t1=0;
    
    //printf("temp=%lld d=%lld k=%lld\n",temp,d,k);
    
    while(temp)
    {
        r=temp%10;
        t1=t1+(r*k);
        temp/=10;
        k/=10;
    }
    
    //printf("hi-end %lld\n",t1);
    
    return t1;
}

