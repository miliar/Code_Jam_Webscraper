#include<fstream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<set>
using namespace std;

ofstream fout("ans.out");
ifstream fin("data.in");


struct node{
       char d[102];
       int len;
       };


int ans1,ans2;
int t,m,n;
int slen;
node s[1001];

int adj[1001];
int dis[1001][1001];
int f[11][11][10001];

int get_num(int now)
{
    int i=0;
    while(i<s[now].len && i<s[now+1].len)
    {
         if(s[now].d[i]!=s[now+1].d[i])
         {
             break;
         }
         
         i++;
    }
    
    return i;
}


bool cmp2(node xx,node yy)
{
     int i=0;
     while(i<xx.len && i<yy.len)
     {
         if(xx.d[i]!=yy.d[i])
         {
             break;
         }
         
         i++;
     }
     
     if(i>xx.len || i>yy.len)
     {
         return xx.len<yy.len;
     }
     
     return xx.d[i]<yy.d[i];
}


int main()
{
    int i,j,k,times,z;
    int temp;
    int p,q;
    fin>>t;
    
    for(times=1;times<=t;times++)
    {
         fin>>m>>n;
         slen=0;
         for(i=1;i<=m;i++)
         {
              fin>>s[i].d;
              s[i].len=strlen(s[i].d);
              slen+=s[i].len;
         }
         
         
         sort(s+1,s+m+1,cmp2);
         
        // return 0;
        /*
         for(i=1;i<=m;i++)
         {
              for(j=0;j<s[i].len;j++)
              {
                  fout<<s[i].d[j];
              }
              fout<<endl;
         }
         fout<<endl;
         */
         
         
         for(i=1;i<m;i++)
         {
             adj[i]=get_num(i);
            // fout<<adj[i]<<' ';
         }
         //fout<<endl;
         
         for(i=1;i<=m;i++)
         {
             dis[i][0]=dis[0][i]=0;
         }
         
         for(i=1;i<=m;i++)
         {
             temp=99999;
             for(j=i+1;j<=m;j++)
             {
                  temp=min(temp,adj[j-1]);
                  
                  dis[i][j]=dis[j][i]=temp;
                  //fout<<dis[i][j]<<' ';
             }
             //fout<<endl;
         }
         
         
         ans1=0;
         for(i=n+1;i<=m;i++)
         {
              ans1+=dis[i][i-n];
         }
         
         fout<<"Case #"<<times<<": ";
         fout<<slen+n-ans1<<' ';
         
         memset(f,0,sizeof(f));
         f[0][0][0]=1;
         
         for(i=1;i<=m;i++)
         {
            for(j=1;j<=n;j++)
            {
                for(k=0;k<=slen;k++)
                {
                     f[i][j][k]+=f[i-1][j-1][k];
                     for(z=1;z<=i-1;z++)
                     {
                         if(k-dis[i][z]>=0)
                             f[i][j][k]+=f[i-1][j][k-dis[i][z]];
                     }
                     fout<<f[i][j][k]<<' ';
                }
                fout<<"    "<<endl;
            }
            fout<<endl;
         }
         
         fout<<f[m][n][ans1]<<endl;
         
    }
    
    
    system("pause");
    return 0;
}
