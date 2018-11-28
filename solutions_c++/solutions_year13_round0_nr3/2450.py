#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

typedef unsigned long long int ull;

bool isPalindrome(ull x){
    ull x2 = x;
    ull tmp = 0;
    while (x != 0){
		tmp = tmp*10 + x%10;
		x = x/10;
    }
    if(x2 == tmp)
		return 1;
	return 0;
}

vector<pair<bool,bool> > isPal;

int main(){
 ifstream cc;
 cc.open("C-large-1.in");
 ofstream co;
 co.open("output.txt");
 
    isPal.push_back(pair<bool,bool>(false,false));
    for(ull i=1 ; ; ++i){
	ull x = i*i;
	isPal.push_back(pair<bool,bool>(isPalindrome(i),isPalindrome(x)));
	if(x>100000000000000LL)
	    break;
    }
    long int t;
    cc >> t;
    
    for(int tc=1 ; tc<=t ; ++tc){
	ull a,b;
	cc>> a >> b;
	
	ull s = (ull)sqrt(a);
	ull e = (ull)sqrt(b);
	if(s*s < a)
	  ++s;
	
	ull c = 0;
	for(ull i=s; i<=e ; ++i)
	      if(isPal[i].first==true && isPal[i].second==true)
		  ++c;
	 co<< "Case #" << tc << ": " << c << endl;
    }
    return 0;
}
