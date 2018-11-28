#include <iostream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;
int main() {

  int T;
  cin >> T;

  for (int I=0;I<T;I++) {
    int smax;
    string data;
    cin >> smax;
    cin >> data;
    assert(data.length()==smax+1);
    
    vector<int> C;
    vector<int> total;
    C.resize(smax+1);
    total.resize(smax+1);
    // C[i] = maximum number of people needed to add to
    // have everyone with shyness <=i to stand.
    // total[i] = total number of people <=i;
    for (int i=0;i<data.length();i++) {
      if (i==0) {
	total[i]=data[0]-'0';
	C[i] = 0;
      } else {
	total[i] = total[i-1]+(data[i]-'0');
	if ((total[i-1]+C[i-1])<i) {
	  C[i]=i-total[i-1];
	} else {
	  C[i]=C[i-1];
	}
      }
    }
    cout << "Case #"<<I+1<<": " << C[data.length()-1] << endl;
  }
}
