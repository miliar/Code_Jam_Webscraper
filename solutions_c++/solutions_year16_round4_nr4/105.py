#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;


int t;
int n;

int map[31][31];
int m2[31][31];

int ans;

bool come[31];
bool used[31];
bool check(int nn)
{
    if(nn==n)
    {
        return true;
    }
    
    int i,j;
    
    for(i=1;i<=n;i++)
    {
        if(come[i]==0)
        {
            come[i]=1;
            bool flag=0;
            for(j=1;j<=n;j++)
            {
                if(used[j]==0 && m2[i][j]==1)
                {
                    flag=1;
                    used[j]=1;
                    if(check(nn+1)==false)
                    {
                       return false;
                    }
                    used[j]=0;
                }
            }
            if(flag==0)
            {
                return false;
            }
            come[i]=0;
        }
    }
    
    return true;
}



int main()
{
    int i,j,k,times;
    char d;
    int temp;
    int xx,yy,zz;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    cin>>t;
    
    for(times=1;times<=t;times++)
    {
        cin>>n;
        ans=999;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                cin>>d;
                map[i][j]=d-'0';
            }
        }
        
        for(i=0;i<(1<<(n*n));i++)
        {
            xx=0;
            temp=0;
            bool flag=0;
            for(j=1;j<=n;j++)
            {
                for(k=1;k<=n;k++)
                {
                    if((i&(1<<xx))!=0)
                    {
                        if(map[j][k]==0)
                        {
                            temp++;
                        }
                        m2[j][k]=1;
                    }
                    else
                    {
                        if(map[j][k]==1)
                        {
                            flag=1;
                        }
                        m2[j][k]=map[j][k];
                    }
                    
                    xx++;
                }
            }
            
            if(flag==1)continue;
            
            /*
            for(j=1;j<=n;j++)
            {
                for(k=1;k<=n;k++)
                {
                    cout<<m2[j][k]<<' ';
                }
                cout<<endl;
            }
            cout<<"(*&^%$#@"<<endl;
            */
            memset(used,0,sizeof(used));
            memset(come,0,sizeof(come));
            if(check(0)==true)
            {
                ans=min(ans,temp);
            }
        }
        
        
        cout<<"Case #"<<times<<": "<<ans<<endl;
    }
    
    
    
    
    return 0;
}
