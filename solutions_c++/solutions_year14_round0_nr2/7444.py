#include<stdio.h>
int main()
{
         int tc=1,tc1;
         double x,f,c,cook;
         FILE *fp2 = fopen("ans8.txt", "w");
         scanf("%d",&tc1);
         double r=2.0;
         while(tc<=tc1)
         {
                      r=2.0;
                      scanf("%lf",&c);
                    //  printf("%lf",c);
                      scanf("%lf",&f);
                      scanf("%lf",&x);
                      //int s=2;
                      cook=0;
                      double t=0,t1=0,t2=0;
                      while(1)
                      {
                              int k;
                                    if(cook<x)       
                                    {
                                                     t1=((c/r)+ x/(r+f));
                                                     t2=(x/r);
                                                     //printf("%f %f %f",t1,t2,t);
                                                     //scanf("%d",&k);
                                                     if(t1<t2)
                                                     {
                                                           /*   if(cook+(r+f)*t1==x)
                                                              {
                                                                                  printf("Case #%d: %f\n",tc,t);
                                                                                  t+=t1;
                                                                                  break;
                                                              }*/
                                                              t+=(c/r);
                                                              cook=0;
                                                              r=f+r;
                                                              
                                                     }
                                                     else
                                                     {
                                                         t+=t2;
                                                         fprintf(fp2,"Case #%d: %lf\n",tc,t);
                                                        // printf("Case #%d: %lf\n",tc,t);
                                                         break;
                                                     }
                                    }
                                    else
                                        {
                                                     fprintf(fp2,"Case #%d: %lf\n",tc,t);
                                                     //printf("Case #%d: %lf\n",tc,t);
                                                     break;
                                        }
         }
                                                    tc++; 
                                  
         }
         return 0;
}
