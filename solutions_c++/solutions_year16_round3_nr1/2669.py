#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <utility>
using namespace std;

int main(int argc, char** argv){
  ofstream outfile("out.txt");
  ifstream inp(argv[1]);
  string line;
  int T;
  inp>>T;
  getline(inp,line);
  for(int t=1;t<=T;t++){
    int N;
    inp>>N;
    getline(inp,line);
    pair<int,int> A[N];
    for(int i=0;i<N;i++){
      inp>>A[i].first;
      A[i].second = 65+i;
    }
    int n = N;
    outfile<<"Case #"<<t<<": ";
    while(n){
      sort(A,A+N);
      //for(int i=0;i<N;i++){cout<<A[i].first<<A[i].second<<" ";}cout<<endl;
      if(n==1){
        if(A[N-1].first>1){
          A[N-1].first-=2;
          outfile<<char(A[N-1].second)<<char(A[N-1].second)<<" ";
          if(A[N-1].first==0)n--;
        }
        else{
          A[N-1].first-=1;
          outfile<<char(A[N-1].second)<<" ";
          if(A[N-1].first==0)n--;
        }
      }
      else{
        int x=0; int y=0;
        if(A[N-1].first!=0){A[N-1].first-=1;x=1;}
        if(A[N-2].first!=0){A[N-2].first-=1;y=1;}
        if(A[N-1].first==0 && x)n--;
        if(A[N-2].first==0 && y)n--;
        if(n==1){
          A[N-2].first=1;n++;y=0;
        }
        if(x && y)outfile<<char(A[N-1].second)<<char(A[N-2].second)<<" ";
        else if(x)outfile<<char(A[N-1].second)<<" ";
        else if(y)outfile<<char(A[N-2].second)<<" ";
        //cout<<n<<endl;
      }
    }
    outfile<<endl;
  }
  return 0;
}
