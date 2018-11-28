#include <iostream>
#include <fstream>
#include <set>

using namespace std;

unsigned long long foo(ifstream& fin,ofstream& fout){
  unsigned long long N = 0;
  fin>>N;

  if(N == 0) {
    fout<<"INSOMNIA";
    return -1;
  }

  unsigned long long digits[] ={1,2,3,4,5,6,7,8,9,0};
  set<unsigned long long> goal(digits, digits+10);

  set<unsigned long long> myset;
  int ans = 1;

  while(1) {
    unsigned long long m = N * ans;
    if(N*(ans-1) > m) {
      fout<<"INSOMNIA";
      return -1;
    }

    while(m) {
      myset.insert(m%10);
      m/=10;
    }

    if(myset == goal) {
      fout<<N*ans;
      return N*ans;
    }
    ans++;
  }
}

int main(){
  ofstream fout;
  ifstream fin;
  fin.open("A-large.in");
  fout.open("Ab.out");
  
  cout<<"open success\n";
  
  int T = 0;
  fin>>T;
  
  cout<<"input size success\n";
  
  for(int i=0;i<T;i++){
    fout<<"Case #"<<i+1<<": ";
    cout<<foo(fin,fout)<<endl;
    fout<<endl;
  }

}