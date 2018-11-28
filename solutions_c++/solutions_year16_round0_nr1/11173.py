#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include<vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

void sacarNumeros(const int n, vector<int> &vec){
	int num = n;
	int exp = 1;
	int digit;
	while(n >= exp){
		digit = (num / exp) % 10;
	//	cout <<  num << "/" << exp << "= " << num/exp << "%10" <<  "... el digito es " << digit << endl;
		vec[digit] = 1;
		exp = exp * 10;
	}
	
}	

bool leyoTodos(vector<int> vec){
	for (int i = 0; i < 10; i++){
		if(vec[i]== 0) {
			return false;
		}
	}
  return true;
}

int main() {
	int t, n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	vector<int> vec(10);
  
	for (int i = 1; i <= t; ++i){
		cin >> n ;  // read n.
		int mult = 1;
		int last = n;
		for (int j = 0; j < 10; j++){
		  vec[j] = 0;
		}
		
		if (n!= 0){
			while(!leyoTodos(vec)){
				last = n*mult;
				//cout << "last es :" << last << endl;
				sacarNumeros(last,vec);
				mult++;
			}
		
			cout << "Case #" << i << ": " << last << endl;
			// cout knows that n + m and n * m are ints, and prints them accordingly.
			// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
		}else{
		cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
	}    
  return 0;
}
