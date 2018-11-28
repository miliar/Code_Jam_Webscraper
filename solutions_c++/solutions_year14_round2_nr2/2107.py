#include<iostream>
#include<string>
#include<fstream>
#include<cmath>

using namespace std;

int main(int argc, char* argv[ ]) {
	int T, A,B,K;
	cin>>T;
	for (int t=1; t<=T; t++) {
		cin>>A>>B>>K;
		/*if (K>=A&&K>=B) {
			cout<<"Case #"<<t<<": "<<A*B<<endl;
			continue;
		}*/
		int count=0;
		for (int a=0; a<A; a++) {
			for (int b=0; b<B; b++) {
				if ((a&b)<K) count++;
			}
		}
		cout<<"Case #"<<t<<": "<<count<<endl;
	}
}

//cout<<"Case #"<<t<<": "<<score1<<" "<<N-score2<<endl;