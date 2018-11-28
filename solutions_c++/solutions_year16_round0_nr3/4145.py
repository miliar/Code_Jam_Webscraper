#include <iostream>
#include <bitset>
#include <cmath>
using namespace std;

long long isprime( long long num )
{
    int i  ;
    int sq = ( int ) sqrt ( num );
    for (  i = 2 ; i <= sq ; i++ )
    {
       if ( num % i == 0 )
        { 
        	return i;
        }
    }
    return  0;
}

long long base( std::string binary, int base )
{
	long long value = 0;
	long long multiplier = 1;
	for(int i = 15; i>= 0; i--)
	{
		if(binary[i] == '1')
			value += multiplier;
		
		multiplier *= base;
	}
	return value;
}

int main()
{
	cout<<"Case #1:"<<endl;
    int no = 32769;
    for(int count = 0; count < 50 ; no++)
    {
    	std::string binary = std::bitset<16>(no).to_string();
		//cout<<"binary : "<<binary<<endl;
		
    	if(binary[0] != '1' || binary[15] != '1')
    		continue;
    	
    	//cout<<"base2 : "<<no<<endl;
    	long long base2 = isprime(no);
    	//cout<<"base2 : "<<base2<<endl;
    	if(!base2)
    		continue;
    	
    	long long base3 = base(binary,3);
    	//cout<<"base3 : "<<base3<<endl;
    	base3 = isprime(base3);
    	//cout<<"base3 : "<<base3<<endl;
    	if(!base3)
    		continue;
    	
    	long long base4 = base(binary,4);
    	//cout<<"base4 : "<<base4<<endl;
    	base4 = isprime(base4);
    	//cout<<"base4 : "<<base4<<endl;
    	if(!base4)
    		continue;
    	
    	long long base5 = base(binary,5);
    	//cout<<"base5 : "<<base5<<endl;
    	base5 = isprime(base5);
    	//cout<<"base5 : "<<base5<<endl;
    	if(!base5)
    		continue;
    		
    	long long base6 = base(binary,6);
    	//cout<<"base6 : "<<base6<<endl;
    	base6 = isprime(base6);
    	//cout<<"base6 : "<<base6<<endl;
    	if(!base6)
    		continue;
    		
    	long long base7 = base(binary,7);
    	//cout<<"base7 : "<<base7<<endl;
    	base7 = isprime(base7);
    	//cout<<"base7 : "<<base7<<endl;
    	if(!base7)
    		continue;
    		
    	long long base8 = base(binary,8);
    	//cout<<"base8 : "<<base8<<endl;
    	base8 = isprime(base8);
    	//cout<<"base8 : "<<base8<<endl;
    	if(!base8)
    		continue;
    		
    	long long base9 = base(binary,9);
    	//cout<<"base9 : "<<base9<<endl;
    	base9 = isprime(base9);
    	//cout<<"base9 : "<<base9<<endl;
    	if(!base9)
    		continue;
    		
    	long long base10 = base(binary,10);
    	//cout<<"base10 : "<<base10<<endl;
    	base10 = isprime(base10);
    	//cout<<"base10 : "<<base10<<endl;
    	if(!base10)
    		continue;
    	
    	cout<<binary<<" "<<base2<<" "<<base3<<" "<<base4<<" "<<base5<<" "<<base6<<" "<<base7<<" "<<base8<<" "<<base9<<" "<<base10<<endl;
    	count++;
    }
    return 0;
}
