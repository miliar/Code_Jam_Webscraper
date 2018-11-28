#include <iostream>
#include <vector>

using namespace std;

unsigned int T,A,B,K,r,i,j;
int main()
{
  cin >> T;
  for(int t=1; t<=T; t++){
    cin >> A >> B >> K;
    r=0;
    for(i=0;i<A;i++){
      for(j=0; j<B; j++){
	//	cout << i << " " << j << " " << (i & j) << endl;
	if((i & j) < K) r++;
      }
    }
  
    cout << "Case #" << t << ": " << r << endl;
  }
  return 0;
}
