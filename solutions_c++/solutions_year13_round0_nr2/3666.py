#include<cstdio>
//#include<conio.h>
#include<set>
#include<cstring>
#include<algorithm>
#include<queue>
#include<cmath>
#include<iostream>
#include<vector>
using namespace std;
typedef long long LL;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<pi> vpii;
#define pb push_back
#define nd second
#define st first
#define mp make_pair
#define rep(i,n) for(int i=0;i<n;i++)
#define inf 9999999999
#define MAX 102

int a,b,i,j,n,m,k,l,t;
int sup[MAX][MAX],tab[MAX][MAX];

void init()
{
     rep(i,MAX)
           rep(j,MAX) tab[i][j] = MAX; 
}

int maksWiersz(int kt)
{
    int curr =0;
    for(int i = 0;i<m;i++)
    {
            curr = max(sup[kt][i], curr);
      }   
   return curr;         
}
int maksKol(int kt)
{
    int curr =0;
    for(int i=0;i<n;i++)
    {
            curr = max(sup[i][kt], curr);
    }   
   return curr;         
}

void setKol(int kt, int v)
{
     int curr =0;
    for(int i=0;i<n;i++)
    {
            tab[i][kt] = min(tab[i][kt],v);
    }   
 }
 void setWiersz(int kt, int v)
{
     int curr =0;
    for(int i=0;i<m;i++)
    {
            tab[kt][i] = min(tab[kt][i],v);
    }   
 }

void solve()
{
     int taa;
      
     for(int i=0;i<n;i++)
     {
          taa = maksWiersz(i);
        //  printf("Wiersz %d %d\n",i,taa);
          setWiersz(i,taa);  
     } 
       for(int i=0;i<m;i++)
     {
               //printf("Kol %d %d\n",i,taa);
          taa = maksKol(i);
          setKol(i,taa);  
     } 
            
}     

bool check()
{
     rep(i,n)
     {
        rep(j,m)
        {
           if(tab[i][j]!=sup[i][j])
                                   return false;
        }      
     }
     return true;
}
//n - ile wierszy
int main()
{
         scanf("%d",&t);
          
         rep(ii,t)
         {
         init();
            scanf("%d %d",&n,&m);
            rep(i,n)
            {
               rep(j,m)
               {
                      scanf("%d",&k);
                      sup[i][j]=k; 
                }        
            }
            
        
            solve();


           if(check() == false) printf("Case #%d: NO\n",ii+1);
           else printf("Case #%d: YES\n",ii+1);       
         } 
      
         
          
        //  getch();
          return 0;
}
