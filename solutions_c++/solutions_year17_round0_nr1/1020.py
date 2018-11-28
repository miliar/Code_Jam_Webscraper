#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;
int main(){
	ifstream is("A-large.in");
	ofstream os("A.out");
	int n,k;
	is >> n;
	string s;
	int l = 1;
	while(l <= n){
		is >> s >> k;
		int cc = 0;
		for(int i = 0; i <= s.length() - k; i++){
			if(s[i]=='-'){
				for(int j=0;j<k;j++){
					if(s[i+j]=='-')s[i+j]='+';
					else s[i+j]='-';
				}
				cc++;
			}
		}
		bool no = false;
		for(int i=0;i<s.length();i++){
			if(s[i]=='-'){no=true;break;}
		}
		if(no){os << "Case #" << l << ": IMPOSSIBLE\n";}
		else os << "Case #" << l << ": " << cc << '\n';
		l++;
	}
	is.close();
	os.close();
	return 0;
}
