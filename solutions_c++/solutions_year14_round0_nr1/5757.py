#include <iostream>
//#include <stdlib>
using namespace std;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int a[4][4],t,n,i,j,l,ans,aa,m,b,k;
    cin>>t;
    for(l=0;l<t;l++)
    {
       // cout<<'n';
        cin>>n ;
        for(i=0;i<4;i++)
        {
                for(j=0;j<4;j++)
                 {
                        cin>>a[i][j];              
                 }    
        }
        ans=0;
       // cout<<'m';
        cin>>m;
        for(i=0;i<4;i++)
        {
            if (i==m-1)
            for(j=0;j<4;j++)
              {
                   cin>>b;   
                   for (k=0;k<4;k++)
                   {
                      if (a[n-1][k]==b) 
                      {
                          ans++;
                        //  cout<<ans<<endl;
                          aa=b;
                      }           
                   } 
              }
            else 
            for(j=0;j<4;j++)
            {
                   cin>>b;    
            }    
        } 
        if (ans==1) cout<<"Case #"<<l+1<<": "<<aa<<endl;
        if (ans>1) cout<<"Case #"<<l+1<<": Bad magician!"<<endl;
        if (ans==0)cout<<"Case #"<<l+1<<": Volunteer cheated!"<<endl;  
    }    
   // cin>>n;
}
