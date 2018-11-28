#include<bits/stdc++.h>
using namespace std;

int DP[60000][2][10];
bool vis[60000][2][10];
char V[60000][10];

int R,C=10,W;
int pwr[12];
char str[12];

void conv(int mask)
{
    int i;
    for(i=0; i<C; i++)  str[i]=0;
    i=0;
    while(mask>0)
    {
        str[i++]=(mask%3);
        mask/=3;
    }
    for(i=0; i<C; i++)  printf("%d",str[i]);
    printf("\n");
}

char vallid(int mask,int pos)
{
    if(V[mask][pos]!=-1)  return V[mask][pos];

    int i;
    char f=1;
    int nmask=mask;
    for(i=0; i<C; i++)
    {
        if(nmask%3==1 && (i>=pos && i<pos+W))
        {
            f=0;
            break;
        }
        else if(nmask%3==2 && !(i>=pos && i<pos+W))
        {
            f=0;
            break;
        }
        nmask/=3;
    }
    return V[mask][pos]=f;
}

int terminal(int state,int boat)
{
    for(int i=0; i<C; i++)
    {
        if(i>=boat && i<boat+W)
        {
            if(state%3==0)  return 0;
        }
        state/=3;
    }
    return 1;
}

int F(int state,int pl,int g)
{
     if(vis[state][pl][g])  return DP[state][pl][g];
     int& ret=DP[state][pl][g];
     vis[state][pl][g]=1;
     int i,tmp;

     int ns,nmask;
     if(pl==0)
     {
         ret=100;
         ns=state;
         for(i=0; i<C; i++)
         {
            if(ns%3==0)
            {
                tmp=F(state,1,i);
                ret=min(tmp,ret);
            }
            ns/=3;
         }
         ret+=1;
         return ret;
     }

     if(pl==1)
     {
         ret=0;
         for(i=0; i<=C-W; i++)
         {
             if(vallid(state,i))
             {
                 if(g>=i && g<i+W)
                 {
                     nmask=state+2*pwr[g];
                 }
                 else nmask=state+pwr[g];
                 if(terminal(nmask,i)){
                    ret=max(ret,0);
                    continue;
                 }
                 tmp=F(nmask,0,0);
                 ret=max(ret,tmp);
             }
         }
         return ret;
     }
}

int main()
{

    int T,it,i,j,k;
    //conv(33);
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    pwr[0]=1;
    for(i=1; i<=10; i++){
            pwr[i]=3*pwr[i-1];
    //printf("%d\n",pwr[i]);
    }


    scanf("%d",&T);
    for(it=1; it<=T; it++)
    {
        scanf("%d%d%d",&R,&C,&W);
        memset(vis,0,sizeof(vis));
        memset(V,-1,sizeof(V));
        int Ans=F(0,0,0);
        printf("Case #%d: %d\n",it,Ans);
    }
    return 0;
}
