
#include <iostream>
#include <stdio.h>
using namespace std;

#define GCJ2
#ifdef GCJ2



double GetMinTime(double C,double F, double X)
{
       int n = 0;
       double sumt = 0;
       double T = 0;
       while(1)
       {       
              T = C/(2+n*F);
              if(sumt + T + X/(2+(n+1)*F) >=  sumt + X/(2+n*F))               
              {
                      return sumt + X/(2+n*F);
              } 
              sumt += T;                             
              n++;
       }
       return 0;
}

int main()
{
    int n;
    cin >> n;
    double C,F,X;
    for(int i = 0;i< n;++i)
    {
              cin>>C>>F>>X;
              printf("Case #%d: %.7f\n",i+1,GetMinTime(C,F,X));
    };
    
    return 0;
}


#endif


#ifdef GCJ1
int findSameNum(int a[4],int b[4],int & r)
{
    int count = 0;
    for(int i = 0;i < 4;++i)
    {
        for(int j = 0;j < 4;++j)
        {
              if(a[i] == b[j])
              {
                      count++;
                      r = a[i];
                      break;        
              }        
        }        
    
    }    
    return count;    
}

int main()
{
    int n,m;
    int a[4];
    int b[4];
    int x;
    cin>>n;
    int iNth = 0;
    while(iNth < n)
    {
              for(int k = 0;k<2;++k)
              {
                  cin>>m;         
                  for(int i = 0;i < 4;++i)
                  {
                          for(int j = 0;j < 4;++j)
                          {
                              cin>>x;
                              if(i == m-1 && 0 == k)
                              {
                                   a[j] = x;    
                              }
                              else if(i == m-1 && 1 == k)                                        
                              {
                                   b[j] = x;
                              }
                          }
                  }                      
              }
              int  r = 0;
              cout<<"Case #"<<iNth+1<<": ";
              switch(findSameNum(a,b,r))
              {
               case 0:
                      cout<<"Volunteer cheated!"<<endl;
                      break;
               case 1:
                      cout<<r<<endl;         
                      break;
               default:
                      cout<<"Bad magician!"<<endl;
              }
              iNth++;
    }    
    return 0;   
}
#endif

