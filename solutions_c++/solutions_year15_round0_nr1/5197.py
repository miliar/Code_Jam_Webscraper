#include<stdio.h>
#include<fstream>
using namespace std;
int main(){
  ofstream result;
  result.open("standingovation.txt");
  int T,N=0,Smax,i,peopleStanding,peopleNeeded,currentIndexPeople;
  char ch;
  scanf("%d",&T);
  while(T--){
    peopleStanding=0;
    peopleNeeded=0;
    scanf("%d",&Smax);scanf("%c",&ch);
    for(i=0;i<=Smax;i++){
      scanf("%c",&ch); currentIndexPeople=(int)ch-48;
      //printf("---CIP: %d  \n",currentIndexPeople);
      if(i>peopleStanding){
        peopleNeeded+=(i-peopleStanding);
        peopleStanding+=(i-peopleStanding);
      }
      peopleStanding+=currentIndexPeople;
    }
    result<<"case #"<<++N<<": "<<peopleNeeded<<"\n";
    //printf("%d\n",peopleNeeded);

  }

  return 0;
}

