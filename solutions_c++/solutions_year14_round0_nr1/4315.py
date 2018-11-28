#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <sstream>

using namespace std;

long long a,b,c,d,e,f,x,z,zz,y[10];

int main() {
    ofstream fout ("A-small-attempt1.out");
    ifstream fin ("A-small-attempt1.in");
    fin>>a;
    for (b=1; b<=a; b++) {
    	z=0;
    	fin>>x;
    	for (c=1; c<=4; c++) {
    		for (d=1; d<=4; d++) {
    			fin>>e;
    			if (c==x) y[d]=e;
    		}
    	}
    	fin>>x;
    	for (c=1; c<=4; c++) {
    		for (d=1; d<=4; d++) {
    			fin>>e;
    			if (c==x) {
    				for (f=1; f<=4; f++) {
    					if (e==y[f]) {
    						z++;
    						zz=e;
    					}
    				}
    			}
    		}
    	} 
    	fout<<"Case #"<<b<<": ";
    	if (z>1) fout<<"Bad magician!"<<endl; else
    	if (z==0) fout<<"Volunteer cheated!"<<endl; else
    	if (z==1) fout<<zz<<endl;
    }
    return 0;
}
