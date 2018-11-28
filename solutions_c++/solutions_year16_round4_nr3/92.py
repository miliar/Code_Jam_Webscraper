#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;

struct node{
    int x,y;
    int from;
    node(int xx,int yy,int ff)
    {
        x=xx;y=yy;
        from=ff;
    }
    node()
    {
    }
};


int t;
int r,c;

int a[41],b[41];

int next[4][2];
int g[4][2];

int map[31][31];

node get_node(int x)
{
    if(x<=c)
    {
        return node(1,x,0);
    }
    
    if(x<=r+c)
    {
        return node(x-c,c,1);
    }
    
    if(x<=r+c+c)
    {
        return node(r,c-(x-r-c)+1,2);
    }
    
    return node(r-(x-r-c-c)+1,1,3);
}


bool check()
{
    int i,j,k;
    int xx,yy;
    int nx,ny;
    int dir;
    node aa,bb;
    
    /*
    for(i=1;i<=r;i++)
    {
        for(j=1;j<=c;j++)
        {
            cout<<map[i][j]<<' ';
        }
        cout<<endl;
    }
    cout<<"()*&^%$#@#$%^&*(*&^%"<<endl;
    */
    
    for(i=1;i<=r+c;i++)
    {
        xx=a[i];yy=b[i];
        aa=get_node(xx);
        bb=get_node(yy);
        
        //cout<<xx<<' '<<yy<<" xxyy"<<endl;
        //cout<<aa.x<<' '<<aa.y<<' '<<aa.from<<"   aaaa"<<endl;
        //cout<<bb.x<<' '<<bb.y<<' '<<bb.from<<"   bbbb"<<endl;
        
        
        while(aa.x>=1 && aa.x<=r && aa.y>=1 && aa.y<=c)
        {
            dir=next[aa.from][map[aa.x][aa.y]];
            //cout<<dir<<"  dir"<<endl;
            //cout<<aa.x<<' '<<aa.y<<' '<<aa.from<<endl;
            //system("pause");
            nx=aa.x+g[dir][0];
            ny=aa.y+g[dir][1];
            
            
            aa.x=nx;aa.y=ny;
            aa.from=(dir+2)%4;
        }
        
        if(aa.x!=bb.x+g[bb.from][0] || aa.y!=bb.y+g[bb.from][1])
        {
            return false;
        }
    }
    return true;
}


int main()
{
    int i,j,k,times;
    int z;
    int xx,yy,zz;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    
    next[0][0]=3;
    next[0][1]=1;
    
    next[1][0]=2;
    next[1][1]=0;
    
    next[2][0]=1;
    next[2][1]=3;
    
    next[3][0]=0;
    next[3][1]=2;
    
    
    g[0][0]=-1;g[0][1]=0;
    g[1][0]=0;g[1][1]=1;
    g[2][0]=1;g[2][1]=0;
    g[3][0]=0;g[3][1]=-1;
    
    
    cin>>t;
    
    for(times=1;times<=t;times++)
    {
        cin>>r>>c;
        
        for(i=1;i<=r+c;i++)
        {
            cin>>a[i]>>b[i];
        }
        
        cout<<"Case #"<<times<<":"<<endl;
        for(z=0;z<(1<<(r*c));z++)
        {
            //cout<<z<<endl;
            xx=0;
            for(i=1;i<=r;i++)
            {
                for(j=1;j<=c;j++)
                {
                    if((z&(1<<xx))!=0)
                    {
                        map[i][j]=1;
                    }
                    else
                    {
                        map[i][j]=0;
                    }
                    xx++;
                }
            }
            ////////////////////////////
            if(check()==true)
            {
            for(i=1;i<=r;i++)
            {
                for(j=1;j<=c;j++)
                {
                    if(map[i][j]==1)
                    {
                        cout<<'\\';
                    }
                    else
                    {
                        cout<<'/';
                    }
                }
                cout<<endl;
            }
            
            break;
            }
            
        }
        
        if(z<(1<<(r*c)))
        {
            continue;
        }
        
        
        
        cout<<"IMPOSSIBLE"<<endl;
    }
    
    
    
    return 0;
}
