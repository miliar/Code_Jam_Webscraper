//#include <cmath>
#include <cstdio>
//#include <vector>
#include <iostream>
//#include <algorithm>
using namespace std;


int main ()
{
	unsigned long long t, n,i,j,caseNumber = 1;
	cin >> t;
	for(i=0;i<t;i++) {
		cin >> n;
		unsigned long long m[n];
		for(j=0;j<n;j++)
			cin >> m[j];

		unsigned long long a,b,y=0,x=0,biggestGap = 0;
		for(a=1;a<n;a++) {
			if(m[a] < m[a-1])
				y += (m[a-1] - m[a]);
		}

		for(b=1;b<n;b++) {
			if(m[b] < m[b-1]) {
				if(m[b-1] - m[b] > biggestGap) biggestGap = (m[b-1] - m[b]);
			}
		}
		for(b=0;b< n - 1;b++) {

				if(m[b] < biggestGap) x += m[b];
				else if (m[b] >= biggestGap) x += biggestGap;

		}

		cout << "Case #" << caseNumber++ << ": " << y << " " << x << endl;
	}
}

