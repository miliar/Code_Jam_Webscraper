#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

  ifstream f("input.txt");
  ofstream of("output.txt");

  long M;long N;
  long T[104][104];

  void sswap(long &a,long &b){

  long c=a;a=b;b=c;

  }

  void Init(){
  f>>N>>M;

    for(long i=0;i<=103;++i)
    for(long j=0;j<=103;++j)
    {T[i][j]=1000;}

    for(long i=1;i<=N;++i)
    for(long j=1;j<=M;++j)
    {f>>T[i][j];}

  }

  string Che(){

  bool p;


  while(M*N){
      long min=1000;long r;long c;
  for(long i=1;i<=N;++i)
  for(long j=1;j<=M;++j)
      if(T[i][j]<min){min=T[i][j];r=i;c=j;}

  //of<<min<<"\n";
  //of<<r<<" "<<c<<"\n";
  //of<<N<<" "<<M<<"\n";
  p=0;

 for(long i=1;i<=N;++i)if(T[i][c]!=min)p=1;
 // of<<p<<"\n";

 // for(long i=1;i<=N;++i,of<<"\n")
 // for(long j=1;j<=M;++j)of<<T[i][j];


  //of<<"\n";
  if(p==0)for(long i=1;i<=N;++i)sswap(T[i][c],T[i][M]);
  if(p==1)for(long j=1;j<=M;++j)sswap(T[r][j],T[N][j]);

  //for(long i=1;i<=N;++i,of<<"\n")
  //for(long j=1;j<=M;++j)of<<T[i][j];

  if (p==0)for(long i=1;i<=N;++i)if(T[i][M]!=min)return "NO";
  if (p==1)for(long j=1;j<=M;++j)if(T[N][j]!=min)return "NO";
  if(p==0)M--;
  if(p==1)N--;


  }
  return "YES";
  }





int main(){

  long T;

  f>>T;

  for(long i=1;i<=T;++i){
  Init();
  of<<"Case #"<<i<<": "<<Che()<<"\n";
  }


return 0;
}
