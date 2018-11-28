#include <iostream>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

typedef unsigned long long int ull;

bool isPalindrome(ull x){
    ull x2 = x;
    ull tmp = 0;
    while (x != 0){
	tmp = tmp*10 + x%10;
	x = x/10;
    }
    return (x2 == tmp);
}

vector<pair<bool,bool> > isPal;

int main(){
    isPal.push_back(pair<bool,bool>(false,false));
    for(ull i=1 ; ; ++i){
	ull x = i*i;
	isPal.push_back(pair<bool,bool>(isPalindrome(i),isPalindrome(x)));
	if(x>100000000000000LL)
	    break;
    }
    
    long int t;
    cin >> t;
    
    for(int tc=1 ; tc<=t ; ++tc){
	ull a,b;
	cin >> a >> b;
	
	ull s = (ull)sqrt(a);
	ull e = (ull)sqrt(b);
	if(s*s < a)
	  ++s;
	
	ull c = 0;
	for(ull i=s; i<=e ; ++i)
	      if(isPal[i].first==true && isPal[i].second==true)
		  ++c;
	cout << "Case #" << tc << ": " << c << endl;
    }
    return 0;
}

