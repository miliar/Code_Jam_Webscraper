#include<iostream>
#include<vector>
using namespace std;

int main(void){
  int T;
  cin >> T;

  unsigned int A;
  unsigned int B;
  unsigned int K;
  unsigned int tmp;
  int count;
  vector<unsigned int> xVect;
  bool flag;
  for(int I=1;I<=T;I++){
    xVect.clear();
    cin >> A;
    cin >> B;
    cin >> K;
    count = 0;
    for(unsigned int a=0;a<A;a++){
      for(unsigned int b=0;b<B;b++){
	flag = true;
	xVect.push_back(a&b);	
      }
    }

    for(int i=0;i<xVect.size();i++){
      if(xVect[i] < K)count++;
    }
    
    cout << "Case #" << I << ": " << count << endl;
  }
  return 0;
}
