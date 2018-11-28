#include<iostream>

using namespace std;

int main()
{
    int t,n,m;
    cin>>t;
    
    for(int p=0;p<t;p++){
    
    cin>>n>>m;
    
    int **a=new int*[n];
    
    for(int i=0;i<n;i++)
    {
        a[i]=new int[m];
        for(int j=0;j<m;j++)
        {
            cin>>a[i][j];
        }
    }
    
    int flg=1;
    
    for(int i=0;i<n;i++)
    {
        if(!flg)break;
        for(int j=0;j<m;j++)
        {
            if(a[i][j]==1)
            {
                //row wise checking
                for(int k=0;k<m;k++)
                {
                    if(a[i][k]!=1){flg=0;break;}
                }
                
                //column wise checking
                if(!flg)
                {
                    flg=1;
                    for(int k=0;k<n;k++)
                    {
                        if(a[k][j]!=1){flg=0;break;}
                    }
                    
                    
                }
            }
            if(!flg)break;
        }
        
    }
    
        
    

    if(flg)cout<<"Case #"<<p+1<<": "<<"YES"<<endl;
    else cout<<"Case #"<<p+1<<": "<<"NO"<<endl;
    }
}