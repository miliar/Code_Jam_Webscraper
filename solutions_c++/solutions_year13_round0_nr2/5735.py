#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<cstring>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<fstream>
#include<stack>
#include<queue>
#include<sstream>
using namespace std;
int a[128][128];
   int n,m;
bool Check(int i,int j)
{
int p=0;
    for(int k=0;k<m;k++)
        if(a[i][k]!=a[i][j]){p=1; break;}
    if(!p)return false;
    for(int k=0;k<n;k++)
        if(a[k][j]!=a[i][j])return true;
    return false;

}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
   int tc;

   scanf("%d",&tc);
   for(int T=1;T<=tc;T++)
   {
       scanf("%d%d",&n,&m);
       for(int i=0;i<n;i++)
       {
           for(int j=0;j<m;j++)
               scanf("%d",&a[i][j]);
       }
       int sol=0;
       for(int i=0;i<n;i++){
           for(int j=0;j<m;j++)
               if(a[i][j]==1)
                   if(Check(i,j)){sol=1; cout<<"Case #"<<T<<": NO"<<endl; break;}
        if(sol)break;
       }
       if(!sol)
           cout<<"Case #"<<T<<": YES"<<endl;


   }




    return 0;
}