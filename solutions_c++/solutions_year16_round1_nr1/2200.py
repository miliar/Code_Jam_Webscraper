#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	ios_base::sync_with_stdio(0);
	int t,i,j=1;
	ifstream infile;
	ofstream outfile;
	infile.open("A-large.in");
	outfile.open("output1.txt");
	string a;
	infile>>t;
	while(t--){
		string b;
		infile>>a;
		b.push_back(a[0]);
		for(i=1;i<a.length();i++){
			if((a[i])<(b[0])) b.push_back(a[i]);
			else b=a[i]+b;
		}
		outfile<<"Case #"<<j<<": "<<b<<endl;
		j++;
	}
	return 0;
}
