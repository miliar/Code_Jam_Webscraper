#include<iostream>

using namespace std;
int main()
 {
  int T[100],v,d=0,z=0;
  cin>>v;
  long int N;int s,t;
 int c[10];
        
   for(int p=1;p<=v;p++)
    {
      cin>>T[p];
    }
   for(int a=1;a<=v;a++)
    {
 for(int j=0;j<10;j++)
         c[j]=0;
      N=T[a];
      for(int i=1;i<100;i++)
       {
         s=i*N;
         t=s;
        
         int r;
            while(t>0)
             {
               r=t%10;
               for(int k=0;k<10;k++)
                 {
                   if(r==k)
                     c[k] ++;
                 }
               t=t/10;
             }
        
     
     if(c[0]>0 && c[1]>0 && c[2]>0 && c[3]>0 && c[4]>0 && c[5]>0 && c[6]>0 && c[7]>0 && c[8]>0 && c[9]>0 )            
            {  cout<<"Case #"<<a<<": "<<s<<endl;
                   z=1;
                  break; }
                         
      }
            if(z!=1)
       cout<<"Case #"<<a<<": INSOMNIA"<<endl;
    }
          
      return 0;
  }
 
