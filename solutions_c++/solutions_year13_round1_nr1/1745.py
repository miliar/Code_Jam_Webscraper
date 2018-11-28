#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<fstream>
using namespace std;


int main(){
  ifstream infile("input.in");
  ofstream outfile("output.out");
  long long T, r, t;
  infile>>T; 
  for(int i=0; i<T; i++){
    infile>>r>>t;
    long long count=0;
    long long j=0;
    while(t>=0){
      t=t-(2*r+4*j+1);
      if(t>=0) count++;
      j++;
    }
    outfile<<"Case #"<<i+1<<": "<<((count==0)? 1 : count)<<endl;
  }
}
