#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int checkp(int n){
	int n1, rev = 0, rem;
	n1 = n;
  if (n<10) return 1;
	while (n > 0){
	rem = n % 10;
	rev = rev * 10 + rem;
	n = n / 10; }
	if (n1 == rev)
	return 1;
	else
	return 0;
}


int main()
{


	ofstream outf;
	ifstream inf;
	outf.open("output.in");
	inf.open("input.in");


    //istringstream lines(line);

	int t;
	inf>>t;
//cout<<checkp(33)<<"\n";

	for(int tt=0;tt<t;tt++)
	{
		int low, high;
		inf>>low>>high;
		int base = sqrt(low);

		int test=0;
		int counter=0;

		test=base*base;
		while(test < low){
			base++;
			test=base*base;
		}
		if(tt==94)
		cout<<base<<" "<<test<<"\n";

		while (test <= high){
		if (checkp(base)==1){
		if (checkp(test)==1){
			counter++;
			if(tt==94)
									cout<<base<<" "<<test<<" "<<counter<<" "<<high<< "\n";

		}
		}
			base++;
			test=base*base;

		}
		if(low==high==1)
			outf<<"Case #"<<tt+1<<": "<<1<<"\n";
		else
		outf<<"Case #"<<tt+1<<": "<<counter<<"\n";
	}


}







