#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int n,k,s=0,sum=0,dif;
	char c[1001];

	ifstream read("input.in");
	ofstream write("out.out");

	read >> n;

	for(int i = 1 ; i <= n ; i++) {
		read >> k;
		read >> c;

		for(int j = 1 ; j <= k ; j++) {
			s += ((int)c[j-1] - 48);

			if((j > s) && ((int)c[j] - 48) > 0) {
				dif = j - s;
				s += dif;
				sum += dif;
			}
		}

		write << "Case #" << i << ": " << sum << endl;
		s=0;
		sum=0;
	}
}
