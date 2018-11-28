#include<iostream>
#include<cmath>
#include<cstring>

using namespace std;

main()
{
      int t,n,m,i;
      int num,ctr,cntr=1;
      char str[15],rev[15];
      freopen("inputsqr.txt","r",stdin);
      freopen("outputsqr.txt","w",stdout);
      scanf("%d",&t);
      while(t--)
      {
          ctr=0;
          scanf("%d %d",&n,&m);
          for(i=n;i<=m;i++)
          {
               sprintf(str, "%d", i);
               sprintf(rev, "%d", i);
               strrev(rev);
               //cout<<str<<" "<<rev<<endl;
               if(strcmp(str,rev)==0)
               {
                  num=sqrt(i);
                  if((num*num)==i)
                  {
                       sprintf(str, "%d", num);
                       sprintf(rev, "%d", num);
                       strrev(rev);
                       if(strcmp(str,rev)==0)
                       {
                         //cout<<str<<" "<<rev<<endl;
                          ctr++;
                       }                                    
                  }                                  
               
               }  
                       
          }
          printf("Case #%d: %d\n",cntr,ctr);
          cntr++;
                         
      }
      return 0;
}
