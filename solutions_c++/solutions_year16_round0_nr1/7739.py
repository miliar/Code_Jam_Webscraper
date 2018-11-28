#include <iostream>
#include <fstream>
using namespace std;
long get_digits(long n)
{
	long i,z,r;
	r=0;
	while (n>0){
		r=r|(1<<(n%10));
		n/=10;
	}
	return r;
}
int main()
{
    long d,n, m, t;
//    fstream infile("A-small-attempt0.in");
    fstream infile("A-large.in");
    ofstream outfile("A-large.out");
    infile >> t;
    cout<<t<<endl;
    for (m=1; m<=t; ++m){
        infile >> n;
        long ii=n;
        cout << n << endl;
		if (n==0){
    	    outfile << "Case #"<<m<<": INSOMNIA"<<endl;
       		cout << "Case #"<<m<<": INSOMNIA"<<endl;
       		continue;
		}
		else{
			d=get_digits(n);
			while(d!=1023)
			{
				n+=ii;
				d=d|get_digits(n);
			}
		    outfile << "Case #"<<m<<": "<<n<<endl;
       		cout << "Case #"<<m<<": "<<n<<endl; 
       	}
    }
    infile.close();
    outfile.close();
}
