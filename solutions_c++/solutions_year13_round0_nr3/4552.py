#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;
int t;
unsigned long long a, b;
bool palindrome(unsigned long long x){
	unsigned long long z, y = 0;
	z = x;
	while (x){
		y = y*10+x%10;
		x /= 10;
	}
	return z==y;
}

void read(){
	int i, c;
	unsigned long long j, k;
	ifstream f("C-small-attempt0.in");
	ofstream g("C-small-attempt0.out");
	f>>t;
	for (i = 1; i<=t; i++){
		c = 0;
		f>>a>>b;
		for (j = ceil(sqrt((double)a)); j<=ceil(sqrt((double)b)); j++)
			if(palindrome (j)){
				k = j*j;
				if (a<=k&&k<=b)
					if (palindrome (k)) c++;
			}
		g<<"Case #"<<i<<": "<<c<<'\n';
	}
	g.close();
	f.close();
}

int main(){
	read();
	return 0;
}