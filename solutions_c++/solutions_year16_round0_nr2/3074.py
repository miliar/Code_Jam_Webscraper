#include<iostream>
#include<cstdlib>
#include<string>
using namespace std;

int main(){
    int T, ps, ns;
    string pcs;
    cin >> T;
    for(int t=1; t<=T; ++t){
	cin >> pcs;
	ps = 0;
	ns = 0;
	for(char ch: pcs){
	    if(ch == '+'){
		ns = 1+ps;
	    }else{
		ps = 1+ns;
	    }
	}
	cout << "Case #" << t << ": " << ps << endl;
    }

    return 0;
}
