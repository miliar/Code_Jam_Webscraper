#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	int T,ct,i,j,len,K,flips;
	char S[1000],passed;
	string input = "";

	cin >> T;
	getline(cin, input);
//	cout <<T<<endl;
	for (ct = 1; ct <= T; ++ct) {
		getline(cin, input);
//		cout <<input<<endl;
		len = 0; K = 0;
		for(i=0;i<input.length();i++){
			if(input[i]=='+')
				S[len++] = 1;
			else if(input[i]=='-')
				S[len++] = 0;
			else if(input[i]!=' ')
				K = K*10 + input[i]-'0';
		}
//		for(i=0;i<len;i++) printf("%d",S[i]);
//		printf(" %d\n",K);
		flips = 0;
		for(i=0;i<=len-K;i++){
			if(S[i]==0){
				for(j=i;j<i+K;j++)
					S[j] ^= 1;
				flips++;
			}
		}
		passed = 1;
		for(i=0;i<len;i++){
			if(S[i]==0){
				passed = 0;
				break;
			}
		}
		if(passed)
			cout << "Case #" << ct << ": " <<flips<< endl;
		else
			cout << "Case #" << ct << ": IMPOSSIBLE" << endl;
	}
}