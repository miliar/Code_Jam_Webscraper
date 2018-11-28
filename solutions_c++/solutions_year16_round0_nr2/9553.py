#include <iostream>
#include <string>
#include <fstream>

using namespace std;

std::ifstream infile("B-large.in");
std::ofstream outfile ("B-out-la.txt",std::ios::out);

int minFilp(string s){
	if(s.empty())
		return -1;

	int m=0, n=0; // number of '-','+'
	int i=0;
	while(i<s.length()){
		if(s[i]=='-')
			m++;
		while(s[i]=='-'){ //skip -
			i++;
		}

		if(s[i]=='+')
			n++;
		while(s[i]=='+') //skip +
			i++;
	}

	if(s[0]=='-') return 1+2*((m+n-1)/2);
	else return 2*((m+n)/2);
}

int main()
{
	int test_n;
    infile>>test_n;

    for(int i=1; i<=test_n; ++i) {
    	string cakes="";
    	infile>>cakes;
    	outfile<<"Case #"<<i<<": "<<minFilp(cakes)<<endl;
    }

    outfile.close();
}
