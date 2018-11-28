#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin >> T;
	for(int i=1;i<=T;i++){
		int A,B,K;
		cin >> A >> B >> K;
		int count = 0;
    for(int j=0;j<A;j++){
      for(int k=0;k<B;k++){
        if((j & k) <K)
          count += 1;
      }
    }
    cout << "Case #" << i << ": " << count << endl;
	}
}
