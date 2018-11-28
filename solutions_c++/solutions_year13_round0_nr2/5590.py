#include <iostream>

using namespace std;
int a[1001][1001];
int ans[1001][1001];
void mowj(int j);
void mowi(int i);
int n,m;
int main() 
{
    int t;
    cin>>t;
    for(int w=1;w<=t;w++)
    {
        cin>>n>>m;
    for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
                {
                    cin>>a[i][j];
                    ans[i][j]=2;
                }
                
        }
       
    for(int i=0;i<n;i++)
            mowi(i);
    for(int j=0;j<m;j++)    
            mowj(j);
    bool right=true;
    for(int i=0;i<n;i++)
        {
            
            for(int j=0;j<m;j++)
            {
                if(a[i][j]!=ans[i][j])
                    {
                        right=false;
                        break;
                    }
            }
            if(!right)
                    {
                        break;
                    }
        }
        if(right)
            cout<<"Case #"<<w<<": "<<"YES"<<endl;
        else
            cout<<"Case #"<<w<<": "<<"NO"<<endl;
    }
    
    return 0;
}
void mowj(int j)
{
    int i;
    for(i=0;i<n;i++)
        {
            if(a[i][j]==a[0][j]&&a[i][j]<2)
                {
                    continue;
                }
            else
                break;      
        }
    if(i==n)
        {
            for(int i=0;i<n;i++)
                ans[i][j]=1;
        }
}
void mowi(int i)
{
    int j;
    for(j=0;j<m;j++)
        {
            if(a[i][j]==a[i][0]&&a[i][j]<2)
                {
                    continue;
                }
            else
                break;      
        }
    if(j==m)
        {
            for(int j=0;j<m;j++)
                ans[i][j]=1;
        }
}
