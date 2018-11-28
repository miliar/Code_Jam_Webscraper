#include<iostream>
using namespace std;
main()
{
      int t, i, j, k, flag, cnt;
      double c, x, f, ti1, ti2, tt, temp1, temp2, tem ;
      cin>>t;
      for(i=1;i<=t;i++)
      {
                       cnt=0;
                       flag=0;
                       ti1=2.0;
                       tt=0.0;
                       temp1=0.0;
                       temp2=0.0;
                       
                       cin>>c>>f>>x;
                        if(c>=x)
                        {
                                         tt=x/ti1;
                                         flag=1;
                        }
                    while(flag==0)
                    {
                                      
                                      
                                          temp1=x/ti1;
                                          temp2=(c/ti1)+(x/(ti1+f));
                                          if(temp2>=temp1)
                                          {
                                                         flag=1;
                                                         tt+=x/ti1;
                                                         break;
                                          }
                                          else
                                          {
                                              tt+=c/ti1;
                                              ti1+=f;
                                          }
                                     
                                  
                    }        
                    printf("Case #%d: %.7lf\n", i, tt);
      }
     
}
