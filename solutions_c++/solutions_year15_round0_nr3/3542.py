#include<iostream>
using namespace std;

int main(){
	int T, l, x, sign;
	string s;
	char last,c;
	bool iseen, jseen, kseen;
	cin >> T;
	for(int t=1; t<=T; t++){
		iseen=false;jseen=false;kseen=false;
		cin >> l >> x;
		cin >> s;
		if(l*x<3 || l==1){
			cout << "Case #" << t << ": NO" << endl;
		}	
		else{
			last = s[0]; sign=0;
			for(int i=1; i<x*l; i++){
				if(last=='i' && sign==0) iseen=true;
				if(last=='k' && sign==0 && iseen==true) jseen=true;
				c=s[i%l];
				if(c=='1')last=last;
				else if(last=='1')last=c;
				else if(c==last) {sign=!sign; last='1';}
				else if(last=='i' && c == 'j') last='k';
				else if(last=='j' && c == 'k') last='i';
				else if(last=='k' && c == 'i') last='j';
				else if(last=='j' && c == 'i') {last='k'; sign=!sign;}
				else if(last=='k' && c == 'j') {last='i'; sign=!sign;}
				else if(last=='i' && c == 'k') {last='j'; sign=!sign;}
			}
			if(last=='1' && sign==1 && jseen==true) kseen=true;
			if(kseen)cout << "Case #" << t << ": YES" << endl;
			else cout << "Case #" << t << ": NO" << endl;
		}
	}
}
