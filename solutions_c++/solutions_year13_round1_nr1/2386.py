#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt0.in");
	fout.open("A-small-attempt0.out");
	unsigned long long test_cases,r,n=1;
	long double total_area=0,t;
	fin>>test_cases;
	for(unsigned long long count=0;count<test_cases;count++) {
		n=1;
		total_area=0;
		fin>>r>>t;
		while(1) {
			total_area += 2*(r+(2*n)-1.5);
			if(total_area==t) {
				break;
			}
			if(total_area>t) {
				n--;
				break;
			}
			n++;
		}
		fout<<"Case #"<<(count+1)<<": "<<n<<"\n";
	}
	return 0;
}
