#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;
double findTime(double c,double f, double x) {
	int i=0;
	double count=0;
	while(x/(2+f*i) >= c/(2+f*i) + x/(2+f+f*i)){
			count+= c/(2+f*i);
			i++;
		}
		count+=x/(2+f*i);

		return count;
}

int main() {
	int t,n;
	double c,f,x,ti;
	ifstream myin;
	myin.open("B-large.in");
	ofstream myout;
	myout.open("output.out");

	myout.setf(ios::fixed, ios::floatfield);
	myout.precision(7);

	myin>>t;
	n=1;
	while(n<=t) {
		
		myin>>c>>f>>x;
		
		ti = findTime(c,f,x);
		myout<<"Case #"<<n<<": "<<ti<<"\n";

		n++;
	}

	myin.close();
	myout.close();
	
	return 0;
}