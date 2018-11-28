#include<stdio.h>
#include<fstream>
#include<algorithm>
using namespace std;
int main(){
  ofstream result;
  result.open("a.txt");
  int T,N,m1,m2,i,rate,R=0;
  long long int eat1,eat2;
  scanf("%d",&T);
  while(T--){
    scanf("%d",&N);
    int plate[N];
    eat1=0;eat2=0;rate=0;
      scanf("%d",&m1);
      plate[0]=m1;
    for(i=1;i<N;i++){
      scanf("%d",&m2);
      plate[i]=m2;
      if(m2<m1){eat1+=(m1-m2); rate=max(rate,(m1-m2));}
      m1=m2;
    }
    for(i=0;i<(N-1);i++){
     {eat2+=min(rate,plate[i]);}
    }




    
    result<<"case #"<<++R<<": "<<eat1<<" "<<eat2<<endl;
    //printf("%lld    %lld\n   ",eat1,eat2);

  }

  return 0;
}

