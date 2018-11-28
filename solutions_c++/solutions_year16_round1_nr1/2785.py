#include <iostream>

using namespace std;

string push_end(string in,char a){
	return in + a;
}

string push_start(string in, char a){
	return a + in;
}

int main(){
	int t,t0=0;
	string tmp, out;
	cin >> t;
	while(t0++<t){
		tmp = out = "";
		cout << "Case #" << t0 << ": ";
		cin >> tmp;
		for(int i = 0; i < tmp.length(); i++){
			if(i == 0){
				out = tmp[0];
			}else if(out[0] <= tmp[i]){
				out = push_start(out,tmp[i]);
			}else{
				out = push_end(out,tmp[i]);
			}
		}
		cout << out << endl;
	}
	return 0;
}