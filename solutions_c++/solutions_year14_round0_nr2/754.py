#include<iostream>
#include<cstdio>
#include<iomanip>
using namespace std;

int main(){
  int tc;
  scanf("%d",&tc);
  for(int tcc=1;tcc<=tc;tcc++){
    printf("Case #%d: ",tcc);
    double c,f,x;
    cin>>c>>f>>x;
    double rate=2.0;
    double prev,now,prevAddval=0;
    prev=x/rate;
    int farms=1;
    while(1){
      now=prevAddval+(x/rate);
      prevAddval+=c/rate;
      //cout<<now<<"  "<<farms<<endl;
      //cout<<rate<<"    --     "<<prevAddval<<endl;
      rate+=f;
      if(now>prev)break;
      prev=now;
      farms++;
    }
    cout<<std::fixed<<std::setprecision(7)<<min(prev,now)<<endl;
  }
  return 0;
}
