
#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int x,r,c,ans;
void calculate();

int main()
{
    int i,j,k,t;
    
    FILE *fp,*ft;
    
    fp=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest QLR\\D-small-attempt1.in","r+");
    ft=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest QLR\\Ominoussmall3.txt","w+");
    
    fscanf(fp,"%d",&t);
    
    //scanf("%d",&t);
    
    for(k=0;k<t;k++)
    {
        fscanf(fp,"%d%d%d",&x,&r,&c);
        //scanf("%d%d%d",&x,&r,&c);
        
        calculate();
        
        if(ans==0)
        {
            fprintf(ft,"Case #%d: RICHARD\n",k+1);
            //printf("Case #%d: RICHARD\n",k+1);
        }
        else
        {
            fprintf(ft,"Case #%d: GABRIEL\n",k+1);
            //printf("Case #%d: GABRIEL\n",k+1);
        }
        
    }
    
    fclose(fp);
    fclose(ft);
    
    return 0;
}

void calculate()
{
    int i,j,temp;
    
    ans=0;
    
    if(x==1)
    {
        ans=1;
    }
    else if(x==2)
    {
        temp=r*c;
        
        if(temp%x==0)
        {
            ans=1;
        }
        else
        {
            ans=0;
        }
        
    }
    else if(x==3)
    {
        temp=r*c;
        
        if(temp%x==0)
        {
            if(r==1 || c==1)
            {
                ans=0;
            }
            else
            {
                ans=1;
            }
        }
        else
        {
            ans=0;
        }
        
    }
    else if(x==4)
    {
        temp=r*c;
        
        if(temp%x==0)
        {
            if(temp==4 || temp==8)
            {
                ans=0;
            }
            else
            {
                ans=1;
            }
        }
        else
        {
            ans=0;
        }
        
    }
    
    //printf("%d %d %d ",x,r,c);
    
}


