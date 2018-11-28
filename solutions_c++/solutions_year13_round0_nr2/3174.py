#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>


using namespace std;

int main(int argc, char *argv []) {
  if(argc<3) return 1;
  ifstream input;
  input.open(argv[1]);
  ofstream output;
  output.open(argv[2]);
  int tcc;
  string nummern;
  getline(input,nummern);
  stringstream(nummern)>>tcc;
  for(int testnr=1;testnr<=tcc;testnr++) {
    getline(input,nummern);
    int N,M;
    stringstream(nummern)>>N>>M;
    int *dish=new int[N*M];
    for(int i=0;i<N;i++) {
      getline(input,nummern);
      stringstream ss(nummern);
      for(int j=0;j<M;j++)
        ss>>dish[M*i+j];
    }
    int *mh=new int[M+N];
    for(int i=0;i<M+N;i++)
      mh[i]=0;
    for(int i=0;i<N;i++)
      for(int j=0;j<M;j++) {
        if(dish[M*i+j]>mh[i]) {
          mh[i]=dish[M*i+j];
        }
        if(dish[M*i+j]>mh[j+N])
          mh[j+N]=dish[M*i+j];
      }
    bool ps=true;
    for(int i=0;i<N&&ps;i++)
      for(int j=0;j<M&&ps;j++)
        if(dish[i*M+j]<mh[i]&&dish[i*M+j]<mh[j+N])
          ps=false;
    output<<"Case #"<<testnr<<": "<<(ps?"YES":"NO")<<endl;
    delete [] dish;
    delete [] mh;
  }
  input.close();
  output.close();
  cout<<"\nFinished\n";
  return 0;
}
