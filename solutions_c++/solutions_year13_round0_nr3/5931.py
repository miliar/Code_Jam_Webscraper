#include<iostream>
using namespace std;

bool palin(int num){
     
     int temp1=num;
     int rev=0;
     while(temp1>0){
                    int dig1=temp1%10;
                    rev=rev*10+dig1;
                    temp1=temp1/10;
                    
                    
                    }
                    if(rev==num)
                    return true;
                    return false;
     
     
     }
int main(){
int tot;
int t;
cin>>t;
tot=t;
while(t--){
int a,b;
cin>>a>>b;
int ans[2000]={0};
for(int i=1;i<34;i++){
        
        if( palin(i*i) && palin(i))
        ans[i*i]=1;
        
        }
        int num=0;
for(int i=a;i<=b;i++)
if(ans[i]==1)
num++;

 cout<<"Case #"<<tot-t<<": "<<num<<"\n";
 


}


//system("pause");
}
