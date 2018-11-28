#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
  int T;
  long A,B,number;
  long temp,i,j;
  vector<int> a;
  a.push_back(1); 
  a.push_back(4); 
  a.push_back(9); 
  a.push_back(121); 
  a.push_back(484); 
  cin >> T;
  for(i=0;i<T;i++){
    cin >> A;
    cin >> B;
    number=0;
    for(j=0;j<5;j++){
	if(a[j] > A-1 && a[j] <B+1){
		number = number+1;
	}		
    }
    cout << "Case #" << i+1 << ": " << number << endl;
  }
  return 0;
}
