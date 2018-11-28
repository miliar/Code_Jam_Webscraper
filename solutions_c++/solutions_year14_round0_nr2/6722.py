#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main() {
	int t;
	ofstream out;
	out.open("B-large.out");
	ifstream in;
	in.open("B-large.in");
	in>>t;
	for(int n=1;n<=t;n++)
	{
    long double p=2.0;
    long double time=0;
    long double c,f,x;
    in>>c>>f>>x;
    while((long double)(c/p + (x/(p+f))) < (long double)(x/p))
    {       
    time=time+(long double)c/p;   
    p=p+f;
    }
    time=time+ (long double)(x/p);
    out<<fixed<<setprecision(7);
    out<<"Case #"<<n<<": ";
    out<<time<<"\n";
    }
	return 0;
}
