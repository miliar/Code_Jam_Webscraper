#include<stdio.h>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
  ofstream result;
  vector<int> diners;
  vector<int> time;
  result.open("infinitehouseofpancakes1.txt");
  int T,D,d,N=0,i,n,timeCount,temp;
  scanf("%d",&T);
  while(T--){
    timeCount=0;
    diners.clear();
    time.clear();

    scanf("%d",&D);
    for(i=0;i<D;i++){
      scanf("%d",&d); diners.push_back(d);
    }
    sort(diners.begin(),diners.end());
    //for(i=0;i<diners.size();i++){
    //  printf("%d ",diners[i]);
    //}


    time.push_back(diners[diners.size()-1]);
    while(diners[diners.size()-1] > 3){
      timeCount++;
      if(diners[diners.size()-1]==9){
        if(diners.size()==1 || diners[diners.size()-2] <= 3 ||diners[diners.size()-2] == 6 ){
          temp=3;//result<<"+";
        }else{temp=diners[diners.size()-1]/2;}//result<<"*";}
      }else{temp=diners[diners.size()-1]/2;}//result<<"/";}
      diners[diners.size()-1] -= temp;
      diners.push_back(temp);
      sort(diners.begin(),diners.end());
      time.push_back(diners[diners.size()-1]+timeCount);
    }

      sort(time.begin(),time.end());
    

    result<<"Case #"<<++N<<": "<<time[0]<<"\n";
    //printf("%d\n",time[0]);

  }

  return 0;
}

