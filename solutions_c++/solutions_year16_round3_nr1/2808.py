#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <stdint.h>
using namespace std;

int p(int x[], int l){
	int k=0;
	for (int i = 0; i < l; i++)
	{
		if (x[i] > 0){
			k++;
		}
	}
	return k;
}

int main()
{
	int t;
	cin >> t;
	string alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	for (int cas = 0; cas < t; cas++){
		int n;
		cin >> n;
		int a[26] = { 0 };
		for (int i = 0; i < n; i++)
			cin >> a[i];
		cout << "Case #" << cas + 1 << ": ";
		if (n>2)
			while (p(a,n)>2)
		{
			int mx = a[0];
			int ind=0;
			for (int i = 1; i < n; i++)
			{
				if (mx < a[i]) {
					mx = a[i];
					ind = i;
				}
			}
			cout << alph[ind] << ' ';
			a[ind]--;
			
		}
		int mx=a[0];
		int ind=0, ind2;
		for (int i = 1; i < n; i++)
		{
			if (mx < a[i]) {
				mx = a[i];
				ind = i;
			}
		}
		for (int i = 0; i < n; i++)
		{
			if (a[i] >0 && i!=ind) {
				ind2 = i;
				break;
			}
		}
		while (a[ind]>a[ind2]){
			cout << alph[ind];
			cout << ' ';
			a[ind]--;
		}
		while (a[ind2] > 0)
		{
			cout << alph[ind2];
			cout << alph[ind]; cout << ' ';
			a[ind2]--;
			a[ind]--;
		}

		cout << endl;
	}
	return 0;
}