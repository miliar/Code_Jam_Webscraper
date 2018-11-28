#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

long long a, b, total;
bool isPalindrome;
long long number, square;

vector<string> palindromes12, palindromes34, palindromes56, palindromes78, palindromes;

void verify(string s){
	
	
	int len;
	if (s[0]!='0'){
		std::stringstream ss(s);
		
		ss >> number;
		square = number * number;
		
		string squarestring = static_cast<ostringstream*>( &(ostringstream() << square) )->str();

		len = squarestring.size();
		isPalindrome=true;
		for (int k = 0; k < len; ++ k ){
			if (squarestring[k] !=squarestring[len-k-1]){
				isPalindrome=false;
				break;
			}
		}
		if (isPalindrome && square >= a && square <=b) 
			total++;
	}
}
void solve(void){
	total = 0;
	cin >> a >> b;

	
	for (unsigned int k = 0; k <palindromes12.size();++k)
		verify(palindromes12[k]);
	for (unsigned int k = 0; k <palindromes34.size();++k)
		verify(palindromes34[k]);
	for (unsigned int k = 0; k <palindromes56.size();++k)
		verify(palindromes56[k]);

	for (unsigned int k = 0; k <palindromes78.size();++k)
		verify(palindromes78[k]);

	cout << total;
}

int main(void){
	int n;
	cin >> n;
	
	string tmp="X", ltmp="XX";
	for (char k = '0'; k<'9';++k){
		tmp[0]=k;
		ltmp[0]=k;
		ltmp[1]=k;
		palindromes12.push_back(tmp);
		palindromes12.push_back(ltmp);
	}

	for (char k = '0'; k<'9';++k){
		for (int i = 0;i<palindromes12.size();++i){
			palindromes34.push_back(k+palindromes12[i]+k);
		}
	}
	for (char k = '0'; k<'9';++k){
		for (int i = 0;i<palindromes34.size();++i){
			palindromes56.push_back(k+palindromes34[i]+k);
		}
	}
	for (char k = '0'; k<'9';++k){
		for (int i = 0;i<palindromes56.size();++i){
			palindromes78.push_back(k+palindromes56[i]+k);
		}
	}


	for (int k=0;k<n;++k){
		cout << "Case #"<<k+1<<": ";
		solve();
		cout << endl;
	}

	return 0;
}