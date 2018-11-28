#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  ifstream myfile("B-small-attempt1.in");
  int testcases;
  myfile >> testcases;
  int b;
  int n ;
  int casenum = 1;
  while(myfile >> b >> n) {
    vector<int>bb(b,0);
    vector<int>temp(b,0);
    vector<int>x(b,0);
    for (int i = 0; i< b; i++){
      myfile>>bb[i];
      temp[i] = bb[i];
      x[i] = i;
    }
    if (n <= b) {
      cout <<"Case #"<<casenum <<": "<<n<<endl;
      casenum++;
      continue;
    }
    int sm;
    for (int i = b; i < n; i++){
      sm = 0;
      for (int j = 1; j < b; j++)
      {
        if(temp[j]<temp[sm])
          sm = j;
      }
      int value = temp[sm];
      for (int j = 0; j < b; j++)
        {
          temp[j] -= value;
        }
      bool zero = true;
      for (int j = 0; j < b;j++)
        if (temp[j]!=0){
          zero = false;
          break;
        }
      if (zero) {
        sm = x[(n-1)%x.size()];
        break;
      }
      temp[sm] += bb[sm];
      x.push_back(sm);
    }
    cout << "Case #"<<casenum<<": "<<sm+1<<endl;
    casenum++;
  }
  return 0;
}
