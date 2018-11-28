#include<iostream>
#include <sstream>
#include<fstream>
#include<string>

using namespace std ;

bool IsPalindrome(int x){
	ostringstream oss;
	oss << x ;
	string str = oss.str() ; 
	int o =  str.length()-1; 
	for(int i = 0 ; i <= o  ; i++){
		if(str[i] == str[o-i])
			continue ;
		else return false ; 
	}
	return true ;  
}

int main(){

	ifstream fin ("s.in") ; 
	ofstream fout ("s.out") ;
	
	int n , a , b , count ; 
	fin >> n ;
	for(int i =1  ; i <= n ; i++ ){
		fin>> a >> b ;
		count = 0 ;
		for(int q = a ; q <=b ; q++){
			double power = pow(q , 0.5) ; 
			if(IsPalindrome(q))
				if (power == (int)power)
						if(IsPalindrome(power))
							count++ ;
		}
		fout<<"Case #"<<i<<": "<<count<< endl; 
	}
}