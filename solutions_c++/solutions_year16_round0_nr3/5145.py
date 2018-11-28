#include <iostream>
#include <string>
#include <cmath>
using namespace std;
long long int primes[24] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,81,83};
long long int is_it_prime(long long int num){
    //if((num%2==0)||(num%3==0)||(num%5==0)||(num%7==0)||(num%11==0)||(num%13==0)||(num%17==0)||(num%19==0)||(num%23==0)||(num%29==0)||(num%31==0)||(num%37==0)||(num%41==0)||(num%43==0)||(num%47==0)||(num%53==0)||(num%59==0)||(num%61==0)||(num%67==0)||(num%71==0)||(num%73==0)||(num%79==0)||(num%83==0))
    //    return 0;
    long long int flag = 0;
    for(int i=0;i<24;i++){
        if(num%primes[i]==0)    flag=primes[i];
    }
    //cout << num << "is prime" << endl;
    return flag;
}

long long int convert_into_ll(string s,int base){
    long long int value = 0;
    for(int i = 0;i<s.length();i++){
        value += (s[i]-'0')*pow(base,s.length()-i-1);
    }
    //cout << "Value of " << s << " is " << value << " in base = " << base << endl;
    return value;
}

bool check_primality(string s){
    long long int num[10];
    for(int i=0;i<9;i++)
        if(!is_it_prime(convert_into_ll(s,2+i)))
            return 1;
    return 0;
}
void print_factors(string s){
     int num;
     for(int i=0;i<9;i++){
        num = is_it_prime(convert_into_ll(s,2+i));
        cout << num << " ";
     }
 }
int main() {
    long long int test, n, j, i, k, carry, count=0;
	cin >> test;
	int h=0;
	while(test--){
	    h++;
	    cout << "Case #" << h<< ":" << endl;
	    cin >> n >> j;
	    string s(n,'0');
	    s[0] = '1';
	    s[n-1] = '1';
	    while(j){
	        carry = 1;
	        for(i=n-2;i>0;i--){
	            if(carry==1){
	                if(s[i]=='1')   s[i] = '0';
	                else           {s[i] = '1';     carry = 0;      break;}
	            }
	        }
	        //cout << "count is " << count++ << "and string is" << s << " ";
	        count++;
	        if(!check_primality(s)){
	            j--;
	            //cout << "Composite : "<< s << " ";
	            long long int number = convert_into_ll(s,10);
	            cout << s << " ";
	            print_factors(s);
	            cout << endl;
	        }
	    }
	    //cout << "count ==" << count;
	}
	//string dd = "10000000000000000000000011111101";
	//cout << check_primality(dd);
	return 0;
}
