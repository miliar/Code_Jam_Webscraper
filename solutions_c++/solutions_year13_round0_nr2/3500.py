#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int a[101][101];
int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);
    
    int t,k,i,j,l,n,m,flag0,flag1;
    scanf("%d",&t);
    k=0;
    while(t--)
    {
        scanf("%d%d",&n,&m);
        memset(a,0,sizeof(a));
        for(i=0;i<n;++i)
        {
            for(j=0;j<m;++j)
            scanf("%d",&a[i][j]);
        }
        for(i=0;i<n;++i)
        {
            for(j=0;j<m;++j)
            {
                flag0=flag1=0;
                for(l=0;l<n;++l)
                {
                    if(a[i][j]<a[l][j])
                    {
                        flag0=1;
                        //cout<<"0 "<<i<<" "<<j<<endl;
                        break;
                    }
                }
                for(l=0;l<m;++l)
                {
                    if(a[i][j]<a[i][l])
                    {
                        flag1=1;
                        //cout<<"1 "<<i<<" "<<j<<endl;
                        break;
                    }
                }
                if(flag0 && flag1)
                break;
            }
            if(flag0 && flag1)
            break;
        }
        if(!flag0 || !flag1)
        printf("Case #%d: YES\n",++k);
        else
        printf("Case #%d: NO\n",++k);
    }
    return 0;
}
        
            
                    
        
