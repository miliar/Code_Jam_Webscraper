#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;



bool isComplete(unordered_map<int, bool> numbers){
	for (auto it = numbers.begin();it !=numbers.end(); it++){
		if (!it->second) return false;
	}
	return true;
}

int main() {
  int testCases;
  cin >> testCases;
  unordered_map<int, bool> numbers;
  vector<int> result;
  for(int j=0; j<10; j++){
	  numbers.insert({j, false});
  }

  for (int i = 1; i <= testCases; ++i) {
	  int N;
	  cin >> N;
	  if (N==0) result.push_back(-1);
	  else if (N==1) result.push_back(10);//cout<<"Case #"<<i<<": "<<"10" <<endl;
	  else{
		  int j = 1;
		  for (auto it = numbers.begin();it !=numbers.end(); it++){
			  it->second=false;
		  }
		  while(true){
			  int n =j*N;
			  string temp = to_string(n);
			  for(char c:temp){
				  int k = c - '0';
				  auto it = numbers.find(k);
				  it->second = true;
			  }
			  if(isComplete(numbers)){
				  result.push_back(n);
				  break;
			  }
			  j++;
		  }

	  }

  }
  for(int i=0; i<result.size();i++){
	  if (result[i]==-1)
		  cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
	  else
		  cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
  }
  return 0;
}


