#include<iostream>
#include <iomanip>
#include<stdio.h>
#include<algorithm>
using namespace std;

int main() {
	int t;
	double c,f,x;
	cin >> t;
	int i;

	for (int i = 0 ;i < t; i++) {
		int n;
		cin >> n;
		double a[1000], b[1000];
		for (int j=0;j<n;j++)
			cin >> a[j];
		for (int j=0;j<n;j++)
			cin >> b[j];
	sort(a,a+n);
	sort(b,b+n);
	/*cout << endl;
	cout << endl;
		for (int j=0;j<n;j++)
	cout << a[j] << " ";
	cout << endl;
		for (int j=0;j<n;j++)
	cout << b[j] << " ";
	cout << endl;*/
	int a_s = 0, b_s = 0;
	int count = 0, breakp=0;
	
	while(1) {
		if (a[a_s] > b[b_s])
		{
			count++;
			a_s++;
			b_s++;
		}
		else
			a_s++;
		breakp++;
		if (breakp==n)
			break;
	}
	a_s = n-1;
	b_s = n-1;
	breakp =0 ;
	int war = 0;
	while (1)
	{
		if (a[a_s] > b[b_s])
		{
			war++;
		}
		else
			b_s--;
		a_s--;

		breakp++;
		if(breakp==n)
			break;
	}
	printf("Case #%d: %d %d\n",i+1,count,war);
	}

	
	return 0;
}
