#include <iostream>

using namespace std;

int main()
{
    int t,n,m,z=0,in[10][10],flag,i,j,k;
    cin>>t;
    while(z++<t)
    {
           cin>>n>>m;
           for(i=0;i<n;i++)
           for(j=0;j<m;j++)
           cin>>in[i][j];
           
           for(i=0;i<n;i++)
           {
               for(j=0;j<m;j++)
               {
                           flag = 0;
                           for(k=0;k<n;k++)
                           if(in[i][j] < in[k][j])
                           {
                                       flag = 1;
                                       break;
                           }
                           if(flag!=0)
                           for(k = 0;k<m;k++)
                           if(in[i][j] < in[i][k])
                           {
                                       flag =2;
                                       break;
                           }
                           if(flag==2)
                           break;
               }
               if(flag == 2)
               break;
           }    
           
           if(flag == 2)
           cout<<"Case #"<<z<<": NO\n";  
           else
           cout<<"Case #"<<z<<": YES\n";  
    }
   // system("PAUSE");
    return 0;
}
