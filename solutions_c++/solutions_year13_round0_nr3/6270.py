#include <iostream>
#include <cmath>
#include <string>
using namespace std;

unsigned long long count_fs_num(unsigned long long A, unsigned long long B){
  unsigned long long low, high;
  low = sqrt(A) - 1;
  high = sqrt(B) + 2;
  unsigned long long count=0;
  for(auto i=low; i< high; i++){
    unsigned long long m = i*i;
    if(m>B||m<A)
      continue;
    string s = to_string(m);
    string sqrs = to_string(i);
    if(s==string(s.rbegin(),s.rend()) &&
       sqrs == string(sqrs.rbegin(), sqrs.rend())){
	count++;
    }
  }
  return count;
}


int main(int argc, char** argv){
  int T;
  cin>>T;
  for(auto t=0; t<T; t++){
    unsigned long long int A, B;
    cin>>A>>B;
    cout<<"Case #"<<t+1<<": "<<count_fs_num(A,B)<<endl;
  }
  return 0;
}
