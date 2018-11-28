#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main(){
  int N;
  cin >> N;

  for(int i=1;i<=N;++i){
	int prevLine, nextLine;
	int prevCards[5][5], nextCards[5][5];

	cin >> prevLine;
	for(int j=1;j<=4;++j){
	  for(int k=1;k<=4;++k){
		cin >> prevCards[j][k];
	  }
	}
	cin >> nextLine;
	for(int j=1;j<=4;++j){
	  for(int k=1;k<=4;++k){
		cin >> nextCards[j][k];
	  }
	}

	vector<int> ret;
	for(int j=1;j<=4;++j){
	  for(int k=1;k<=4;++k){
		if(prevCards[prevLine][j] == nextCards[nextLine][k]){
		  ret.push_back(nextCards[nextLine][k]);
		  break;
		}
	  }
	}
	if(ret.size() == 1){
	  printf("Case #%d: %d\n", i, ret[0]);
	}
	else if(ret.size() > 1){
	  printf("Case #%d: %s\n", i, "Bad magician!");
	}else{
	  printf("Case #%d: %s\n", i, "Volunteer cheated!");
	}
  }
  return 0;
}
