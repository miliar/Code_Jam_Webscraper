#include<iostream>
using namespace std;
main()
{
      int t,i,flag,count;
      double C,X,F,ti,t3,t1,t2;
      cin>>t;
      for(i=1;i<=t;i++)
      {
                       flag=0;
                       count=0;
                       ti=2.0;
                       t3=0.0;
                       t1=0.0;
                       t2=0.0;
                       cin>>C>>F>>X;
                       if(C>=X)
                       {
                               t3=X/ti;
                               flag=1;
                       }
                       while(flag==0)
                       {
                                     t1=X/ti;
                                     t2=(C/ti)+(X/(ti+F));
                                     if(t2>=t1)
                                     {
                                               flag=1;
                                               t3+=X/ti;
                                               break;
                                     }
                                     else
                                     {
                                         t3+=C/ti;
                                         ti+=F;
                                     }
                    }        
                    printf("Case #%d: %.7lf\n",i,t3);
      }
     
}
