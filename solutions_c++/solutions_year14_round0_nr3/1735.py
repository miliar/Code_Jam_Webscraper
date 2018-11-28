#include<math.h>
#include<algorithm>
#include<cstdlib>
#include<iostream>
#include<stdio.h>
#include<map>
#include<ext/hash_map>
#include<ext/hash_set>
#include<set>
#include<string>
#include<assert.h>
#include<vector>
#include<time.h>
#include<queue>
#include<deque>
#include<sstream>
#include<stack>
#include<sstream>
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ep 0.0000000001
#define INF 1001001001
#define P 1000000007
#define pr(x) ((x)>=P?(x)-P:(x))
using namespace std;
const int N=100201;
int n,m,i,j,k,f,fi;
int a[50];
int c[100];
int fix[50][50];
int fu[50][50],xx,yy;
bool fin;
void gg(int x,int y)
{
   if (fix[x][y]!=fi) fix[x][y]=fi,f++;
   
    for (int i=x-1;i<=x+1;i++)
    for (int j=y-1;j<=y+1;j++)
    if (i>0 && i<=n && j>0 && j<=m) 
     if (fix[i][j]!=fi && fu[i][j]==0) fix[i][j]=fi,f++;
    
    for (int i=x-1;i<=x+1;i++)
    for (int j=y-1;j<=y+1;j++)
    if (fix[i][j]!=fi && fu[i][j]==1) gg(i,j);     
     }
void go(int x,int s)
{
     if (x==n)
     {
              if (s==k)
              {
                    /*   for (int i=1;i<=n;i++)
                       {for (int j=1;j<=m;j++)
                        cout<<((a[i]&(1<<(j)))>0);
                        cout<<endl;
                       }*/
                       
                       for (int i=1;i<=n;i++)
                       for (int j=1;j<=m;j++){                       
                           fu[i][j]=0;
                       if ((a[i]&(1<<(j)))==0)
                       if ((a[i]&(1<<(j+1)))==0)
                       if ((a[i]&(1<<(j-1)))==0)
                       if ((a[i-1]&(1<<(j)))==0)
                       if ((a[i-1]&(1<<(j+1)))==0)
                       if ((a[i-1]&(1<<(j-1)))==0)
                       if ((a[i+1]&(1<<(j)))==0)
                       if ((a[i+1]&(1<<(j+1)))==0)
                       if ((a[i+1]&(1<<(j-1)))==0)
                       fu[i][j]=1;
                       }
                /*        for (int i=1;i<=n;i++)
                       {for (int j=1;j<=m;j++)
                        cout<<fu[i][j];
                        cout<<endl;
                       }
                       */
                        for (int i=1;i<=n;i++)
                       for (int j=1;j<=m;j++)
                       if (fu[i][j]==1){                       
                          fi++;
                           f=0;
                           gg(i,j);
                           if (f+k==n*m) fin=1;
                           fu[i][j]=27;
                       /* cout<<f<<endl;
                         system("pause");*/
                       
                           return;
                       }
                   }
              return;
              }
    // cout<<x<<" "<<s<<" "<<n<<" "<<m<<" ";system("pause");
     for (int i=0;i<(1<<m);i++) 
     {
   //      cout<<s+c[i]<<" "<<k<<" "<<s+c[i]+m*(n-x-1)<<" "<<k<<" "<<fin<<" ";system("pause");
         if (s+c[i]<=k && s+c[i]+m*(n-x-1)>=k && fin==0) 
     {
           //        cout<<i<<endl;
                   a[x+1]=(i<<1),go(x+1,s+c[i]);
     }
     }
     }
int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("text.out","w",stdout);
   for (i=1;i<100;i++) c[i]=c[(i&(i-1))]+1;
    int t;
    cin>>t;
    int tt=0;
    while (t--)
    {
          tt++;
          cin>>n>>m>>k;
          printf("Case #%d:\n",tt);
          for (i=0;i<=40;i++){
              for (j=0;j<40;j++) 
              fix[i][j]=fu[i][j]=0;
              a[i]=0;
              }
          
          if (k==m*n-1)
          {
                       for (i=0;i<n;i++)
                       {for (j=0;j<m;j++)
                       if (i+j==0) putchar('c'); else putchar('*');
                       putchar('\n');
                       }
            //           printf("Impossible\n");
                       }
          else {          
          fin=0;
          go(0,0);
          if (fin){
                   for (i=1;i<=n;i++)
                   {   for (j=1;j<=m;j++)
                        if ((a[i]&(1<<(j)))>0) putchar('*'); else
                        {
                                                if (fu[i][j]==27) putchar('c'); else putchar('.');
                                                } 
                       putchar('\n');
                       }
                       
                   } else printf("Impossible\n");
           
          }
                  
          
          }   
    return 0;
}
