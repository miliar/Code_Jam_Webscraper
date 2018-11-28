// Pre-written
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>

#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#define ALL(x) (x).begin(),(x).end()
#define FOR(i,a,b) for(i=a;i<=(b);i++)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define ZERO(x,s) memset(x,0,sizeof(s))
// Pre-written

void start() {

}

int numDigits(long number)
{
   int digits = 0; 
   while (number != 0) { 
	   number /= 10; 
	   digits++; 
   }
   return digits;
}
int nthdigit(long x, int n)
{
    while (n--) {
        x /= 10;
    }
    return x % 10;
}
bool palindrome(long x) {
	if(x < 10) return true;
	int digits = numDigits(x);
	int i;
	int a, b;
	for(i=0; i < digits / 2; i++) {
		a = nthdigit(x, i);
		b = nthdigit(x, digits - i - 1);
		if(a != b ) return false;
	}
	return true;
}

void doIt() {
	long gA, gB;
	cin >> gA;
	cin >> gB;

	long start = sqrt((double) gA) + 0.5;
	long i;
	long mocnina;
	long pocet = 0;
	for(i=start; true; i++) {
		if(!palindrome(i)) continue;
		mocnina = i*i;
		if(mocnina < gA) continue;
		if(mocnina > gB) break;
		if(palindrome(mocnina)) {
			pocet++;
		}
	}
	cout << pocet;
	cout << "\n";
}

int main( int argc, const char* argv[] )
{
	ifstream in("in.in");
    cin.rdbuf(in.rdbuf());

    ofstream out("out.out");
    cout.rdbuf(out.rdbuf());
	
	/*
	bool x;
	//x = palindrome(4);
	x = palindrome(454);
	x = palindrome(4554);
	x = palindrome(2311);
	*/
	int n;
	cin >> n;
	start();
	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";
		doIt();
	}
	return 0;
}