#include <iostream>
using namespace std;

int main(){
	int t,s,st,cl,k;
	char c;
	cin >>t;
	for(int i=0;i<t;i++){
		cin >>s;
		cin >>c;
		cl = 0;
		st = c - '0';
		for(int i=1;i<=s;i++){
			cin >>c;
			if(st<i){
				k = i - st;
				cl += k;
				st += k;
			}
			st += c-'0';
		}
		cout <<"Case #" <<i+1 <<": " <<cl <<endl;
	}
	return 0;
}