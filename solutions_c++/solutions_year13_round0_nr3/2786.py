#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool palindrome(int n) {
	int digit[10000];
	int len=0;
	while(n>0) {
		digit[len++]=n%10;
		n/=10;
	}
	bool palin=true;
	for(int i=0; i<len/2 && palin; i++)
		if(digit[i]!=digit[len-i-1])
			palin=false;
	return palin;
}

int main() {
	int nTestCases;
	ifstream in("C-small-attempt0.in");
	ofstream out("out");
	in>>nTestCases;
	for(int t=0; t<nTestCases; t++) {
		int min, max;
		in>>min>>max;
		int n=0;
		for(int i=min; i<=max; i++) {
			float root=sqrt(i);
			if(palindrome(i) && (float)i==root*root && palindrome(root)) {
				n++;
			}
		}
		out<<"Case #"<<(t+1)<<": "<<n<<endl;
	}
	in.close();
	out.close();
}