#include<iostream>

int main(){
  int n;
  std::cin >> n;
  for(int prob=1;prob<=n;prob++){
    int a,as[4],tmp[4];
    std::cin >> a;
    for(int i=1;i<=4;i++){
      for(int j=0;j<4;j++)std::cin >> tmp[j];
      if(a==i){
        for(int j=0;j<4;j++){
          as[j]=tmp[j];
        }
      }
    }
    int b,bs[4];
    std::cin >> b;
    for(int i=1;i<=4;i++){
      for(int j=0;j<4;j++)std::cin >> tmp[j];
      if(b==i){
        for(int j=0;j<4;j++){
          bs[j]=tmp[j];
        }
      }
    }
    int d=-1;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        if(as[i]==bs[j]){
          if(d==-1)d=as[i];
          else d=-2;
        }
      }
    }      
    std::cout << "Case #" << prob << ": ";
    if(d==-1)std::cout << "Volunteer cheated!";
    else if(d==-2)std::cout << "Bad magician!";
    else std::cout << d;
    std::cout << std::endl;
  }
  return 0;
}