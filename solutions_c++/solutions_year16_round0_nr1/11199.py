#include<bits/stdc++.h>

using namespace std;


int main(){

  int numbers[10];
  int count,n,number,tem,tem1;
  bool sw;
  for(int i=0;i<10;i++){
    numbers[i]=0;
  }
  cin>>n;
  for(int k=1;k<=n;k++){
      cin>>number;
      count=0;
      sw=false;
      tem=number;
      for (int i=2;true;i++){
          do{
            if(numbers[tem%10]!=k){
              numbers[tem%10]=k;
              count++;
            }
            tem=tem/10;
          }while (tem!=0);
          if(count==10){
            sw=true;
            break;
          }
          tem1=i*number;
            if(tem1==number){
            break;
          }
          tem=tem1;
      }
      cout<<"Case #"<<k<<": ";
      if(sw){
        cout<<tem1<<endl;
      }else{
        cout<<"INSOMNIA"<<endl;
      }
  }

  return 0;
}
