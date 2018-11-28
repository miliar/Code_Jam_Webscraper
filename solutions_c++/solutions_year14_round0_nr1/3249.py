#include <vector>
#include <list>
#include <iostream>
#include <map>

using namespace std;
int main(){
  int T;
  cin >> T;
  for(int i=0;i<T;++i){
	vector<int> first(4), second(4);
	int selection1, selection2;
	int tmp;

	cin >> selection1;
	for(int j=0;j<4*(selection1-1);++j)   cin >> tmp;
	for(int j=0;j<4;++j){
	  cin >> first[j];
	}
	for(int j=0;j<4*(4-(selection1));++j) cin >> tmp;
	
	cin >> selection2;
	for(int j=0;j<4*(selection2-1);++j)   cin >> tmp;
	for(int j=0;j<4;++j){
	  cin >> second[j];
	}
	for(int j=0;j<4*(4-(selection2));++j) cin >> tmp;
	
	int count=0, last=-1;
	for(int j=0;j<4;++j){
	  for(int k=0;k<4;++k){
		if(first[j]==second[k]){
		  ++count;
		  last = first[j];
		}
	  }
	}

	// cout << "debug:" << endl;
	// for(int j=0;j<4;++j){
	//   cout << first[j] << endl;
	// }
	// for(int j=0;j<4;++j){
	//   cout << second[j] << endl;
	// }
	cout << "Case #" << i+1 << ": ";
	if(count == 1){
	  cout << last;
	}else if(count == 0){
	  cout << "Volunteer cheated!";
	}else{
	  cout << "Bad magician!";
	}
	cout << endl;
  }

  return 0;
}
