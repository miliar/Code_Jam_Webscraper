#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	freopen ("in.txt","r",stdin); freopen("out.txt","w",stdout);
	int ncase, a, b, k;
	cin >> ncase;
	for (int c=0;c<ncase;c++){
		cout << "Case #" << c+1 << ": ";
		cin >> a >> b >> k;
		int act, cont=0;
		for (int i=0;i<a;i++)
			for (int j=0;j<b;j++){
				act=i&j;
				if (act<k) cont++;
			}
		cout << cont << endl;
	}

	return 0;
}