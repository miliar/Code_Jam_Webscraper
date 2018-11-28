#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;


bool isPalindrome(int x) {
  if (x < 0) return false;
  int div = 1;
  while (x / div >= 10) {
    div *= 10;
  }        
  while (x != 0) {
    int l = x / div;
    int r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}

vector<int> ValidSquare(int lower, int higher){

	vector<int> result;
	int ss = 0;
	int ls = 0;

	if(lower > higher) return result;

	if(lower < 0) ss = 0;
	else{
		ss = ceil(sqrt(lower));
	}

	if(higher < 0) ls = 0;
	else{
		ls = floor(sqrt(higher));
	}

	for(int i = ss; i <= ls; i++){
		if(isPalindrome(i)){
			result.push_back(i);
		}
	}

	return result;
}

void solve(int test){
	int lower = 0, higher = 0;
	cin >> lower >> higher;

	int sandq = 0;

	vector<int> source = ValidSquare(lower, higher);
	vector<int>::iterator iter = source.begin();
	for(;iter!=source.end(); iter++){
		if(isPalindrome((*iter)*(*iter))){
			sandq++;
		}
	}

	cout << "Case #" << test << ": " << sandq << endl;
}

int main(){

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests = 0;
	scanf("%d", &tests);
	for(int i=1; i<=tests; i++){
		solve(i);
	}

}