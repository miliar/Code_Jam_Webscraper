#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

ofstream out;

int isPalindrome(int x){
	int reverse = 0;
	int temp = x;
	while( temp != 0 )
        {
	        reverse = reverse * 10;
	        reverse = reverse + temp % 10;
	        temp = temp/10;
        }

	return ( x == reverse );
}

void display_palindromes(int x,int y, int cs){
	int n2 = floor(sqrt(y));
	int n1 = ceil(sqrt(x));
	int count = 0;
//	cout<<endl<<"case #"<<cs<<":"<<endl;
	for(int i = n1 ; i <= n2 ; i++){
		if(isPalindrome(i) && isPalindrome(i * i)){
			//cout<<i<<" and "<<(i * i)<<" are Palindrome."<<endl;
			count++;
		}
	}
	out<<"Case #"<<cs<<": "<<count<<endl;
}

int main ( int argc, char *argv[] )
{
	int lp = -1;
	char mat[4][4];
	if ( argc != 2 ) 
		out.open(argv[2]);
	else
		out.open("output.txt");

	if( !out.is_open()){
		cout<<"Could not open output file";
		return -1;
	}
	
    // We assume argv[1] is a filename to open
    ifstream the_file ( argv[1] );
    // Always check to see if file opening succeeded
    if ( !the_file.is_open() )
      out<<"Could not open file\n";
    else {
      
	char y = '1';
	int i = 0;
      // the_file.get ( x ) returns false if the end of the file
      //  is reached or an error occurs
	the_file.get(y);
	while(y != '\n'){
		i = i*10 + (y - 48);
		the_file.get(y);
	}

	for(int j = 1 ; j <= i ; j++){
		
			
		int num1 = 0, num2 = 0;
		the_file.get(y);
		while(y != ' '){
			num1 = num1*10 + (y - 48);
			the_file.get(y);
		}
		the_file.get(y);
		while(y != '\n'){
			num2 = num2*10 + (y - 48);
			the_file.get(y);
		}	
		
		display_palindromes(num1, num2, j);
		
	}
    }
    // the_file is closed implicitly here

	the_file.close();
	out.close();
  
}
