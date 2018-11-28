#include<iostream>
#include<cstdio>
#include<math.h>
#include<algorithm>



using namespace std;

int s[102],n;

int solve(int key,int j,int p)
{
    int ans1=0,ans2=0,k=0,ans=0;
    if(j==n)
    return key;
            
            else if(p<=s[j])
            {
                ans1= (solve(key+1,j+1,p));
                ans2=(solve(key+1,j,p+p-1));
                ans=min(ans1,ans2);
                return(ans);
            }
            else if(p>s[j])
            {
                p=p+s[j];
                return (solve(key,j+1,p));
            }
            
}   



int main()
{
    FILE *fp,*fo;
    fp=fopen("input.txt","r");
    fo=fopen("output.txt","w");
    int t,a,i,p,ans,j;
    fscanf(fp,"%d",&t);
    for(i=1;i<=t;i++)
    {
        ans=0;
        fscanf(fp,"%d%d",&a,&n);
        for(j=0;j<n;j++)
        {
            fscanf(fp,"%d",&s[j]);
        }
        sort(s,s+n);
       
        p=a;
        if(p==1)
        ans=n;
        else
        {
        ans=solve(0,0,p);
        }
        fprintf(fo,"Case #%d: %d\n",i,ans);
    }
    fclose(fp);
    fclose(fo);
    return 0;
}
