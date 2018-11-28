#include<stdio.h>
#include<fstream>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
int main(){
  ofstream result;
  result.open("countingsheep.txt");
  int T,M;
  long long int N,temp1,temp2;
  int digits,isFinite;
  scanf("%d",&T);
  M=0;
  while(T--){
   digits=0;temp1=temp2=0;isFinite=0;
   scanf("%lld",&N);
   if(N==0){isFinite=1;}
   else{
    while(digits != 1023){
 	temp1+=N;
	temp2=temp1;
        while(temp2){
		digits = digits|(1<<(temp2%10));
		temp2/=10;
        }
    }
   }
   //result<<"N: "<<N<<"   isFinite: "<<isFinite<<endl;
   if(isFinite==1){   result<<"Case #"<<++M<<": "<<"INSOMNIA"<<"\n";}
   else{result<<"Case #"<<++M<<": "<<temp1<<"\n";}
  }
}
