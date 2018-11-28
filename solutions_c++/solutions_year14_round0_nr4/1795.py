#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    

    freopen("D-large.in","r",stdin);
    freopen("outer10.txt","w",stdout);
     int cases;
    
    scanf("%d",&cases);
    for(int c =1;c<=cases;c++)
    {
          
          int num;
          scanf("%d",&num);
          double  a[num];
          double  b[num];
          double b2[num];
          for(int i=0;i<num;i++)
          {
                  scanf("%lf",&a[i]);
                  
          }
          for(int i=0;i<num;i++)
          {
                  scanf("%lf",&b[i]);
                 
          }
          sort(a,a + num);
          sort(b,b +  num);
          for(int i=0;i<num;i++)
          {
           //       scanf("%lf",&b[i]);
            b2[i] = b[i];     
          }
          int ans2 = 0;
          for(int i=0;i<num;i++)
          {
                  int temp = 0;
                  for(int j=0;j<num;j++)
                  {
                          if(b[j]>a[i])
                          {
                                       temp  =1;
                                       b[j] = 0;
                                       break;
                          }
                  }
                  if(temp==0)
                  ans2++;
          }
          int ans1 =0;
          int start  = -1;
          //cout<<ans2<<endl;
          for(int i = num-1;i>=0;i--)
          {
                  int done =0;
                  for(int  l = num-1;l>=0;l--)
                  {
                           //cout<<a[i]<<" "<<b[l]<<endl;
                           if(a[i]>b2[l]&&b2[l]>0)
                           {
                                                ans1++;
                                                done  =1;
                                                b2[l] = -1;
                                                break;
                           }
                  }
                  
                  if(done==0)
                  {
                         start  =  i;    
                         break;  
                  }
            // cout<<"yes"<<endl;     
          }
                  
                  
          //cout<<ans1<<endl;
          if(start>-1)
          {
          for(int i=0;i<start;i++)
          {
                  int got =0;
                  for(int j=num-1;j>=0;j--)
                  {
                       if(b2[j]>a[i]&&b2[j]>0)
                        {
                                      got =1;
                                      b2[j] = -1;
                                      break;
                        }
                       
                        
                        
                        
                  }
                  if(got==0)
                  {
                            ans1++;
                            
                  }
                  
           }
          }
          
          printf("Case #%d: %d %d\n",c,ans1,ans2);//<<endl;
          }
          return 0;
}
