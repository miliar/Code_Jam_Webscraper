#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;

struct node{
       int x,y;
       };


int n,m;
int map[101][101];



int g[5][2];

int ans;
int t;


bool check(int sx,int sy)
{
    int i;
    
    for(i=1;i<=n;i++)
    {
        if(i!=sx)
        {
             if(map[i][sy]!=0)
             {
                 return true;
             }
        }
    }
    for(i=1;i<=m;i++)
    {
        if(i!=sy)
        {
             if(map[sx][i]!=0)
             {
                 return true;
             }
        }
    }
    
    return false;
}



int main()
{
    int i,j,k,times;
    char d;
    node last;
    node now,st;
    int dir;
    bool flag;
    
    
    freopen("A-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    
    g[1][0]=-1;g[1][1]=0;
    g[2][0]=0;g[2][1]=1;
    g[3][0]=1;g[3][1]=0;
    g[4][0]=0;g[4][1]=-1;
    
    cin>>t;
    
    
    for(times=1;times<=t;times++)
    {
    
    
    
    cin>>n>>m;
    
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=m;j++)
        {
            cin>>d;
            if(d=='<')
            {
                map[i][j]=4;
            }
            else if(d=='>')
            {
                map[i][j]=2;
            }
            else if(d=='^')
            {
                map[i][j]=1;
            }
            else if(d=='v')
            {
                map[i][j]=3;
            }
            else
            {
                map[i][j]=0;
            }
        }
    }
    
    ans=0;
    flag=0;
    
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=m;j++)
        {
            if(map[i][j]==0)
            {
               continue;
            }
            
            dir=map[i][j];
            now.x=i;now.y=j;
            
            while(now.x>=1 && now.x<=n && now.y>=1 && now.y<=m)
            {
                 now.x+=g[dir][0];
                 now.y+=g[dir][1];
                 
                 if(now.x>=1 && now.x<=n && now.y>=1 && now.y<=m)
                 {
                     if(map[now.x][now.y]!=0)
                     {
                         break;
                     }
                 }
            }
            
            if(now.x>=1 && now.x<=n && now.y>=1 && now.y<=m)
            {
                
            }
            else
            {
                if(check(i,j)==true)
                {
                    ans++;
                }
                else
                {
                    flag=1;
                }
            }
            
            
        }
        
    }
    
    cout<<"Case #"<<times<<": ";
    
    if(flag==1)
    {
        cout<<"IMPOSSIBLE"<<endl;
    }
    else
    {
        cout<<ans<<endl;
    }
    
    
    }
    
    //system("pause");
    return 0;
}
