#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <sstream>

using namespace std;

long long a,b,c,n,d;
double x,y,z,m,p,o;

int main() {
    ofstream fout ("B-large.out");
    ifstream fin ("B-large.in");
    fin>>a;
    for (b=1; b<=a; b++) {
    	fin>>x>>y>>z; n=0; p=0.0; m=2.0;
    	fout<<"Case #"<<b<<": ";
    	if (z<=x) {
    		fout<<fixed<<setprecision(7)<<z/2<<endl;
    	} else {
    		o=z/m; n=0; p=0.0;
    		for (c=1; c<=10000000; c++) {
    			n++;
    			for (d=1; d<=n; d++) {
    				p=p+(x/m); m=m+y;
    				if (d==n) p=p+(z/m);
    			}
    			if (p>=o) {
    				fout<<fixed<<setprecision(7)<<o<<endl;
    				break;
    			} else {
    				o=p;
    				p=0.0;
					m=2;	
    			}
    		}
    	}
    }
    return 0;
}
