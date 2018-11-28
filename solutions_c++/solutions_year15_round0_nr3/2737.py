
#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

//i=2 //j=3 //k=4

int dj[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int l,x,ans;
char s[10005];
char ss[10005];
void calculate();

int main()
{
    int i,j,k,t;
    
    FILE *fp,*ft;
    
    fp=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest QLR\\C-small-attempt2.in","r+");
    ft=fopen("F:\\Projects\\PROJECTS\\PROGRAMMING\\Code Jam\\contest QLR\\djksmall3.txt","w+");
    
    fscanf(fp,"%d",&t);
    
    //scanf("%d",&t);
    
    for(k=0;k<t;k++)
    {
        fscanf(fp,"%d%d",&l,&x);
        //scanf("%d%d",&l,&x);
        
        fscanf(fp,"%s",s);
        //scanf("%s",s);
        
        calculate();
        
        if(ans==0)
        {
            fprintf(ft,"Case #%d: NO\n",k+1);
            //printf("Case #%d: NO\n",k+1);
        }
        else
        {
            fprintf(ft,"Case #%d: YES\n",k+1);
            //printf("Case #%d: YES\n",k+1);
        }
        
    }
    
    fclose(fp);
    fclose(ft);
    
    return 0;
}

void calculate()
{
    int i,j,k,m,n,o,p,q,ck,s1,s2,s3,temp,prev,flag,prs1,prs2,prs3;
    
    ans=0;
    ck=0;
    i=0;
    j=0;
    k=0;
    
    //printf("%d %d\n",l,x);
    //printf("%s\n",s);
    /*
    for(i=0;i<5;i++)
    {
        for(j=0;j<5;j++)
        {
            printf("%d ",dj[i][j]);
        }
        printf("\n");
    }
    */
    for(i=0;i<x;i++)
    {
        for(j=0;j<l;j++)
        {
            ss[k]=s[j];
            k++;
        }
    }
    
    i=0;
    j=0;
    k=0;
    ck=0;
    s1=0;
    s2=0;
    s3=0;
    prs1=0;
    prs2=0;
    prs3=0;
    flag=0;
    
    while(ck!=3 && flag!=1 && flag!=2 && flag!=3)
    {
        m=0;
        if(prs1!=0)
        {
            m=prs1+1;
            prev=i;
            temp=0;
        }
        
        while(m<l*x && temp!=2)
        {
            if(ss[m]=='i')
            {
                temp=2;
            }
            else if(ss[m]=='j')
            {
                temp=3;
            }
            else
            {
                temp=4;
            }
            
            if(m==0)
            {
                prev=temp;
            }
            else
            {
                if(prev<0)
                {
                    temp=-dj[-prev][temp];
                }
                else
                {
                    temp=dj[prev][temp];
                }
                
                prev=temp;
            }
            //printf("m=%d %d\n",m,temp);
            m++;
        }
        
        if(m<l*x)
        {
            s1=m;
            prs1=s1;
            ck=1;
        }
        else
        {
            flag=1;
            break;
        }
        
        s2=s1;
        //printf("s1=%d m=%d flag=%d\n",s1,m,flag);
        
        while(ck!=3 && flag!=2 && flag!=3)
        {
            n=s1;
            //printf("hihi\n");
            
            if(prs2!=0)
            {
                n=prs2+1;
                prev=j;
                temp=0;
            }
            
            while(n<l*x && temp!=3)
            {
                if(ss[n]=='i')
                {
                    temp=2;
                }
                else if(ss[n]=='j')
                {
                    temp=3;
                }
                else
                {
                    temp=4;
                }
                
                if(n==s1)
                {
                    prev=temp;
                }
                else
                {
                    if(prev<0)
                    {
                        temp=-dj[-prev][temp];
                    }
                    else
                    {
                        temp=dj[prev][temp];
                    }
                    
                    prev=temp;
                }
                //printf("n=%d %d\n",n,temp);
                n++;
            }
            
            if(n<l*x)
            {
                s2=n;
                ck=2;
                prs2=n;
            }
            else
            {
                flag=2;
                break;
            }
            
            s3=s2;
            
            //printf("s2=%d n=%d flag=%d\n",s2,n,flag);
            
            while(ck!=3 && flag!=3)
            {
                o=s2;
                
                while(o<l*x)
                {
                    if(ss[o]=='i')
                    {
                        temp=2;
                    }
                    else if(ss[o]=='j')
                    {
                        temp=3;
                    }
                    else
                    {
                        temp=4;
                    }
                    
                    if(o==s2)
                    {
                        prev=temp;
                    }
                    else
                    {
                        if(prev<0)
                        {
                            temp=-dj[-prev][temp];
                        }
                        else
                        {
                            temp=dj[prev][temp];
                        }
                        
                        prev=temp;
                    }
                    //printf("o=%d %d\n",o,temp);
                    o++;
                }
                
                if(temp==4)
                {
                    s3=o;
                    ck=3;
                }
                else
                {
                    //flag=3;
                    break;
                }
                
                //printf("s3=%d o=%d flag=%d\n",s3,o,flag);
            }
            
            if(ck==3)
            {
                ans=1;
                break;
            }
        }
        
    }
    
    //printf("ck=%d\n",ck);
    
}



