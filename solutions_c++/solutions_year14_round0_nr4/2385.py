#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>

using namespace std;
typedef double T;

int n,i,j,k,w,dw,l,v,eq;
double tab1[1001], tab2[1001];

int comp (const T * arg1, const T * arg2) {
	if ( * arg1 <* arg2 ) return -1;
	else if ( * arg1 >* arg2 ) return 1;
	return 0;
}

int main(int argc, char **argv)
{
	ifstream test;
	test.open (argv[1]);
	ofstream odp;
	odp.open (argv[2]);
	test >> n;
	for (i=0; i<n; i++) {
		test >> k;
		for (j=0; j<k; j++) {
			test >> tab1[j];
		}
		for (j=0; j<k; j++) {
			test >> tab2[j];
		}
			
	
		qsort(tab1, k, sizeof (* tab1), (int (*)(const void*, const void *)) comp);
		qsort(tab2, k, sizeof (* tab2), (int (*)(const void*, const void *)) comp);
		w = 0; dw = 0; l = 0; eq = 0;
		v = 0;
		for (j=0; j<k; j++) {
			if (tab1[j] > tab2[v]) {
				v++;
				dw++;
			} 
			if (tab2[j] >= tab1[l]) {
				if (tab2[j] == tab1[l]) eq++;
				else {
					l++;
					w++;
				}
			}
		}
		w = k - eq - w;
		odp << "Case #" << i+1 << ": " << dw <<" " << w << endl;
	}
	test.close();
	odp.close();
	
	return 0;
}
