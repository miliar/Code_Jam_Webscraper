#include <iostream>
#include <iomanip>
#include <math.h> 
using namespace std;
long long CONST =  1099511627776ll;
long long gcd(long long u, long long v)
{
    // simple cases (termination)
    if (u == v)
        return u;
 
    if (u == 0)
        return v;
 
    if (v == 0)
        return u;
 
    // look for factors of 2
    if (~u & 1) // u is even
    {
        if (v & 1) // v is odd
            return gcd(u >> 1, v);
        else // both u and v are even
            return gcd(u >> 1, v >> 1) << 1;
    }
 
    if (~v & 1) // u is odd, v is even
        return gcd(u, v >> 1);
 
    // reduce larger argument
    if (u > v)
        return gcd((u - v) >> 1, v);
 
    return gcd((v - u) >> 1, u);
}


int main(){
	int numberOfTestCases;
	
	cin >> numberOfTestCases;
	int caseNumber = 0;
	long long citatel;
	long long divisor;
	char ch;
	while(numberOfTestCases--){			
		//scanf("%ld/%ld", citatel, ch, divisor);		
		cin >> ch;			
		caseNumber++;
		
		citatel=0;
		while(ch != '/'){
			citatel *= 10;
			citatel += ch-'0';
			cin >> ch;
		}
		cin >> ch;
		
		divisor = 0;
		while(ch != '\n'){
			divisor *= 10;
			divisor += ch-'0';
			scanf("%c", &ch);
		}
		
		
		
		long long greatest = gcd(citatel, divisor);
		
		divisor /= greatest;

		bool isMocnina = false;
		long long mocnina = 1;
		while(2){
			if(divisor == mocnina){
				isMocnina = true;
				break;
			}
			if(mocnina > divisor){
				isMocnina = false;
				break;
			}
			mocnina *= 2;
		}
		if(!isMocnina){
			cout << "Case #" << caseNumber << ": impossible\n";
			continue;
		}
		citatel /= greatest;
		long long numberOfElves = (citatel  * CONST) / divisor;

		long long generation=40;
		while(numberOfElves > 1){
			generation--;
			numberOfElves /= 2;
		}
		std::cout << "Case #" << caseNumber << ": " << generation << "\n"; 	
	}
	
	//std::cout << setprecision(7) << fixed;
		
	return 0;
}