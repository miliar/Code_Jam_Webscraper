#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <gmpxx.h>
#include <math.h>

using namespace std;

mpz_class check( mpz_class t ){

	mpz_class div;
	mpz_class end;

	div = 2;
	end = sqrt(t);
//	cout<<" t "<<t<<" end "<<end<<endl;
	long long guard =0;
	while( (div <= end)&& (guard < 1000000)){
		guard++;
		if(mpz_divisible_p( t.get_mpz_t(),div.get_mpz_t() ))
			return div;
		else
			div++;
	}
	return 0; 
}


int main( int argc, char** argv){


ofstream output;
ifstream input;
cout<< " start "<<endl;
input.open(argv[1]);
output.open("ans.txt");


if(input.fail()){
  cout<<" error opening file"<<endl;
  return -1;
}


int cases;
input >> cases;

int N;
int J;
string s;
string buf;
int count;



for(int i=0; i< cases ; i++){
output<<"Case #"<<i+1<<":"<<endl;  
cout<<"Case #"<<i+1<<":"<<endl;  

input >> N >> J;

count=1;


long long combin = pow(2, (N-2) );

cout<<"combination "<<combin<<endl;

for( int j=0; j<combin ; j++){

	s.clear();
	buf.clear();
	s.push_back('1');
	bitset<(30)> bin(j);
	buf = bin.to_string();
	s=s+buf;
	s.push_back('1');
	cout<<s<<endl;

mpz_class b2( s , 2); 
mpz_class b2a = check(b2);
//cout<<"b2 "<<b2<<" "<<b2a<<endl;
if( b2a ==0 )
	continue;
mpz_class b3( s , 3); 
mpz_class b3a = check(b3);
//cout<<"b3 "<<b3<<" "<<b3a<<endl;
if( b3a ==0 )
	continue;
mpz_class b4( s , 4); 
mpz_class b4a = check(b4);
//cout<<"b4 "<<b4<<" "<<b4a<<endl;
if( b4a ==0 )
	continue;
mpz_class b5( s , 5); 
mpz_class b5a = check(b5);
//cout<<"b5 "<<b5<<" "<<b5a<<endl;
if( b5a ==0 )
	continue;
mpz_class b6( s , 6); 
mpz_class b6a = check(b6);
//cout<<"b6 "<<b6<<" "<<b6a<<endl;
if( b6a ==0 )
	continue;
mpz_class b7( s , 7); 
mpz_class b7a = check(b7);
//cout<<"b7 "<<b7<<" "<<b7a<<endl;
if( b7a ==0 )
	continue;
mpz_class b8( s , 8); 
mpz_class b8a = check(b8);
//cout<<"b8 "<<b8<<" "<<b8a<<endl;
if( b8a ==0 )
	continue;
mpz_class b9( s , 9); 
mpz_class b9a = check(b9);
//cout<<"b9 "<<b9<<" "<<b9a<<endl;
if( b9a ==0 )
	continue;
mpz_class b10( s , 10); 
mpz_class b10a = check(b10);
//cout<<"b10 "<<b10<<" "<<b10a<<endl;
if( b10a ==0 )
	continue;

cout<<s<<" "<<b2a<<" "<<b3a<<" "<<b4a<<" "<<b5a<<" "<<b6a<<" "<<b7a<<" "<<b8a<<" "<<b9a<<" "<<b10a<<" count "<<count<<endl;
output<<s<<" "<<b2a<<" "<<b3a<<" "<<b4a<<" "<<b5a<<" "<<b6a<<" "<<b7a<<" "<<b8a<<" "<<b9a<<" "<<b10a<<endl;

if( count == J ) 
	break;
else
	count++;
}
}

input.close();
output.close();
return 0;
}
