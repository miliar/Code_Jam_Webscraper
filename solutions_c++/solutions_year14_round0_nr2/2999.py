#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
	// freopen("B-large.in","r",stdin);
	// freopen("2.out","w",stdout);
	int T;
	double c,f,x;
	double nf,time;
	cin >> T;
	for (int tt = 0; tt<T; tt++){
		time = 0.0;
		nf = 2.0;
		cin >> c >> f >> x;
		while (true){			
			if (x/nf < (x/(nf + f))+c/nf){
				time += x/nf;
				break;
			}else{					
				time += c/nf;
				nf += f;
				// cout << nf << ' ' << time << endl;
			}
					
		}
		//--------------------- print -----------------
		cout << "Case #" << tt+1 << ": ";
		cout << setiosflags(ios::fixed) << setprecision(7) << time;
		cout << endl;
	}
	
}