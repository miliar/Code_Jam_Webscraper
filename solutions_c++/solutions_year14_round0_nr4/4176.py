#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <sstream>

using namespace std;

long long m,a,b,x,c,d,n,war,dewar;
double nao[1005],ken[1005];

int main() {
    ofstream fout ("D-large.out");
    ifstream fin ("D-large.in");
    fin>>a;
    for (b=1; b<=a; b++) {
    	fin>>x;
    	for (c=1; c<=x; c++) {
    		fin>>nao[c];
    	}
    	for (c=1; c<=x; c++) {
    		fin>>ken[c];
    	}
    	sort(nao+1,nao+x+1);
    	sort(ken+1,ken+x+1);
    	war=0; dewar=0; m=1;
    	for (c=1; c<=x; c++) {
    		for (d=m; d<=x; d++) {
    			if (nao[c]>ken[d]) {
    				dewar++; m++;
    				break;
    			}
    		}
    	}
    	for (c=1; c<=x; c++) {
    		n=0;
    		for (d=1; d<=x; d++) {
    			if (nao[c]<ken[d]) {
    				ken[d]=0.0; n=1;
    				break;
    			}
    		}
    		if (n==0) war++; 
    	}    	
    	fout<<"Case #"<<b<<": "<<dewar<<" "<<war<<endl;
    }
    return 0;
}
