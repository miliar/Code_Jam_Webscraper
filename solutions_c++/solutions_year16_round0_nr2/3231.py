#include <iostream>
#include <string>
using namespace std;

string S;
inline void reverse(){
	for(unsigned i=0;i<S.size()-1-i;i++)
		swap(S[i],S[S.size()-i-1]);
}

int main(){
	int T, tt;
	cin >> T;
	for(tt=1;tt<=T;tt++){
		cout << "Case #" << tt << ": ";
		cin >> S; reverse();
		unsigned i=0, ans = 0;
		bool p=true;
		while(i<S.size()){
			if(p){
				while(i<S.size() && S[i]=='+')i++;
				if(i<S.size())ans++;
				p=!p;
			} else{
				while(i<S.size() && S[i]=='-')i++;
				if(i<S.size())ans++;
				p=!p;
			}
		} cout << ans << endl;
	}
	return 0;
}
