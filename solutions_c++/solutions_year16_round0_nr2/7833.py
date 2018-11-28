#include <iostream>
#include <fstream>
#include <strings.h>
using namespace std;

int main()
{
    long d,n, m, t,l;
    char s[200];
    //fstream infile("B-small-attempt0.in");
    fstream infile("B-large.in");
//    ofstream outfile("B-small.out");
    ofstream outfile("B-large.out");
    infile >> t;
    cout<<t<<endl;
    for (m=1; m<=t; ++m){
        infile >> s;
        cout<<s<<endl;
        l=strlen(s);
        int x=0;
        if (s[0]=='-')x++;
		for(d=0;d<l;d++)
			if((s[d]=='+')&&(s[d+1]=='-'))x+=2;
	    outfile << "Case #"<<m<<": "<<x<<endl;
   		cout << "Case #"<<m<<": "<<x<<endl; 
    }
    infile.close();
    outfile.close();
}
