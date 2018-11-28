#include<iostream>
#include<string>
using namespace std;

typedef unsigned long long ull;


int main(){
	int tc, n;
	string s ;
	cin >>tc;
	for(int tt = 1 ; tt<=tc; tt++){
		cin >> n;
		cin >> s;
		
		ull ret = 0, sum = 0 ;
		for( int i = 0; i<= n; i++){
			if( sum >= i ) sum += s[i] - '0';
			else {
				ret += (i-sum);
				sum =  i + s[i]- '0';
			}
		}
		cout<<"Case #"<<tt<<": "<<ret<<endl;
	}
	return 0;
}
