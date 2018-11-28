#include <iostream>
#include <cmath>
#include <map>
using namespace std;

typedef unsigned int uint;
typedef unsigned long long int ull;

bool isPalindrome(uint x){
    uint x2 = x;
    uint tmp = 0;
    while (x != 0){
	tmp = tmp*10 + x%10;
	x = x/10;
    }
    if (x2 == tmp)
	return true;
    return false;
}

map<int,bool> hash;
map<int,bool>::iterator it;

int main(){
    long int t;
    cin >> t;
    
    for(int tc=1 ; tc<=t ; ++tc){
	ull a,b;
	cin >> a >> b;
	double sq = sqrt(a);
	ull s = (ull)sq;
	if(s*s < a)
	  ++s;
	
	ull c = 0;
	for(ull i=s ; i*i<=b ; ++i)
	    if(isPalindrome(i) && isPalindrome(i*i))
		++c;
	cout << "Case #" << tc << ": " << c << endl;
    }
    return 0;
}