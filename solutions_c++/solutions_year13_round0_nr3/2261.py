#include <vector>
#include <fstream>
#include <iostream>
#include <cmath>

using namespace std;

vector<long long> palindromes, squares;

long long mypow( int e ){
	if( e == 1 ) return 10LL;
	if( !(e%2)  ){
		long long res = mypow(e/2);
		return res*res;
	}
	
	long long res = mypow((e-1)/2);
	return 10LL*res*res;
}

void add_palindrome( int n ){
	long long ndigits = (long long)ceil(log10((double)n+0.5));
	long long reverse = 0, ncopy=n;
	
	while(ncopy > 0 ){
		int d = ncopy%10;
		reverse*=10;
		reverse+=d;
		ncopy=(ncopy-d)/10;
	}

	palindromes.push_back(n*mypow(ndigits)+reverse);

	for( int b=0;b<=9;++b ){	
		palindromes.push_back(n*mypow(ndigits+1)+reverse+mypow(ndigits)*b);
	}
}

bool palindrome( long long n ){
	vector<int> digits;
	long long copy = n;
	
	while(copy > 0){
		int d = copy%10;
		digits.push_back(d);
		copy=(copy-d)/10;
	}
	
	for( int i=0;i<digits.size()/2;++i ){
		if( digits[i] != digits[digits.size()-1-i] ) return false;
	}
	
	return true;
}

int main(){
	ifstream infile("C-large-1.in");
	ofstream outfile("Clarge1out.out");
	int T;
	
	for( int i=1;i<10;++i ){
		palindromes.push_back(i);
	}
	
	for( int i = 1 ; i < 1000 ; ++i ){
		add_palindrome(i);
	}
	
	//cout<<"size "<<palindromes.size()<<endl;
	for( int i=0;i<palindromes.size();++i ){
	//	if( palindromes[i]*palindromes[i] < 0 ) cout<<"help"<<endl;
		if( palindrome(palindromes[i]*palindromes[i]) ){
			squares.push_back(palindromes[i]*palindromes[i]);
			//cout<<"found good "<<palindromes[i]*palindromes[i]<<endl;
		}
	}
	
	infile>>T;
	
	for( int t=1;t<=T;++t ){
		long long A, B;
		int aantal=0;
		infile>>A>>B;
		
		for( int i=0;i<squares.size();++i ){
			if( squares[i] >= A && squares[i] <= B ) aantal++;
		}
		
		outfile<<"Case #"<<t<<": "<<aantal<<endl;
	}
	
	return 0;
}