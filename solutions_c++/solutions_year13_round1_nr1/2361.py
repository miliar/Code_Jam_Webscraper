#include <iostream>
#include <string>
#include <vector>
using std::vector;
using std::string;

int main(void){
	using namespace std;

	int T;cin>>T;
	for(int X=1;X<=T;X++){
		long long  result=0;
		long long r;cin>>r;
		long long t;cin>>t;
		//
		long long R=r;
		double u = 2*R+1;
		while(t-u>=0){
			result++;
			R+=2;
			u+=2*R+1;
		}
		//
		cout<<"Case #"<<X<<": "<<result<<endl;
	}
	cout.flush();
	cerr.flush();
	return 0;
}
