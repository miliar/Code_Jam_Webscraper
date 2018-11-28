#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

void update_dig(int** dig,int N){
  while(N>0){
    int r=N%10;
    dig[0][r]=1;
    N=N/10;
  }
}

int main(int argc, char** argv){
  ofstream outfile("out.txt");
  ifstream inp(argv[1]);
  string line;
  int T;
  inp>>T;
  getline(inp,line);
  for(int t=1;t<=T;t++){
    int dig[10]={0};
    int N;
    inp>>N;
    getline(inp,line);
    if(N!=0){
      int res=N;
      int i=1;
      int done = 0;
      while(done==0){
        while(res>0){
          int r= res%10;
          dig[r]=1;
          res/=10;
        }
        done=1;
        for(int j=0;j<=9;j++)if(dig[j]==0){done=0;break;}
        if(done==1)break;
        i++;
        //cout<<i<<endl;
        res = N*i;
      }
      res = N*i;
      outfile<<"Case #"<<t<<": "<<res<<endl;
    }
    else outfile<<"Case #"<<t<<": INSOMNIA"<<endl;
  }

}
