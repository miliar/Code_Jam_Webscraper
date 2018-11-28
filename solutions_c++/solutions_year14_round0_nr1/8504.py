#include<iostream>
#include<algorithm>
#define MAX 4
using namespace std;
main()
{
      int a[MAX][MAX], b[MAX][MAX], c[MAX],p, t, i,j, k, c1, c2, cnt, d[100];
      cin>>t;
      for(p=1;p<=t;p++)
      {
      cnt=0;
      
                cin>>c1;
                for(i=0;i<4;i++)
                {                for(j=0;j<4;j++)
                                {
                                                cin>>a[i][j];
                                }
                }
                cin>>c2;
                for(i=0;i<4;i++)
                {
                                for(j=0;j<4;j++)
                                {
                                                cin>>b[i][j];
                                }
                 }
                 for(j=0; j<4; j++)
                 {
                          for(k=0;k<4; k++)
                          {
                                       if(a[c1-1][j]==b[c2-1][k])
                                       {                     
                                                              
                                                             c[cnt++]=a[c1-1][j];
                                       }
                          }
                 }
                 if(cnt==1)
                 {
                           cout<<"Case #"<<p<<": "<<c[0]<<"\n";
                 }
                 if(cnt==0)
                 {
                           cout<<"Case #"<<p<<": "<<"Volunteer cheated!\n";
                 }
                 if(cnt>1)
                 {
                          cout<<"Case #"<<p<<": "<<"Bad magician!\n";
                 }
      }
  
                          
      
}
                                                
                
                
