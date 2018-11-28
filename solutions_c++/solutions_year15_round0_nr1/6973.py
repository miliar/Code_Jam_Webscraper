#include<iostream>
#include<fstream>
using namespace std;
char s[1500];
int sMax;
int T;

int solve(int sMax,char *s){
	int total = 0;
	int result = 0;
	for(int i=0;i<sMax+1;i++){
		if(total < i){
			result += i-total;
			total = i;
		}
		total += s[i]-'0';
	}
	return result;
}

int main(int argc,char *argv[]){
	ifstream in(argv[1]);
	in >> T;
	for(int t=1;t<=T;t++){
		in >> sMax;
		in >> s;
		cout << "Case #" << t << ": " << solve(sMax,s) << endl;
	}
}