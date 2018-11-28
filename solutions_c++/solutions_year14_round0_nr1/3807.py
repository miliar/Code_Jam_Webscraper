#include<iostream>
#include<stdio.h>
#define rep(i,a,b) for(i=a;i<=b;i++)
using namespace std;



int main()
{
    
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,m,x,y,a[4][4],b[4][4],val,ctr,i,j;
    scanf("%d",&t);
    rep(m,1,t)
    {
    //cin>>x;
    scanf("%d",&x);
    
    rep(i,0,3)
    rep(j,0,3)
    //cin>>a[i][j];
    scanf("%d",&a[i][j]);
    
    //cin>>y;
    scanf("%d",&y);
    
    
    rep(i,0,3)
    rep(j,0,3)
    //cin>>b[i][j];
    scanf("%d",&b[i][j]);
    
    
    ctr=0;
    rep(i,0,3)
    {
              rep(j,0,3)
              {
               if(a[x-1][i]==b[y-1][j])
               {
               ctr++;
               val=a[x-1][i];
               }
              }
    }
    
    if(ctr==1)
    {
    printf("Case #%d: %d\n",m,val);
    }
    
    else if(ctr>1)
    {
    printf("Case #%d: Bad magician!\n",m);     
    }
    
    
    else 
    {
     printf("Case #%d: Volunteer cheated!\n",m);
    }
    
    }
    
    
    return 0;
    
}
