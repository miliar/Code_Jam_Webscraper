
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

void standingOvation()
{
	int t;
	std::cin>>t;
	for(int i = 0; i < t; ++i) {
		int slen;
		std::string s;
		std::cin>>slen>>s;
		int present = s[0] - '0';
		int req = 0;
		for(auto j = 1; j < s.size(); ++j) {
			int numppl = (int)(s[j] - '0');
			if(present < j && numppl != 0) {
				req += j - present;
				present += j - present;
			}
			present += numppl ;
		}
		std::cout<<"Case #"<<i+1<<": "<<req<<std::endl;
	}
}

void pancakes()
{
	int t;
	std::cin>>t;
	for(int i=0; i < t ; ++i) {
		int d;
		std::cin>>d;
		std::vector<int> a;
		for(int j=0; j < d; ++j) {
			int p;
			std::cin>>p;
			a.push_back(p);
		}
		std::sort(a.begin(), a.end());
		while(1) {

		}
	}
}

char quatProd(char a, char b)
{
	std::vector<std::string> qtable;
	qtable.push_back("hijk");
	qtable.push_back("iHkJ");
	qtable.push_back("jKHi");
	qtable.push_back("kjIH");

	int m;
	int n;
	bool isaNeg = false;
	bool isbNeg = false;
	if(islower(a)) {
		m = a-'h';
	} else {
		isaNeg = true;
		m = a-'H';
	}
	if(islower(b)) {
		n = b - 'h';
	} else {
		isbNeg = true;
		n = b-'H';
	}
	char prod = qtable[m][n];
	if(isaNeg != isbNeg) {
		if(islower(prod)) {
			prod = 'H' + (prod - 'h');
		} else {
			prod = 'h' + (prod - 'H');
		}
	}
	return prod;
}
char divide(char a, char b)
{
	std::vector<std::string> qtable;
	qtable.push_back("hijk");
	qtable.push_back("iHkJ");
	qtable.push_back("jKHi");
	qtable.push_back("kjIH");
	int m;
	int n;
	bool isaNeg = false;
	bool isbNeg = false;
	if(islower(a)) {
		m = a-'h';
	} else {
		isaNeg = true;
		m = a-'H';
	}
	if(islower(b)) {
		n = b - 'h';
	} else {
		isbNeg = true;
		n = b-'H';
	}
	char quot;
	if(qtable[m][0] == b) {
		quot = 'h';
	} else if(qtable[m][1] == b) {
		quot = 'i';
	} else if(qtable[m][2] == b) {
		quot = 'j';
	} else if(qtable[m][3] == b) {
		quot = 'k';
	}

	if(isaNeg && isbNeg) {
		if(!islower(quot)) {
			quot = 'h' + (quot - 'H');
		}
	} else if(isaNeg || isbNeg) {
		if(islower(quot)) {
			quot = 'H' + (quot - 'h');
		}
	}
	return quot;
}
char findprod(std::vector<char>& prodArray, int i, int j)
{
	return divide(prodArray[i], prodArray[j]);
}

void initializeProdtable(std::vector<char> & array, std::string input)
{
	array.push_back(input[0]);
	for(int i = 1; i < input.size(); ++i) {
		char tempprod = quatProd(array[i-1], input[i]);
		array.push_back(tempprod);
	}
}

void dijkstras()
{
	int t;
	std::cin>>t;
	for(int i = 0; i < t; ++i) {
		int l;
		int x;
		std::string qstr;
		std::string realqstr;
		std::cin>>l>>x>>qstr;
		for(int j = 0; j < x; ++j) {
			realqstr.append(qstr);
		}
		bool foundResult = false;
		vector<char> prodArray;

		for(int m = 0; m < realqstr.size() - 2 && !foundResult; ++m) {
			for(int n = m + 1; n < realqstr.size() - 1 && !foundResult; ++n) {
				if((prodArray[m] == 'i') &&
				   (findprod(prodArray, m+1, n) == 'j') &&
				   (findprod(prodArray, n+1, realqstr.size() - 1))) {
					foundResult = true;
				}
			}
		}
		if(foundResult) {
			std::cout<<"Case #"<<i+1<<": YES"<<std::endl;
		} else {
			std::cout<<"Case #"<<i+1<<": NO"<<std::endl;
		}
	}
}
int main() {
	//dijkstras();
	standingOvation();
	return 0;
}
