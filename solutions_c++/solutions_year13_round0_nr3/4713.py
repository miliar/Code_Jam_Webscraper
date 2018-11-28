#include<iostream>
#include<fstream>
using namespace std ;
bool IsPalindrome(long long x){

	long long n, digit, rev = 0;
     n = x;
     do
     {
         digit = x%10;
         rev = (rev*10) + digit;
         x = x/10;
     }while (x!=0);
   
     if (n == rev)
       return true ; 
     else
       return false ; 
}

int main(){ 

	long long *p = new long long[100] ; 
	for(long long i = 0 , j=1 ; i <=10000000 ; i++ ){
		if(IsPalindrome(i*i)&&IsPalindrome(i)){
			p[j] = i*i; j++ ; 
		}
	}
	ifstream fin ("ss.in") ; 
	ofstream fout ("s.out") ;
	int n ;
	long double  a , b ; 
	long long e ; 
	int  count  ;
	fin >> n ;
	for(int i =1  ; i <= n ; i++ ){
		fin>> a >> b ;
		count = 0 ;
		for(long long i = 1 ; i <= 99 ; i++){

			if(p[i]>=a && p[i]<=b ){
				count++;
			}
		}
		fout<<"Case #"<<i<<": "<<count<< endl; 
	}
	delete[] p ;
	return 0 ;
}
