#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	ifstream input;
	input.open("D-small-attempt0.in");
	ofstream output;
	output.open("out.txt");
	input >> t;
	int i=0,k,c,s;
	while(t--){
		i++;
		output << "Case #" <<i<<": ";
		input >> k>>c>>s;
		for(int i=1;i<=k;i++){
			output << i <<" ";
		}
		output << endl;
	}
	return 0;
}
