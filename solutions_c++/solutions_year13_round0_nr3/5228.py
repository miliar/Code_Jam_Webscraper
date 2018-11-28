#include <iostream>
#include <math.h>
using namespace std;

int main (){
    int cases;
    cin>>cases;
    unsigned long long result[cases];
    for (int i = 0; i<cases;i++)
    result[i]=0;
    for (int i = 0; i<cases;i++){
     unsigned long long a,b;   
     cin>>a>>b;
     for(int k = a;k<=b;k++){
             int c = sqrt(k);
             if((c*c)==k){
                  int t=k,rev=0,m;
                  while(t>0)
                       {
                       m=t%10;
                       rev=rev*10+m;
                       t=t/10;        
                       }
                if(rev==k){
                   int p=c,rev2=0;
                    while(p>0)
                       {
              m=p%10;
rev2=rev2*10+m;
p=p/10;        
                          }
                          if(rev2==c)
                          ++result[i];
                        
                        }
             
             }   
        }
    
}
for(int i=0;i<cases;i++)
cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
  return 0;  }
