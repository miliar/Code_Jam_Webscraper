#include<fstream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<set>
using namespace std;

ofstream fout("ans.out");
ifstream fin("B-large.in");

struct node{
       int num,id;
       };


int n,t;
node b[1011];
int a[1011];

int g[1011];
int f[1011][1011];
int ans;
int ll[1011],rr[1011];


bool cmp2(node xx,node yy)
{
    return xx.num<yy.num;
}

int main()
{
    int i,j,k,times;
    
    fin>>t;
    for(times=1;times<=t;times++)
    {
        fin>>n;
        for(i=1;i<=n;i++)
        {
            fin>>a[i];
            b[i].num=a[i];
            b[i].id=i;
        }
        
        sort(b+1,b+n+1,cmp2);
        for(i=1;i<=n;i++)
        {
             a[b[i].id]=i;
             g[i]=b[i].id;
        }
        
        for(i=1;i<=n;i++)
        {
            ll[i]=rr[i]=0;
            for(j=1;j<=i-1;j++)
            {
                if(a[j]<a[i])ll[i]++;
            }
            
            for(j=i+1;j<=n;j++)
            {
                if(a[j]<a[i])rr[i]++;
            }
        }
        
        
        
       // for(i=1;i<=n;i++)
       // {
       //     fout<<a[i]<<' ';
        //}
        //fout<<endl;
        
        
        memset(f,-1,sizeof(f));
        f[0][0]=0;
        for(i=0;i<=n-1;i++)
        {
            for(j=0;j<=i;j++)
            {
                if(f[i][j]!=-1)
                {
                     if(f[i+1][j+1]==-1 || f[i+1][j+1]>f[i][j]+(g[i+1]+(j-ll[g[i+1]])-(j+1)))
                     {
                         f[i+1][j+1]=f[i][j]+(g[i+1]+(j-ll[g[i+1]])-(j+1));
                     }
                     
                     if(f[i+1][j]==-1 || f[i+1][j]>f[i][j]+(n-(i-j))-(g[i+1]+(j-ll[g[i+1]]))  )
                     {
                         f[i+1][j]=f[i][j]+(n-(i-j))-(g[i+1]+(j-ll[g[i+1]]));
                     }
                }
            }
        }
        
        ans=2000000000;
        for(i=0;i<=n;i++)
        {
            ans=min(ans,f[n][i]);
        }
        
        //for(i=1;i<=n;i++)
        //{
        //    fout<<a[i]<<' ';
        //}
        //fout<<endl;
        
        
        fout<<"Case #"<<times<<": ";
        fout<<ans<<endl;
    }
    
    
    system("pause");
    return 0;
}
