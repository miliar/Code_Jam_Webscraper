#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;

bool isPali(int num){
   int n=num,m=0;
   while(n>0){
      m *= 10;
      m += n%10;
      n /= 10;
    }
   if(m==num)
     return true;
   else
     return false;
}


int main(){
    int T;
    cin>>T;
    int t1=T;
    int a,b;
    float r;
    int count=0;
    while(T--){
        count=0;
        cin>>a>>b;
        for(int i=a;i<=b;i++){
                if((i/10==0)&&((i==1)||(i==4)||(i==9))){
                    count++;
                    continue;
                }
                if(isPali(i)){
                   r = sqrt(i);
                   if((r-(int)r)==0)
                      if(isPali((int)r))
                          count++;    
                }
                //if(isPali(i)&&isPali(sqrt(
                
        }
        cout<<"Case #"<<(t1-T)<<": "<<count<<endl;
    }    
    return 0;
}
