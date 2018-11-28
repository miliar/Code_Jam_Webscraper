#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmpBlks(double blk1, double blk2){return blk1>blk2;}
void readBlocks(int N, vector<double>& blks);
int war(vector<double> nBlks, vector<double> kBlks);
int decWar(vector<double> nBlks, vector<double> kBlks);

int main(int argc, char** argv){
  int T;

  cin>>T;
  for(int i=0; i<T; i++){
    double N;
    vector<double> nBlks, kBlks;
    
    cin>>N;

    readBlocks(N,nBlks);
    readBlocks(N,kBlks);

    sort(nBlks.begin(),nBlks.end(),cmpBlks);  
    sort(kBlks.begin(),kBlks.end(),cmpBlks);  

    cout<<"Case #"<<i+1<<": "<<decWar(nBlks,kBlks)<<" "<<war(nBlks,kBlks)<<"\n"; 
  }


  return 0;
}

void readBlocks(int N, vector<double>& blks){
  double blk;
  for(int i=0; i<N; i++){
    cin>>blk;
    blks.push_back(blk);
  }
}


int war(vector<double> nBlks, vector<double> kBlks){
  int nScore=0;
  
  while(nBlks.size()>0){
    if(nBlks[0]>kBlks[0]){
      nScore++;
      kBlks.erase(kBlks.begin()+kBlks.size()-1);
    }
    else
      kBlks.erase(kBlks.begin());

    nBlks.erase(nBlks.begin());
  }

  return nScore;
}

int decWar(vector<double> nBlks, vector<double> kBlks){
  int nScore=0;

  while(nBlks.size()>0){
    if(nBlks[0]>kBlks[0]){
      nScore++;
      kBlks.erase(kBlks.begin());
      nBlks.erase(nBlks.begin());
    }
    else if(nBlks[nBlks.size()-1]<kBlks[0]){
      kBlks.erase(kBlks.begin());
      nBlks.erase(nBlks.begin()+nBlks.size()-1);
    }
    else{
      nScore++;
      kBlks.erase(kBlks.begin()+kBlks.size()-1);
      nBlks.erase(nBlks.begin()+nBlks.size()-1);
    }
  }

  return nScore;
}
