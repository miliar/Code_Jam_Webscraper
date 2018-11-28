#include<iostream>
#include <iomanip>
#include<stdio.h>
using namespace std;

int main() {
	int t;
	double c,f,x;
	cin >> t;
	int i;

	for (int test = 0 ;test < t; test++) {
		int c1,c2;
		int a1[4][4],a2[4][4];
		cin >> c1;
		for (int j = 0;j <4;j++)
			for (int k = 0;k<4;k++)
			 cin >> a1[j][k];

		cin >> c2;
		for (int j = 0;j <4;j++)
			for (int k = 0;k<4;k++)
			 cin >> a2[j][k];

		int count = 0;
		int val = 0;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++) {
				if(a1[c1-1][i] == a2[c2-1][j]) {
					count ++;
					val = a1[c1-1][i];
				}
			}

		if (count == 1)
			printf("Case #%d: %d\n",test+1,val);
		if (count == 0)
			printf("Case #%d: Volunteer cheated!\n",test+1);
		if (count > 1)
			printf("Case #%d: Bad magician!\n", test+1);
	}

	
	return 0;
}
