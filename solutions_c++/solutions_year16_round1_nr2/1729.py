#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		int n;
		cin >> n;
		int freq[2501]={0};
		for (int j=0; j<2*n-1; j++)
		{
			for (int k=0; k<n; k++)
			{
				int element;
				cin >> element;
				freq[element]++;
			}
		}
		printf ("Case #%d:",i+1);
		for (int i=0; i<2501; i++)
		{
			if (freq[i]%2==1)
				printf (" %d", i);
		}
		cout << endl;
	}
}
