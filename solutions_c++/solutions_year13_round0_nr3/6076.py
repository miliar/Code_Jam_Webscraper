#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;

bool isFair(string nr);

int main(){
	ios_base::sync_with_stdio(0);
	int caseNum;
	cin >> caseNum;
	REP(x, caseNum){
		int counter = 0;
		int a, b;
		cin >> a >> b;
		while(a <= b){
			string s;
			stringstream out;
			out << a;
			s = out.str();
			bool aIsFair = isFair(s);
			if(aIsFair){
				double sqa = sqrt(a);
				int sqai = sqa;
				if(sqa == sqai){
					string ss;
					stringstream out1;
					out1 << sqai;
					ss = out1.str();
					if(isFair(ss))
						counter++;
				}		
			}
			a++;
		}
		cout << "Case #" << x+1 << ": " << counter << endl;
	}
	return 0;
}


bool isFair(string nr){
	int lenght = nr.length();
	bool isPalindrome = 1;
	int i = 0;
	while(isPalindrome && i < lenght/2){
		if(nr[i] != nr[lenght-1-i])
			isPalindrome = 0;
		i++;
	}
	if(isPalindrome)
		return 1;
	else
		return 0;
}
